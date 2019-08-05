import contextlib
import morph
import numpy as np
from sensel import sensel
from pathlib import Path
# redirect stdout to nowhere
with contextlib.redirect_stdout(None):
    import pygame

WINDOW_SIZE_MULTIPLE = 4
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FRAMERATE = 250  # Hz
CALIBRATION_LENGTH = 3  # seconds
CALIBRATION_FRAMES = FRAMERATE * CALIBRATION_LENGTH
NUM_CONTACTS = 5


class ForceGame():
    def __init__(self):
        self.forcepad = morph.Morph()
        icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(icon)
        (self.width, self.height) = (WINDOW_SIZE_MULTIPLE * self.forcepad.cols,
                                     WINDOW_SIZE_MULTIPLE * self.forcepad.rows)
        # self.calibrate()
        self.mean_force_rest = np.array([20, 20, 20, 20, 20])
        self.mean_force_press = np.array([150, 150, 150, 150, 150])
        self.generate_mapping()
        self.run_game()

    def calibrate(self):
        # we assume that you can produce any force within these
        # ranges at any desired level, so we can choose four random
        # vectors to serve as our "corners" to then produce a mapping

        # get min and max force levels for fingers #
        calibration_matrix_rest = np.zeros((NUM_CONTACTS, CALIBRATION_FRAMES))
        calibration_matrix_press = np.zeros((NUM_CONTACTS, CALIBRATION_FRAMES))
        calibrating = True
        while calibrating:
            ready = False
            print("Rest five fingers on the force pad.")
            contacted = 0
            while not ready:
                frames = self.forcepad.read_frames()
                for frame in frames:
                    if frame.n_contacts == NUM_CONTACTS:
                        contacted += 1
                    else:
                        "broke contact, restarting."
                        contacted = 0
                    if contacted > 100:
                        print("ready.")
                        ready = True
                        recording_rest = True
                        recording_press = False
                        col_idx = 0
            print("starting calibration record.")
            while recording_rest:
                frames = self.forcepad.read_frames()
                for frame in frames:
                    if frame.n_contacts != NUM_CONTACTS:
                        print("detected liftoff, restarting calibration.")
                        recording_rest = False
                        col_idx = 0
                        calibration_matrix_press = np.zeros(
                            (NUM_CONTACTS, CALIBRATION_FRAMES))
                        calibration_matrix_rest = np.zeros(
                            (NUM_CONTACTS, CALIBRATION_FRAMES))
                    else:
                        forces = np.zeros((NUM_CONTACTS))
                        for i in range(NUM_CONTACTS):
                            forces[i] = frame.contacts[i].total_force
                        if col_idx > calibration_matrix_rest.shape[1] - 1:
                            recording_rest = False
                            recording_press = True
                            col_idx = 0
                        else:
                            calibration_matrix_rest[:, col_idx] = forces
                            col_idx += 1
            print("starting calibration press \n push fingers into the pad")
            while recording_press:
                frames = self.forcepad.read_frames()
                for frame in frames:
                    if frame.n_contacts != NUM_CONTACTS:
                        print("detected liftoff, restarting calibration.")
                        recording_press = False
                        col_idx = 0
                        calibration_matrix_press = np.zeros(
                            (NUM_CONTACTS, CALIBRATION_FRAMES))
                        calibration_matrix_rest = np.zeros(
                            (NUM_CONTACTS, CALIBRATION_FRAMES))
                    else:
                        forces = np.zeros((NUM_CONTACTS))
                        for i in range(NUM_CONTACTS):
                            forces[i] = frame.contacts[i].total_force
                        if col_idx > calibration_matrix_press.shape[1] - 1:
                            print("calibration complete.")
                            recording_press = False
                            calibrating = False
                        else:
                            calibration_matrix_press[:, col_idx] = forces
                            col_idx += 1
        self.mean_force_rest = np.mean(calibration_matrix_rest, axis=1)
        self.mean_force_press = np.mean(calibration_matrix_press, axis=1)
        print(f"mean force rest = {self.mean_force_rest}")
        print(f"mean force press= {self.mean_force_press}")

    def generate_mapping(self, random=True):
        # "force" vectors
        up = np.array([[0], [1]])
        down = np.array([[0], [-1]])
        left = np.array([[-1], [0]])
        right = np.array([[1], [0]])
        output_zeros = np.zeros((2, 1))

        input_zeros = np.zeros((NUM_CONTACTS, 1))
        if random:
            inputs = []
            for i in range(4):
                vec = []
                for low, high in zip(self.mean_force_rest,
                                     self.mean_force_press):
                    vec.append(np.random.uniform(low, high))
                inputs.append(np.array(vec))

        C = np.block([[up, output_zeros, output_zeros, output_zeros], [
            output_zeros, down, output_zeros, output_zeros
        ], [output_zeros, output_zeros, left, output_zeros],
                      [output_zeros, output_zeros, output_zeros, right]])

        R = np.block([[
            inputs[0].reshape(-1, 1), input_zeros, input_zeros, input_zeros
        ], [input_zeros, inputs[1].reshape(-1, 1), input_zeros, input_zeros], [
            input_zeros, input_zeros, inputs[2].reshape(-1, 1), input_zeros
        ], [input_zeros, input_zeros, input_zeros, inputs[3].reshape(-1, 1)]])

        Rinv = np.linalg.pinv(R)
        Abig = np.dot(C, Rinv)

        self.A = Abig[:2, :NUM_CONTACTS]
        print(f"mapping shape {self.A.shape}")

    def run_game(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('move dot')
        self.screen.fill(WHITE)
        pygame.display.flip()
        running = True
        force_delta = np.zeros((2))
        circle_loc = np.array([self.width // 2, self.height // 2])
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.forcepad.close()
                    running = False
            self.screen.fill(WHITE)
            frames = self.forcepad.read_frames()
            forces = np.zeros(NUM_CONTACTS)
            for frame in frames:
                if frame.n_contacts == NUM_CONTACTS:
                    for i in range(NUM_CONTACTS):
                        c = frame.contacts[i]
                        forces[i] = c.total_force
                    force_delta = np.dot(self.A, forces.reshape(
                        NUM_CONTACTS, 1))
                    next_x = circle_loc[0] + int(force_delta[0])
                    next_y = circle_loc[1] + int(force_delta[1])
                    if next_x > 0 and next_x < self.width and next_y > 0 and next_y > self.height:
                        circle_loc[0] = next_x
                        circle_loc[1] = next_y
                    pygame.draw.circle(self.screen, BLUE,
                                       (circle_loc[0], circle_loc[1]), 10)
                    print("circle ", circle_loc)
            pygame.display.flip()


if __name__ == "__main__":
    game = ForceGame()

# sensel contact attributes:
# 'area'
# 'content_bit_mask'
# 'delta_area'
# 'delta_force'
# 'delta_x'
# 'delta_y'
# 'id'
# 'major_axis'
# 'max_x'
# 'max_y'
# 'min_x'
# 'min_y'
# 'minor_axis'
# 'orientation'
# 'peak_force'
# 'peak_x'
# 'peak_y'
# 'state'
# 'total_force'
# 'x_pos'
# 'y_pos'

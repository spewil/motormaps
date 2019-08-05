import contextlib
import morph
import numpy as np
from sensel import sensel
from pathlib import Path
# redirect stdout to nowhere
with contextlib.redirect_stdout(None):
    import pygame

WINDOW_SIZE_MULTIPLE = 3
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FRAMERATE = 250  # Hz
CALIBRATION_LENGTH = 3  # seconds
CALIBRATION_FRAMES = FRAMERATE * CALIBRATION_LENGTH
NUM_CONTACTS = 5


class ForceGame():
    def __init__(self):
        self.forcepad = morph.Morph()
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        (self.width, self.height) = (WINDOW_SIZE_MULTIPLE * self.forcepad.cols,
                                     WINDOW_SIZE_MULTIPLE * self.forcepad.rows)
        self.calibrate()
        self.generate_mapping()

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
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.forcepad.close()
                    running = False
            self.screen.fill(WHITE)
            frames = self.forcepad.read_frames()
            forces = []
            for frame in frames:
                if frame.n_contacts > 0:
                    for c in frame.contacts:
                        if c.state == sensel.CONTACT_START:
                            sensel.setLEDBrightness(self.forcepad.handle, c.id,
                                                    100)
                        elif c.state == sensel.CONTACT_END:
                            sensel.setLEDBrightness(self.forcepad.handle, c.id,
                                                    0)
                        forces.append(c.total_force)
                        pygame.draw.circle(
                            self.screen, BLUE,
                            (int(2 * c.x_pos), int(2 * c.y_pos)), 10)
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

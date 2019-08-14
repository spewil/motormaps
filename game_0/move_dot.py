import contextlib
import morph
import numpy as np
from sensel import sensel
from pathlib import Path
from pprint import pprint
# redirect stdout to nowhere
with contextlib.redirect_stdout(None):
    import pygame

WINDOW_SIZE_MULTIPLE = 6
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FRAMERATE = 250  # Hz
CALIBRATION_LENGTH = 3  # seconds
CALIBRATION_FRAMES = FRAMERATE * CALIBRATION_LENGTH
NUM_CONTACTS = 4
OFFSET = 150
CENTER = OFFSET + 100
FORCE = 10
SCALE = 5
MAP_POSITION = False
"""
TODO:
- make mini Morph API directly from C code instead of two modules
- implement modulo width, height for periodic boundary conditions
- add target and reset
- add timer for reset
- add scorekeeping
- time varying dynamics?
- 4 finger random calibration vector finger
- 5 finger random calibration vector

DONE
- pause when fingers are lifted off
"""


class DotGame():
    def __init__(self):
        self.forcepad = morph.Morph()
        icon = pygame.image.load('../assets/icon.png')
        pygame.display.set_icon(icon)
        (self.width, self.height) = (WINDOW_SIZE_MULTIPLE * self.forcepad.cols,
                                     WINDOW_SIZE_MULTIPLE * self.forcepad.rows)
        self.mean_force_rest = np.array([20, 20, 20, 20, 20])
        self.mean_force_press = np.array([150, 150, 150, 150, 150])

        if not MAP_POSITION:
            self.A = self.generate_force_mapping(NUM_CONTACTS)
            self.state_dynamics = np.eye(2, 2) + np.random.normal(
                scale=.01, size=(2, 2))
            pprint(self.state_dynamics)
            theta = np.radians(30)
            c, s = np.cos(theta), np.sin(theta)
            R = np.array(((c, -s), (s, c)))
            self.control_dynamics = R
        else:
            self.calibrate()
            self.A = self.generate_position_mapping(self.width, self.height,
                                                    NUM_CONTACTS)
        self.run_game()

    def generate_target(self):

        target_loc = np.random.uniform(2, 1)
        pygame.draw.circle(self.screen, RED, (target_loc[0], target_loc[1]),
                           25)

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

    def generate_position_mapping(self, width, height, num_contacts):
        # calibration vectors
        top_left = np.array([[0], [0]])
        top_right = np.array([[width], [0]])
        bottom_left = np.array([[0], [height]])
        bottom_right = np.array([[width], [height]])

        inputs = []
        for i in range(num_contacts):
            z = np.ones((num_contacts)) * OFFSET
            z[i] = CENTER
            inputs.append(z)
        input_zeros = np.ones((1, num_contacts)) * OFFSET

        S = np.vstack([top_left, top_right, bottom_left, bottom_right])

        # this should be done programatically
        F = np.block([[inputs[0].reshape(1, -1),
                       input_zeros], [input_zeros, inputs[0].reshape(1, -1)],
                      [inputs[1].reshape(1, -1),
                       input_zeros], [input_zeros, inputs[1].reshape(1, -1)],
                      [inputs[2].reshape(1, -1),
                       input_zeros], [input_zeros, inputs[2].reshape(1, -1)], [
                           inputs[3].reshape(1, -1), input_zeros
                       ], [input_zeros, inputs[3].reshape(1, -1)]])

        Fplus = np.linalg.pinv(F)
        Avec = np.dot(Fplus, S)

        A = Avec.reshape(2, -1)

        # write some assertions here for shapes

        return A

    def generate_force_mapping(self, num_contacts):
        # calibration vectors
        top_left = np.array([[FORCE], [0]])
        top_right = np.array([[-FORCE], [0]])
        bottom_left = np.array([[0], [FORCE]])
        bottom_right = np.array([[0], [-FORCE]])

        inputs = []
        for i in range(num_contacts):
            z = np.ones((num_contacts)) * OFFSET
            z[i] = CENTER
            inputs.append(z)
        input_zeros = np.ones((1, num_contacts)) * OFFSET

        calibration_vectors = [top_left, top_right, bottom_left, bottom_right]
        np.random.shuffle(calibration_vectors)
        S = np.vstack(calibration_vectors)

        # this should be done programatically
        F = np.block([[inputs[0].reshape(1, -1),
                       input_zeros], [input_zeros, inputs[0].reshape(1, -1)],
                      [inputs[1].reshape(1, -1),
                       input_zeros], [input_zeros, inputs[1].reshape(1, -1)],
                      [inputs[2].reshape(1, -1),
                       input_zeros], [input_zeros, inputs[2].reshape(1, -1)], [
                           inputs[3].reshape(1, -1), input_zeros
                       ], [input_zeros, inputs[3].reshape(1, -1)]])

        Fplus = np.linalg.pinv(F)
        Avec = np.dot(Fplus, S)

        A = Avec.reshape(2, -1)

        # write some assertions here for shapes

        return A

    def increment_dynamics(self, current_state, current_input):

        return np.dot(self.state_dynamics, current_state) + np.dot(
            self.control_dynamics, current_input) + 0 * np.random.normal(
                scale=SCALE, size=(self.state_dynamics.shape[0], 1))

    def run_game(self):
        pygame.init()
        fontname = pygame.font.match_font('sourcecodepro')
        print(fontname)
        self.screen = pygame.display.set_mode((self.width, self.height))
        font = pygame.font.Font(fontname, 32)
        font.set_bold(True)
        text = font.render('Paused.', True, BLUE)
        textRect = text.get_rect()
        textRect.center = (self.width // 2, self.height // 2)
        pygame.display.set_caption('move dot')
        pygame.display.flip()
        self.screen.fill(BLACK)
        running = True
        circle_loc = np.array([self.width // 2, self.height // 2])
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.forcepad.close()
                    running = False
            frames = self.forcepad.read_frames()
            forces = np.zeros(NUM_CONTACTS)
            self.screen.fill(BLACK)
            for frame in frames:
                if frame.n_contacts == NUM_CONTACTS:
                    for i in range(NUM_CONTACTS):
                        c = frame.contacts[i]
                        forces[i] = c.total_force
                    S = np.dot(self.A, forces.reshape(NUM_CONTACTS, 1))
                    if not MAP_POSITION:
                        next_loc = self.increment_dynamics(
                            circle_loc.reshape(-1, 1), S.reshape(-1, 1))
                    else:
                        next_loc = S
                    if next_loc[0] > 0 and next_loc[0] < self.width and next_loc[1] > 0 and next_loc[1] < self.height:
                        circle_loc = next_loc
                    pygame.draw.circle(self.screen, BLUE,
                                       (circle_loc[0], circle_loc[1]), 10)
                else:
                    self.screen.fill(GREY)
                    self.screen.blit(text, textRect)

            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    game = DotGame()

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

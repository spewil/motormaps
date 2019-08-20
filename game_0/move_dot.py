import contextlib
import morph
import utils
import time
import numpy as np
from pprint import pprint
# redirect stdout to nowhere
with contextlib.redirect_stdout(None):
    import pygame

from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

FRAMERATE = 250  # Hz ## for morph
WINDOW_SIZE_MULTIPLE = 8
FULLSCREEN = True

CALIBRATE = False
CALIBRATION_LENGTH = 3  # seconds
CALIBRATION_FRAMES = FRAMERATE * CALIBRATION_LENGTH

MAP_POSITION = False
TIME_DEPENDENCE = False
NUM_CONTACTS = 5
NOISE_AMP = 0
NOISE_SCALE = 5
CURSOR_SIZE = 10
TARGET_SIZE = 25
TIME_LIMIT = 10
OFFSET = 150  # morph units
CENTER = OFFSET + 100  # morph units
FORCE = 10  # d_pixels
NUM_LEVELS = 100
TIME_UP = False
HIT = False
QUIT = False
"""
TODO:
- timer
- liftoff means fingers get remapped?
    - make it such that the order is the same (left to right)
- test and debug calibration for force mapping
- write data to file
    - list of dictonaries, dictionary per "level"
    - append file each level (file per session)
    - liftoffs? restart level on liftoff?
    - inputs in morph coordinates
    - inputs in screen coordinates
    - hits / misses
    - time to hit
    - target positions
- time varying dynamics?
- make mini Morph API directly from C code instead of two modules
- implement modulo width, height for periodic boundary conditions

DONE
- 5 finger calibration vector
- pause when fingers are lifted off
- add target and reset
- add scorekeeping
- add timer for reset
- fix Pause (its really distracting)
- Paused doesn't actually pause the timer

GAME MODES
- position
- 4-finger force (random rotation)
- 5-finger force (random rotation)

"""


class DotGame():
    def __init__(self, test=False):
        self.forcepad = morph.Morph()
        icon = pygame.image.load('../assets/icon.png')
        pygame.display.set_icon(icon)
        self.setup_screen()
        self.setup_params()
        self.run_game()

    def setup_params(self):
        if CALIBRATE:
            pass
        else:
            self.mean_force_rest = np.array([20, 20, 20, 20, 20])
            self.mean_force_press = np.array([150, 150, 150, 150, 150])
        self.A = self.generate_mapping(NUM_CONTACTS)
        self.state_time = 0

    def generate_state_transform(self, time, space):
        return np.eye(2, 2)

    def generate_control_transform(self, time, space):
        return np.eye(2, 2)

    def increment_dynamics(self, current_state, current_input):
        state_dynamics = self.generate_state_transform(self.state_time,
                                                       self.circle_loc)
        control_dynamics = self.generate_control_transform(
            self.state_time, self.circle_loc)
        return np.dot(state_dynamics, current_state) + np.dot(
            control_dynamics, current_input) + NOISE_AMP * np.random.normal(
                scale=NOISE_SCALE, size=(state_dynamics.shape[0], 1))

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
            print(f"Rest {NUM_CONTACTS} fingers on the force pad.")
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

    def generate_mapping(self, num_contacts):

        if MAP_POSITION:
            # output calibration vectors -- screen coords
            top_left = np.array([[0], [0]])
            top_right = np.array([[self.width], [0]])
            bottom_left = np.array([[0], [self.height]])
            bottom_right = np.array([[self.width], [self.height]])
            S = np.vstack([top_left, top_right, bottom_left, bottom_right])

        else:
            # input calibration vectors -- morph force coords
            calibration_vectors = np.array(
                utils.roots_of_unity(num_contacts, FORCE), dtype=np.int8)
            np.random.shuffle(calibration_vectors)
            S = np.vstack(calibration_vectors)

        # output calibration vectors -- screen coords
        inputs = []
        input_zeros = np.ones((1, num_contacts)) * OFFSET
        for i in range(num_contacts):
            z = np.ones((num_contacts)) * OFFSET
            z[i] = CENTER
            inputs.append([z.reshape(1, -1), input_zeros])
            inputs.append([input_zeros, z.reshape(1, -1)])
        F = np.block(inputs)

        Fplus = np.linalg.pinv(F)
        Avec = np.dot(Fplus, S)
        A = Avec.reshape(2, -1)
        return A

    def setup_screen(self):
        pygame.init()
        if FULLSCREEN:
            display = pygame.display.Info()
            self.width, self.height = display.current_w, display.current_h - 50
        else:
            (self.width,
             self.height) = (WINDOW_SIZE_MULTIPLE * self.forcepad.cols,
                             WINDOW_SIZE_MULTIPLE * self.forcepad.rows)
        fontname = pygame.font.match_font('sourcecodepro')
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('move dot')
        self.pause_font = pygame.font.Font(fontname, 32)
        self.pause_font.set_bold(True)
        self.pause_text = self.pause_font.render('Paused.', True, BLUE)
        self.pause_textRect = self.pause_text.get_rect()
        self.pause_textRect.center = (self.width // 2, self.height // 2)
        pygame.display.flip()

        self.score = 0
        self.score_font = pygame.font.Font(fontname, 28)
        self.score_font.set_bold(True)
        self.score_text = self.score_font.render(f"Score: {self.score}", True,
                                                 WHITE)
        self.score_textRect = self.score_text.get_rect()
        self.score_textRect.center = (self.width - self.score_textRect.width,
                                      self.score_textRect.height)

        self.time = TIME_LIMIT
        self.time_font = pygame.font.Font(fontname, 28)
        self.time_font.set_bold(True)
        self.time_text = self.time_font.render(f"{self.time}", True, WHITE)
        self.time_textRec = self.time_text.get_rect()
        self.time_textRec.center = (self.time_textRec.width * 3,
                                    self.time_textRec.height)

    def decrement_timer(self):
        self.time -= 1
        if self.time > 3:
            self.time_text = self.time_font.render(f"{self.time}", True, WHITE)
        else:
            self.time_text = self.time_font.render(f"{self.time}", True, RED)

    def reset(self):
        global TIME_UP
        self.time = TIME_LIMIT
        self.time_text = self.time_font.render(f"{self.time}", True, WHITE)
        TIME_UP = False

    def increment_score(self):
        print("HIT")
        self.score += 1
        self.score_text = self.score_font.render(f"Score: {self.score}", True,
                                                 WHITE)

    def generate_target(self):
        target = utils.random_radial_vector((self.height // 2) - 5)
        target[0] += self.width // 2
        target[1] += self.height // 2
        return target

    def run_level_loop(self):
        global TIME_UP
        global HIT
        global QUIT
        self.screen.fill(BLACK)
        running = True
        self.target_loc = self.generate_target().reshape(2, 1)
        self.circle_loc = np.array([self.width // 2,
                                    self.height // 2]).reshape(2, 1)
        local_time = time.time()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    QUIT = True
            self.screen.fill(BLACK)
            self.screen.blit(self.score_text, self.score_textRect)
            frames = self.forcepad.read_frames()
            forces = np.zeros(NUM_CONTACTS)
            for frame in frames:
                if frame.n_contacts == NUM_CONTACTS:
                    if time.time() - local_time > 1:
                        local_time = time.time()
                        self.decrement_timer()
                    if self.time == 0:
                        TIME_UP = True
                        running = False
                    self.state_time += 1
                    for i in range(NUM_CONTACTS):
                        # save left-right position of contacts
                        c = frame.contacts[i]
                        # out of loop, sort by position and assign force only
                        forces[i] = c.total_force
                    S = np.dot(self.A, forces.reshape(NUM_CONTACTS, 1))
                    if not MAP_POSITION:
                        next_loc = self.increment_dynamics(
                            self.circle_loc.reshape(-1, 1), S.reshape(-1, 1))
                    else:
                        next_loc = S
                    if next_loc[0] > 0 and next_loc[0] < self.width and next_loc[1] > 0 and next_loc[1] < self.height:
                        self.circle_loc = next_loc
                    if np.linalg.norm(
                            self.circle_loc - self.target_loc) < TARGET_SIZE:
                        HIT = True
                        running = False
                else:
                    self.screen.blit(self.pause_text, self.pause_textRect)

            self.screen.blit(self.time_text, self.time_textRec)
            pygame.draw.circle(self.screen, BLUE,
                               (self.circle_loc[0], self.circle_loc[1]),
                               CURSOR_SIZE)
            pygame.draw.circle(self.screen, RED,
                               (self.target_loc[0], self.target_loc[1]),
                               TARGET_SIZE)
            pygame.display.flip()

    def run_game(self):
        global HIT
        global QUIT
        for level in range(NUM_LEVELS):
            self.run_level_loop()
            if HIT:
                self.increment_score()
            if QUIT:
                break
            self.reset()
        self.forcepad.close()
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

import numpy as np
from pprint import pprint

OFFSET = 150
CENTER = OFFSET + 100
FORCE = 10


def generate_position_mapping(width, height, num_contacts):
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
    pprint(S)

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


def generate_force_mapping(num_contacts):
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
    pprint(S)

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

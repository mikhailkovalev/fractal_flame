import sys
import numpy as np
from random import randint
from functools import partial
from PIL import Image

from transformations import LinearTransformation


def print_percentage(i, iteration_count, process, frequency=10):
    if i == 0:
        return

    if i % frequency == 0:
        percentage = 100 * i / iteration_count
        print('{} {:.2f}%'.format(process, percentage), end='')
        sys.stdout.flush()


def main():
    transformations = (
        LinearTransformation(
            np.array((0.5, 0.5, 0.5, -0.5)).reshape((2, 2)),
            np.array((0.0, 0.0))
        ),
        LinearTransformation(
            np.array((0.5, 0.5, -0.5, 0.5)).reshape((2, 2)),
            np.array((0.5, 0.5))
        ),
    )

    colors = (
        (255, 201, 14),
        (34, 177, 76),
    )

    transformation_count = len(transformations)

    assert(len(colors) == transformation_count)

    get_idx = partial(randint, 0, transformation_count-1)

    point = np.array((0.1, 0.1))

    width, height = 800, 494

    iteration_count = 10000


    for i in range(iteration_count):
        print_percentage(i, iteration_count, 'Generated')
        idx = get_idx()
        chosen_transformation = transformations[idx]
        chosen_color = colors[idx]



if __name__ == '__main__':
    main()
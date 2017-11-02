import sys
import numpy as np
from random import choice
from operator import itemgetter
from PIL import Image

from transformations import LinearTransformation


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

    point = np.array((1, 0.1))

    width, height = 800, 494

    iteration_count = 1000000
    points = [None] * iteration_count

    for i in range(iteration_count):
        if i % 5 == 0:
            percentage = 100 * i / iteration_count
            if i > 0:
                print('\r', end='')
            print('Generated {:.2f}%'.format(percentage), end='')
            sys.stdout.flush()
        t = choice(transformations)
        point = t.apply(point)
        points[i] = point
    print()

    x_min = min(map(itemgetter(0), points))
    x_max = max(map(itemgetter(0), points))

    y_min = min(map(itemgetter(1), points))
    y_max = max(map(itemgetter(1), points))

    ax = (width-1) / (x_max-x_min)
    bx = -ax * x_min

    ay = (height-1) / (y_min-y_max)
    by = -ay * y_max

    image_data = [1] * (width*height)

    for i, point in enumerate(points):
        if i % 5 == 0:
            percentage = 100 * i / iteration_count
            if i > 0:
                print('\r', end='')
            print('Rendered {:.2f}%'.format(percentage), end='')
            sys.stdout.flush()
        x, y = point
        row = int(ay*y + by)
        column = int(ax*x + bx)
        image_data[column + row * width] = 0
    print()

    img = Image.new('1', (width, height))
    img.putdata(image_data)
    img.save('./out.png')


if __name__ == '__main__':
    main()

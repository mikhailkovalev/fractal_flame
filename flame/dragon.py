import numpy as np
from math import ceil
from operator import itemgetter
from PIL import Image, ImageDraw

from transformations import LinearTransformation


def main():
    t2 = LinearTransformation(
        np.array((-0.5, -0.5, 0.5, -0.5)).reshape((2, 2)),
        np.array((490.0, 120.0))
    )
    t1 = LinearTransformation(
        np.array((0.5, -0.5, 0.5, 0.5)).reshape((2, 2)),
        np.array((340.0, -110.0))
    )

    points = [np.array((0.0, 0.0))]
    points_count = 1
    iteration_count = 2
    for i in range(iteration_count):
        new_points_count = points_count << 1
        new_points = [None] * new_points_count
        for j, point in enumerate(points):
            idx = j << 1
            new_points[idx] = t1.apply(point)
            new_points[idx+1] = t2.apply(point)
        points = new_points
        points_count = new_points_count

    min_x = min(map(itemgetter(0), points))
    max_x = max(map(itemgetter(0), points))
    min_y = min(map(itemgetter(1), points))
    max_y = max(map(itemgetter(1), points))

    points = list(map(lambda x: (x[0]-min_x, x[1]-min_y), points))

    img = Image.new('1', (ceil(max_x - min_x), ceil(max_y - min_y)), 1)
    draw = ImageDraw.Draw(img)
    draw.line(points, fill=0)
    print(points)
    img.show()


if __name__ == '__main__':
    main()
import random
import numpy as np
from functools import partial

from transformations import (LinearTransformation, SinusoidalTransformation, 
                             DiskTransformation, HeartTransformation, 
                             PolarTransformation, SphericalTransformation)


def main():
    point_count = 100
    image_size = (809, 500)
    linear_transformations_count = 10
    active_iteration_count = 10
    inactive_iteration_count = 20

    linear_transformations = [
        LinearTransformation.generate() 
        for i in range(linear_transformations_count)
    ]

    non_linear_transformations = [
        SinusoidalTransformation(),
        DiskTransformation(),
        HeartTransformation(),
        PolarTransformation(),
        SphericalTransformation(),
    ]
    non_linear_transformations_count = len(non_linear_transformations)

    min_image_size = min(image_size)

    x_radius, y_radius = (e / min_image_size for e in image_size)
    get_x = partial(random.uniform, -x_radius, x_radius)
    get_y = partial(random.uniform, -y_radius, y_radius)

    for point_idx in range(point_count):
        point = np.array((get_x(), get_y()))

        for iteration_idx in range(-inactive_iteration_count,
                                   active_iteration_count):
            transformation_idx = random.randrange(
                linear_transformations_count)

            point = linear_transformations[
                transformation_idx].apply(point)

            transformation_idx = random.randrange(
                non_linear_transformations_count)
            point = non_linear_transformations[
                transformation_idx].apply(point)


if __name__ == '__main__':
    main()

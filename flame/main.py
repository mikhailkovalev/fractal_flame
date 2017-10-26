import random
import numpy as np
from PIL import Image
from operator import mul
from functools import partial

from transformations import (LinearTransformation, SinusoidalTransformation, 
                             DiskTransformation, HeartTransformation, 
                             PolarTransformation, SphericalTransformation)


def main():
    point_count = 10000
    image_size = (809, 500)
    linear_transformations_count = 5
    active_iteration_count = 30
    inactive_iteration_count = 0

    linear_transformations = [
        LinearTransformation.generate() 
        for i in range(linear_transformations_count)
    ]

    colors = [
        tuple((random.randrange(256) for j in range(3)))
        for i in range(linear_transformations_count)
    ]

    non_linear_transformations = [
        # SinusoidalTransformation(),
        # DiskTransformation(),
        # HeartTransformation(),
        # PolarTransformation(),
        # SphericalTransformation(),
    ]
    non_linear_transformations_count = len(non_linear_transformations)

    min_image_size = min(image_size)

    x_radius, y_radius = (e / min_image_size for e in image_size)
    
    get_x = partial(random.uniform, -x_radius, x_radius)
    get_y = partial(random.uniform, -y_radius, y_radius)
    
    offset_x = 0.5 * image_size[0]
    scale_x = offset_x / x_radius
    
    offset_y = 0.5 * image_size[1]
    scale_y = offset_y / y_radius
    
    def to_screen(point):
        return (int(0.5 + point[0] * scale_x + offset_x), 
                int(0.5 + point[1] * scale_y + offset_y))

    def get_idx(point):
        column, row = to_screen(point)
        return row * image_size[1] + column

    img = Image.new('RGB', image_size)
    img_data = list(img.getdata())
    pixel_counters = [0] * mul(*image_size)
                
    for point_idx in range(point_count):
        percentage = 100 * point_idx / point_count
        if point_idx > 0:
            print('\r', end='')
        print('Done {:.2f}%'.format(percentage), end='')
        point = np.array((get_x(), get_y()))

        for iteration_idx in range(-inactive_iteration_count,
                                   active_iteration_count):
            transformation_idx = random.randrange(
                linear_transformations_count)

            color = colors[transformation_idx]

            point = linear_transformations[
                transformation_idx].apply(point)

            #transformation_idx = random.randrange(
            #    non_linear_transformations_count)
            #point = non_linear_transformations[
            #    transformation_idx].apply(point)
            
            if (iteration_idx > 0 and 
                    np.fabs(point[0]) <= x_radius and 
                    np.fabs(point[1]) <= y_radius):
                pixel_idx = get_idx(point)
                
                if pixel_counters[pixel_idx] == 0:
                    img_data[pixel_idx] = color
                else:
                    img_data[pixel_idx] = tuple(map(lambda x, y: (x+y) >> 1, img_data[pixel_idx], color))
                   
                pixel_counters[pixel_idx] += 1

    img.putdata(img_data)
    img.save('./out.png')
    print()
    img.show()


if __name__ == '__main__':
    main()

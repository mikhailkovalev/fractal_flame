import math
import random
import numpy as np


class Transformation:
    def apply(self, point):
        pass


class LinearTransformation(Transformation):
    __radius = 1.2

    def __init__(self, matrix, offset, color):
        self.matrix = matrix
        self.offset = offset
        self.color = color

    def apply(self, point):
        return np.dot(self.matrix, np.array(point)) + self.offset

    @classmethod
    def generate(cls):
        c = random.uniform(-cls.__radius, cls.__radius)
        f = random.uniform(-cls.__radius, cls.__radius)

        while True:
            a = random.uniform(-1.0, 1.0)
            b = random.uniform(-1.0, 1.0)

            d_radius = math.sqrt(1.0 - a*a)
            e_radius = math.sqrt(1.0 - b*b)

            d = random.uniform(-d_radius, d_radius)
            e = random.uniform(-e_radius, e_radius)

            t1 = a*a + b*b + d*d + e*e
            t2 = a*e - b*d

            if t1 < 1 + t2*t2:
                break
    
        matrix = np.array((a, b, c, d)).reshape((2, 2))
        offset = np.array((c, f))
        color = [random.random() for i in range(3)]
        return cls(matrix, offset, color)


class SinusoidalTransformation(Transformation):
    def apply(self, point):
        return np.sin(point)

class SphericalTransformation(Transformation):
    def apply(self, point):
        x, y = point
        z = x*x + y*y
        return np.array((x/z, y/z))


class PolarTransformation(Transformation):
    def apply(self, point):
        x, y = point
        return np.array((np.arctan(y, x)/np.pi, np.sqrt(x*x + y*y) - 1))


class HeartTransformation(Transformation):
    def apply(self, point):
        x, y = point
        r = np.linalg.norm(point)
        phi = np.arctan(y/x)
        return np.array((r*np.sin(r*phi), -r*np.cos(r*phi)))


class DiskTransformation(Transformation):
    def apply(self, point):
        x, y = point
        r = np.linalg.norm(point)
        phi = np.arctan(y/x)
        new_x = phi * np.sin(np.pi*r) / np.pi
        new_y = phi * np.cos(r*np.pi) / np.pi
        return np.array((new_x, new_y))

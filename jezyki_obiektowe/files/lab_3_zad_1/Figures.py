import math


class GeometricShape:

    def calculate_field(self):
        pass


class Square(GeometricShape):
    def __init__(self, a):
        self.a = a

    def calculate_field(self):
        return self.a * self.a



class Rectangle(GeometricShape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_field(self):
        return self.a * self.b


class Circle(GeometricShape):

    def __init__(self, r):
        self.r = r

    def calculate_field(self):
        return math.pi * (self.r * self.r)


class Triangle(GeometricShape):

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def calculate_field(self):
        return (self.a * self.h) / 2


class Trapeze(GeometricShape):

    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def calculate_field(self):
        return ((self.a + self.b) / 2) * self.h

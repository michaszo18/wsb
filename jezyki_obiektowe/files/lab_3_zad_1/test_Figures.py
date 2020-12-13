from unittest import TestCase

from lab_3_zad_1.Figures import Square


class GeometricShape(TestCase):

    def test_square_int(self):
        gs = Square(4)
        self.assertEqual(gs.calculate_field(), 16)

    def test_square_float(self):
        gs = Square(4.5)
        self.assertEqual(gs.calculate_field(), 20.25)

    def test_square_string(self):
        gs = Square("4.5")
        self.assertEqual(gs.calculate_field(), 20.25)

    def test_square_string(self):
        gs = Square("lalaalal")
        self.fail('Oops! That was no valid number.')

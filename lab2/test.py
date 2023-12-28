import unittest

from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle


green = "зелёного"
red = "красного"
yellow = "жёлтого"


class TestFigures(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle(12, 13, red)
        self.b = Circle(13, yellow)
        self.c = Square(13, green)

    def test_area(self):
        from math import pi
        self.assertEqual(self.a.area(), 156)
        self.assertEqual(self.b.area(), pi * 13 * 13)
        self.assertEqual(self.c.area(), 169)

    def test_color(self):
        self.assertEqual(self.a.r_color._color, red)
        self.assertEqual(self.b.c_color._color, yellow)
        self.assertEqual(self.c.r_color._color, green)

    def test_repr(self):
        self.assertEqual(str(self.a), 'Прямоугольник красного цвета, длина 13, ширина 12, площадь 156.')
        self.assertEqual(str(self.b), 'Круг жёлтого цвета, радиус 13, площадь 530.929158456675.')
        self.assertEqual(str(self.c), 'Квадрат зелёного цвета, длина 13, площадь 169.')


def main():
    print(Rectangle(12, 13, red))
    print(Circle(13, yellow))
    print(Square(13, green))


if __name__ == "__main__":
    main()

from lab_python_oop.rectangle import Rectangle
class Square(Rectangle):
    type = "Квадрат"
    def __init__(self, side, color):
        self.side = side
        super().__init__(self.side, self.side, color)

    def __repr__(self):
        return '{} {} цвета, длина {}, площадь {}.'.format(
            self.type,
            self.r_color._color,
            self.side,
            self.area()
        )
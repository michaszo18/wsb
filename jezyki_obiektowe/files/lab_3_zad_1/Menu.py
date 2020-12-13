from datetime import datetime

from lab_3_zad_1.Figures import Square, Rectangle, Circle, Triangle, Trapeze
from classes.FileManipulation import FileManipulation


class Menu:

    def __init__(self):
        super(Menu, self).__init__()
        self.__fileManipulation = FileManipulation('log.txt')
        self.select = None

    def show(self):
        print("""
        Wybierz opcję: 
        1. Kwadart
        2. Prostokąt
        3. Koło
        4. Trójkąt
        5. Trapez
        0. Koniec
        """)
        # self.get_select()

    def get_select(self):
        self.select = input("Jakie pole chcesz policzyć? ")
        self.get_result()

    def get_result(self):
        if self.select == '1':
            a = input("Podaj długość a: ")
            geometric_shape = Square(a)
        elif self.select == '2':
            a = float(input("Podaj długość a: "))
            b = float(input("Podaj długość b: "))
            geometric_shape = Rectangle(a, b)
        elif self.select == '3':
            r = float(input("Podaj długość r: "))
            geometric_shape = Circle(r)
        elif self.select == '4':
            a = float(input("Podaj długość a: "))
            h = float(input("Podaj długość h: "))
            geometric_shape = Triangle(a, h)
        elif self.select == '5':
            a = float(input("Podaj długość a: "))
            b = float(input("Podaj długość b: "))
            h = float(input("Podaj długość h: "))
            geometric_shape = Trapeze(a, b, h)
        else:
            exit()
        result = geometric_shape.calculate_field()
        print(result)
        self.save_log(result, geometric_shape)


    def save_log(self, result, geometric_shape):
        date_now = datetime.now()
        message = f"{date_now} - Select {self.select} - Result {result} - Obj {geometric_shape}\n"
        self.__fileManipulation.add_line(message)


import math
from MethodCoord_classes import Line, Plane

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js


def main():
    put_text("Это программа для рассчёта угла методом координат. Укажите между какими геометрическими объектами будем искать\n"
             "№1: между прямой и другой прямой\n"
             "№2: между прямой и плоскостью\n"
             "№3: между плоскостью и  другой плоскостью")
    print("Это программа для рассчёта угла методом координат. Укажите между какими геометрическими объектами будем искать")
    print("№1: между прямой и другой прямой")
    print("№2: между прямой и плоскостью")
    print("№3: между плоскостью и  другой плоскостью")

    variant = input('введите номер №:')


    if variant == '1':  # №1: между прямой и другой прямой
        dots1 = [int(input(f"Введите координату {i} для первой прямой: ")) for i in ('x1', 'y1', 'z1', 'x2', 'y2', 'z2')]
        dots2 = [int(input(f"Введите координату {i} для второй прямой: ")) for i in ('x1', 'y1', 'z1', 'x2', 'y2', 'z2')]
        l1 = Line(*dots1)
        l2 = Line(*dots2)
        print(f'нормаль первой прямой {l1.get_norm()}')
        print(f'нормаль второй прямой  {l2.get_norm()}')
        numerator = abs(l1.get_norm()[0] * l2.get_norm()[0] + l1.get_norm()[1] * l2.get_norm()[1] + l1.get_norm()[2] * l2.get_norm()[2])
        denominator1 = math.sqrt(l1.get_norm()[0]**2 + l1.get_norm()[1]**2 + l1.get_norm()[2]**2)
        denominator2 = math.sqrt(l2.get_norm()[0]**2 + l2.get_norm()[1]**2 + l2.get_norm()[2]**2)
        print('cos =',math.cos(numerator/(denominator1*denominator2)))

    elif variant == '2':  # №2: между прямой и плоскостью
        dots1 = [int(input(f"Введите координату {i} для прямой: ")) for i in ('x1', 'y1', 'z1', 'x2', 'y2', 'z2')]
        dots2 = [int(input(f"Введите координату {i} для плоскости: ")) for i in ('x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3')]
        l1 = Line(*dots1)
        p1 = Plane(*dots2)
        print(f'нормаль прямой {l1.get_norm()}')
        print(f'нормаль плоскости {p1.get_norm()}')
        numerator = abs(l1.get_norm()[0] * p1.get_norm()[0] + l1.get_norm()[1] * p1.get_norm()[1] + l1.get_norm()[2] * p1.get_norm()[2])
        denominator1 = math.sqrt(l1.get_norm()[0]**2 + l1.get_norm()[1]**2 + l1.get_norm()[2]**2)
        denominator2 = math.sqrt(p1.get_norm()[0]**2 + p1.get_norm()[1]**2 + p1.get_norm()[2]**2)
        print('sin =',math.sin(numerator/(denominator1*denominator2)))

    elif variant == '3':  #№3: между плоскостью и  другой плоскостью
        dots2 = [int(input(f"Введите координату {i} для первой плоскости: ")) for i in ('x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3')]
        dots2 = [int(input(f"Введите координату {i} для второй плоскости: ")) for i in ('x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3')]
        p1 = Plane(*dots1)
        p2 = Plane(*dots2)
        print(f'нормаль первой плоскости {p1.get_norm()}')
        print(f'нормаль второй плоскости {p2.get_norm()}')
        numerator = abs(p1.get_norm()[0] * p2.get_norm()[0] + p1.get_norm()[1] * p2.get_norm()[1] + p1.get_norm()[2] * p2.get_norm()[2])
        denominator1 = math.sqrt(p1.get_norm()[0]**2 + p1.get_norm()[1]**2 + p1.get_norm()[2]**2)
        denominator2 = math.sqrt(p2.get_norm()[0]**2 + p2.get_norm()[1]**2 + p2.get_norm()[2]**2)
        print('sin =',math.sin(numerator/(denominator1*denominator2)))
    else:
        print("недопустимое значение")


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)

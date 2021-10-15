# Quadratic Equation
from math import sqrt


def discriminant(a, b, c):
    return b * b - 4 * a * c


def solutions(a, b, c):
    if a != 0:
        if discriminant(a, b, c) < 0:
            return 'No Solutions'
        elif discriminant(a, b, c) == 0:
            x = -b / (2 * a)
            return f'One solution: {x}'
        else:
            x1 = (-b + sqrt(discriminant(a, b, c))) / (2 * a)
            x2 = (-b - sqrt(discriminant(a, b, c))) / (2 * a)
            return f'Two solutions: {x1} {x2}'
    elif c == 0:
        if b == 0:
            return 'Infinite solutions'
        else:
            return f'One solution: {0}'
    elif b == 0:
        return 'No Solutions'
    else:
        x = -c / b
        return f'One solution: {x}'


a = float(input())
b = float(input())
c = float(input())
if a != 0:
    print('Quadratic equation')
    print(f'Discriminant: {discriminant(a, b, c)}')
    print(solutions(a, b, c))
else:
    print('Non-quadratic equation')
    print(solutions(a, b, c))

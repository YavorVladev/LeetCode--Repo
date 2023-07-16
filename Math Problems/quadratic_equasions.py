import sys
import math


def quadratic_solver(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f"{x1}|{x2}"
    elif d == 0:
        x1 = -b / (2 * a)
        return f"{x1}"

    return "no roots"


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Incorrect input')
    else:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])

            if a == 0:
                print('Special Case')
            else:
                result = quadratic_solver(a, b, c)
                print(result)
        except ValueError:
            print('Please enter only numbers as coefficients.')

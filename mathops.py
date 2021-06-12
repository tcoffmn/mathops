import math
import numbers
import sys

def print_sin():
    a = -90

    while a <= 90:
        print(a, '=', math.sin(a))
        a=a+1

if __name__ == '__main__':

    print_sin()

    sys.exit(0)

from TikZCodeGen import *

def fdx(x, y):
    return 3 * x


def fdy(x, y):
    return 4 * y

def der(x, y):
    return -3 * x / (4 * y)

# generating TikZ code for the direction field to be drawn in the integral points of the square [-2, 2]^2

diff_eq_field(x1=-2, x2=3, y1=-2, y2=3, move_x=1, move_y=1, f=der, length=0.5, filename='equation_field.txt', show_undefined_points=True)
print()
diff_one_form_field(x1=-2, x2=3, y1=-2, y2=3, move_x=1, move_y=1, f=fdx, g=fdy, length=0.5, filename='one-form_field.txt', show_undefined_points=True)
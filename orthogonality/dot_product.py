import math
import fractions


# simple dot product
def dot(x, y):
    multiple = 0
    for i in range(len(x)):
        multiple = multiple + x[i] * y[i]
    print("dot product of x and y is:", multiple)


# length of x and y
def length(x, y):
    # length of x
    sum_x = 0
    for i in range(len(x)):
        sum_x = sum_x + x[i] * x[i]

    print("Length of x is:", math.sqrt(sum_x))

    # length of y
    sum_y = 0
    for i in range(len(y)):
        sum_y = sum_y + y[i] * y[i]

    print("Length of y is:", math.sqrt(sum_y))


# distance between x and y
def distance(x, y):
    square = 0
    result = [None] * len(x)

    for i in range(len(x)):
        # minus x and y
        result[i] = x[i] - y[i]
        # pow resault
        square = square + result[i] ** 2
    # computing square of result
    print("Distance between x and y is:", math.sqrt(square))


# angle between x and y
def angle(x, y):
    # dot product
    multiple = 0
    for i in range(len(x)):
        multiple = multiple + x[i] * y[i]
    print('multiple for angle is:', multiple)

    # length of x
    sum_x = 0
    for i in range(len(x)):
        sum_x = sum_x + x[i] * x[i]
    sum_x = math.sqrt(sum_x)

    print('length x  for angle is:', sum_x)

    # length of y
    sum_y = 0
    for i in range(len(y)):
        sum_y = sum_y + y[i] * y[i]
    sum_y = math.sqrt(sum_y)
    print('length y for angle is:', sum_y)

    # multiple of length x and y
    mul_len = sum_x * sum_y
    print('multiple of length x and y is :', mul_len)

    # angle of x and y
    frac = fractions.Fraction(multiple, int(mul_len))
    print("fraction is:", frac)
    ang = math.cos(frac)

    print("Angle of x and y is:", ang)


# main
if __name__ == '__main__':
    x = [1, 2]
    y = [2, 1]
    dot(x, y)
    length(x, y)
    distance(x, y)
    angle(x, y)

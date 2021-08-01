import math
import fractions


# computing x**T Ay
def lengthOfVector(x):
    result = 0
    sum = (x[0] ** 2) - (x[0] * x[1]) + (x[1] ** 2)
    result = math.sqrt(sum)
    print("result is:", result)


def orthonomial(x, y):
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
    if frac == 0 :
        print("Two vectores are orthogonal")
    else:
        print("Two vectores are not orthogonal")
    ang = math.cos(frac)

    print("Angle of x and y is:", ang)


if __name__ == '__main__':
    x = [1, 1]
    y = [-1, 1]
    lengthOfVector(x)
    orthonomial(x, y)

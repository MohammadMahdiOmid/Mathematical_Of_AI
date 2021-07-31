import math
# simple dot product
def dot(x, y):
    multiple = 0
    for i in range(len(x)):
        multiple = multiple + x[i] * y[i]
    print("dot product of x and y is:", multiple)


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


# main
if __name__ == '__main__':
    x = [1, 2, 3]
    y = [2, 3, 4]
    dot(x, y)
    length(x, y)

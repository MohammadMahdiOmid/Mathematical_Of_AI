import math

# computing x**T Ay
def lengthOfVector(x):
    result = 0
    sum = (x[0] ** 2) - (x[0] * x[1]) + (x[1] ** 2)
    result = math.sqrt(sum)
    print("result is:", result)


if __name__ == '__main__':
    x = [-2, 2]
    lengthOfVector(x)

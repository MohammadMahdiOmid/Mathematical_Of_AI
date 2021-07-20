import statistics
import numpy as np


def computing_mean(dataset):
    sum = 0

    # computing sum of dataset members
    for i in range(len(dataset) + 1):
        sum = sum + int(i)

    print("sum is:", sum)

    # computing mean of dataset
    mean = sum / len(dataset)
    print("manually mean of this data set is :", mean)

    # automatically computing mean
    print("automatically computing mean is:", statistics.mean(dataset))

    # Computing variance needs to have mean of dataset
    computing_variace(dataset)


def computing_variace(dataset):
    mean = statistics.mean(dataset)
    inverse_square = 0

    # To computing inverse square
    for i in range(len(dataset)):
        inverse_square = inverse_square + pow(dataset[i] - mean, 2)
    print("inverse_square is:", inverse_square)

    # computing Variance of dataset
    variance = inverse_square / (len(dataset) - 1)
    print("Manually Variance is:", variance)

    # Automatically compute variance
    print("Automatically Variance is", statistics.variance(dataset))

    computing_covariace()


def computing_covariace():
    sum_x = 0
    sum_y = 0

    x = [4, 2, 5]
    y = [4, 4, 7]

    #Finding the mean of the series x and y
    x_mean = sum(x)/float(len(x))
    y_mean = sum(y)/float(len(y))

    #Subtracting mean from the individual elements
    sub_x=[i - x_mean for i in x]
    sub_y=[i - y_mean for i in y]

    #computing multiple of subs
    mul=sum([sub_x[i]*sub_y[i] for i in range(len(x))])

    #computing manually covariance
    covariance=mul/(len(x)-1)

    print(" manually covariance is:",covariance)


    auto_cova=np.cov(x,y)
    print("Automatically covariance with matrix is:",auto_cova)


# mutlt_sums = sum_x * sum_y
# cov = mutlt_sums / len(x)
# print("covariance is:", cov)
# print(np.cov(x, y))
#
# # Finding the mean of the series x and y
# mean_x = sum(x) / float(len(x))
# mean_y = sum(y) / float(len(y))
# # Subtracting mean from the individual elements
# sub_x = [i - mean_x for i in x]
# sub_y = [i - mean_y for i in y]
# numerator = sum([sub_x[i] * sub_y[i] for i in range(len(sub_x))])
# denominator = len(x) - 1
# cov = numerator / denominator
# print(cov)

if __name__ == '__main__':

    number_of_dataset = int(input("Please Enter your count of dataset:"))

    dataset = []
    for x in range(number_of_dataset):
        dataset.append(int(input("Entire your value:")))

    print("Dataset is:", dataset)
    computing_mean(dataset)

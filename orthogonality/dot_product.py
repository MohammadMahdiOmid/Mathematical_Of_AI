
#simple dot product
def dot(x, y):
    multiple = 0
    for i in range(len(x)):
        multiple = multiple + x[i] * y[i]
    print(multiple)

#main
if __name__ == '__main__':
    x=[1,2]
    y=[1,2]
    dot(x,y)
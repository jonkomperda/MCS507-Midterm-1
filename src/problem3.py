import numpy
from math import sin,cos,pi

def ranSymMatrix(n):
    """Creates a symmetric random matrix """
    arr = numpy.random.random_integers(0,1,size=(n,n))
    for x in range(len(arr)):
        arr[x,x] = 0
    #return arr + arr.T - numpy.diag(arr.diagonal())
    return (arr + arr.T)//2

def genVertList(n):
    """docstring for genVerList"""
    return [(cos(2*k*pi/n),sin(2*k*pi/n)) for k in range(n)]

if __name__ == '__main__':
    from matplotlib import pyplot as plt
    a = ranSymMatrix(10)
    v= genVertList(10)
    print v
    print a
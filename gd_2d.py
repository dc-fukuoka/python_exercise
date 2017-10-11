#!/usr/bin/env python3

# gradient descent

import math
import sys
import numpy as np


def gauss(x, offset):
    return -1.0*math.exp(-1.0*((x[0]-offset[0])**2+(x[1]-offset[1])**2))

def grad_gauss(x, offset):
    grad = np.empty(2, dtype=np.float64)
    for i in range(2):
        grad[i] = -2.0*(x[i]-offset[i])*gauss(x, offset)
    return grad

def gradient_descent(grad_func, offset, x0, tol, iter_max, alpha):
    x    = x0
    xnew = np.zeros(2, dtype=np.float64)
    
    for iter in range(iter_max):
        xnew = x - alpha*grad_func(x, offset)
        diff = abs(xnew - x)

        if iter%10 == 0:
            print("iter:", iter, "x:", x, "diff:", diff)
        
        if (diff < tol).all():
            print("converged, iter:", iter)
            break

        
        if iter == iter_max-1:
            print("gradient descent did not converge.")
            sys.exit(-1)

        x = xnew

    return x

def main():
    offset   = np.array([0.25, 0.50], dtype=np.float64)
    x0       = np.array([1.0,  2.0],  dtype=np.float64)
    tol      = 1.0e-40
    iter_max = 1000
    
    argv = sys.argv
    argc = len(argv)
    if argc == 1:
        alpha = 0.1
    else:
        alpha = float(argv[1])

    print("alpha:", alpha, "offset:", offset)
    res = gradient_descent(grad_gauss, offset, x0, tol, iter_max, alpha)

    print("minimum value at x = ", res)
        
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# gradient descent

import numpy as np
import math
import sys

def gauss(x, offset):
    return -1.0*math.exp(-1.0*((x-offset)**2))

def gauss_prime(x, offset):
    return -2.0*(x-offset)*gauss(x, offset)

def gradient_descent(func_prime, offset, x0, tol, iter_max, alpha):
    x    = x0
    xnew = 0.0
    
    for iter in range(iter_max):
        xnew = x - alpha*func_prime(x, offset)
        diff = abs(xnew - x)

        if iter%10 == 0:
            print("iter:", iter, "x:", x, "diff:", diff)
        
        if diff < tol:
            print("converged, iter:", iter)
            break

        
        if iter == iter_max-1 and diff >= tol:
            print("gradient descent did not converge.")
            sys.exit(-1)

        x = xnew

    return x

def main():
    offset   = 0.25
    x0       = 1.0
    tol      = 1.0e-40
    iter_max = 1000
    
    argv = sys.argv
    argc = len(argv)
    if argc == 1:
        alpha = 0.1
    else:
        alpha = float(argv[1])

    print("alpha:", alpha, "offset:", offset)
    res = gradient_descent(gauss_prime, offset, x0, tol, iter_max, alpha)

    print("minimum value:", res)
        
if __name__ == "__main__":
    main()

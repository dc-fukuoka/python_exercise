#!/usr/bin/env python3

import numpy as np
import time as t

# matrix product c = a*b

def dgemm(a, b, c):
    np.dot(a, b, out=c)

"""
# C like manner by for loop, too slow for python, though the result is correct
def dgemm(a, b, c):
    size = len(a[0][:])
    for i in range(size):
        for j in range(size):
            for k in range(size):
                c[i][j] += a[i][k]*b[k][j]
"""
 
def trace(c):
    return  np.trace(c)

def main():
    size = 128
    seed = 7777
    np.random.seed(seed)
    a = np.random.rand(size, size).astype(np.float64)
    b = np.random.rand(size, size).astype(np.float64)
    c = np.zeros((size, size), dtype=np.float64)

    print("dtype:", a.dtype)
    
    t0 = t.time()
    dgemm(a, b, c)
    time = t.time() - t0
    print("matrix size:", size, "x", size)
    print("dgemm time:", time, "trace:", trace(c))
    
if __name__ == "__main__":
    main()

python exercise - exercise of python, just for my study.
====
contents:
----
 * gd.py: gradient descent by python.
~~~
$ ./gd.py 0.4
alpha: 0.4 offset: 0.25
iter: 0 x: 1.0 diff: 0.3418696948385538
iter: 10 x: 0.2500003616058507 diff: 2.892846805435667e-07
iter: 20 x: 0.250000000000037 diff: 2.964295475749168e-14
converged, iter: 25
minimum value at x = 0.25
~~~
 * gd_2d.py: gradient descent with two dimensional function.
~~~
 $ ./gd_2d.py 0.4
alpha: 0.4 offset: [ 0.25  0.5 ]
iter: 0 x: [ 1.  2.] diff: [ 0.0360328  0.0720656]
iter: 10 x: [ 0.25172876  0.50345752] diff: [ 0.00138299  0.00276598]
iter: 20 x: [ 0.25  0.5 ] diff: [  1.41628875e-10   2.83257751e-10]
iter: 30 x: [ 0.25  0.5 ] diff: [ 0.  0.]
converged, iter: 30
minimum value at x = [ 0.25  0.5 ]
~~~
 
 * dgemm.py: matrix-matrix multiplication by python.
~~~
$ ./dgemm.py
dtype: float64
matrix size: 128 x 128
dgemm time: 0.0002474784851074219 trace: 4110.47098433
~~~
performance comparison between MKL blas dgemm() by fortran vs numpy dot(both uses 16 threads):  
matrix size: 8192x8192  
  
MKL dgemm(): 3.82s  
numpy dot  : 3.87s  

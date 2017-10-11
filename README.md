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
minimum value: 0.25
~~~
 * gd_2d.py gradient descent with two dimensional function. numpy is needed.
 ~~~
 $ ./gd_2d.py 0.4
alpha: 0.4 offset: [ 0.25  0.5 ]
iter: 0 x: [ 1.  2.] diff: [ 0.0360328  0.0720656]
iter: 10 x: [ 0.25172876  0.50345752] diff: [ 0.00138299  0.00276598]
iter: 20 x: [ 0.25  0.5 ] diff: [  1.41628875e-10   2.83257751e-10]
iter: 30 x: [ 0.25  0.5 ] diff: [ 0.  0.]
converged, iter: 30
minimum value: [ 0.25  0.5 ]
 ~~~

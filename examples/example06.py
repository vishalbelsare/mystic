#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2016 California Institute of Technology.
# Copyright (c) 2016-2025 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/mystic/blob/master/LICENSE
"""
Example:
    - Solve 8th-order Chebyshev polynomial coefficients with Powell's method.
    - Plot of fitting to Chebyshev polynomial.

Demonstrates:
    - standard models
    - minimal solver interface
"""

# Powell's Directonal solver
from mystic.solvers import fmin_powell

# Chebyshev polynomial and cost function
from mystic.models.poly import chebyshev8, chebyshev8cost
from mystic.models.poly import chebyshev8coeffs

# tools
from mystic.math import poly1d
from mystic.tools import getch
import matplotlib.pyplot as plt
plt.ion()

# draw the plot
def plot_exact():
    plt.title("fitting 8th-order Chebyshev polynomial coefficients")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    import numpy
    x = numpy.arange(-1.2, 1.2001, 0.01)
    exact = chebyshev8(x)
    plt.plot(x,exact,'b-')
    plt.legend(["Exact"])
    plt.axis([-1.4,1.4,-2,8])#,'k-')
    plt.draw()
    plt.pause(0.001)
    return
 
# plot the polynomial
def plot_solution(params,style='y-'):
    import numpy
    x = numpy.arange(-1.2, 1.2001, 0.01)
    f = poly1d(params)
    y = f(x)
    plt.plot(x,y,style)
    plt.legend(["Exact","Fitted"])
    plt.axis([-1.4,1.4,-2,8])#,'k-')
    plt.draw()
    plt.pause(0.001)
    return


if __name__ == '__main__':

    print("Powell's Method")
    print("===============")

    # initial guess
    import random
    from mystic.tools import random_seed
    random_seed(123)
    ndim = 9
    x0 = [random.uniform(-100,100) for i in range(ndim)]

    # draw frame and exact coefficients
    plot_exact()

    # use Powell's method to solve 8th-order Chebyshev coefficients
    solution = fmin_powell(chebyshev8cost,x0)

    # use pretty print for polynomials
    print(poly1d(solution))

    # compare solution with actual 8th-order Chebyshev coefficients
    print("\nActual Coefficients:\n %s\n" % poly1d(chebyshev8coeffs))

    # plot solution versus exact coefficients
    plot_solution(solution)
    getch() #XXX: or plt.show() ?

# end of file

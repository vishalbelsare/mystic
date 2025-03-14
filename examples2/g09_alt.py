#!/usr/bin/env python
#
# Problem definition:
# A-R Hedar and M Fukushima, "Derivative-Free Filter Simulated Annealing
# Method for Constrained Continuous Global Optimization", Journal of
# Global Optimization, 35(4), 521-549 (2006).
# 
# Original Matlab code written by A. Hedar (Nov. 23, 2005)
# http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/go.htm
# and ported to Python by Mike McKerns (December 2014)
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2016 California Institute of Technology.
# Copyright (c) 2016-2025 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/mystic/blob/master/LICENSE

from g09 import objective, bounds, xs, ys

from mystic.constraints import as_constraint
from mystic.penalty import quadratic_inequality

def penalty1(x): # <= 0.0
    return 2*x[0]**2 + 3*x[1]**4 + x[2] + 4*x[3]**2 + 5*x[4] - 127.0

def penalty2(x): # <= 0.0
    return 7*x[0] + 3*x[1] + 10*x[2]**2 + x[3] - x[4] - 282.0

def penalty3(x): # <= 0.0
    return 23*x[0] + x[1]**2 + 6*x[5]**2 - 8*x[6] - 196.0

def penalty4(x): # <= 0.0
    return 4*x[0]**2 + x[1]**2 - 3*x[0]*x[1] + 2*x[2]**2 + 5*x[5] - 11*x[6]

@quadratic_inequality(penalty1, k=1e12)
@quadratic_inequality(penalty2, k=1e12)
@quadratic_inequality(penalty3, k=1e12)
@quadratic_inequality(penalty4, k=1e12)
def penalty(x):
    return 0.0

solver = as_constraint(penalty)



if __name__ == '__main__':

    from mystic.solvers import diffev2
    from mystic.math import almostEqual

    result = diffev2(objective, x0=bounds, bounds=bounds, penalty=penalty, npop=40, gtol=200, disp=False, full_output=True)

    assert almostEqual(result[0], xs, rel=1e-2)
    assert almostEqual(result[1], ys, rel=1e-2)



# EOF

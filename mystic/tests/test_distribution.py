#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2023-2025 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/mystic/blob/master/LICENSE

from mystic.math import Distribution, almostEqual

N = 100000
a = Distribution('normal', 0, 1)
b = Distribution('normal', 5, 3)
c = Distribution('normal', 6, 6)

apb = a+b
a2pb2 = a/2+b/2
apb2= (a+b)/2
anb = Distribution(a,b)
bnc = Distribution(b,c)
bpc2 = (b+c)/2
amb = a*b
a0nb = Distribution(a,b,p=(0,1))
a4nb6 = Distribution(a,b,p=(.4,.6))
anc = Distribution(a,c,p=(.5,.5))

assert almostEqual(a2pb2(N).mean(), apb2(N).mean(), tol=.1)
assert almostEqual(anb(N).mean(), .5*apb(N).mean(), tol=.1)
assert almostEqual(anb(N).mean(), amb(N).mean(), tol=.1)
assert almostEqual((a(N).mean() + b(N).mean())/2, apb2(N).mean(), tol=.1)
assert almostEqual((b(N).mean() + c(N).mean())/2, bpc2(N).mean(), tol=.1)
assert almostEqual((a+b+c)(N).mean(), (c+b+a)(N).mean(), tol=.1)
assert almostEqual(a0nb(N).mean(), b(N).mean(), tol=.1)
assert almostEqual(a4nb6(N).mean(), anc(N).mean(), tol=.1)

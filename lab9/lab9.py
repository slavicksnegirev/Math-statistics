import math
import sympy as sp
import sympy.plotting as plt
from sympy.abc import p, w, i

A = sp.Matrix([[0, 1],
               [-4, -5]])
B = sp.Matrix([[1],
               [1]])
C = sp.Matrix([[1, 0]])

I = sp.eye(A.shape[0])
r = sp.Matrix.eigenvals(A)

Mp = p*I-A

Np = sp.simplify(Mp.inv())
Wp = sp.simplify(C*Np*B)

W1 = Wp.subs(p, i * w)
W2 = Wp.subs(p, -i * w)

Su = 1

Sy = sp.simplify(sp.expand(W1*Su*W2).subs(i**2,-1))
Sy.doit()
print(Sy)

Dy = 2 * sp.integrate(Sy, (w, 0, math.inf))
print(Dy)
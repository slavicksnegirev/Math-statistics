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
print(r)
Mp = p*I-A
print(Mp)

Np = sp.simplify(Mp.inv())
print(Np)
Wp = sp.simplify(C*Np*B)
print(Wp)

W1 = Wp.subs(p, i * w)
print(W1)
W2 = Wp.subs(p, -i * w)
print(W2)

Su = 1

Sy = sp.simplify(sp.expand(W1*Su*W2).subs(i**2,-1))
Sy.doit()
print(Sy)

Dy = sp.integrate(Sy, (w, -math.inf, math.inf))
print(Dy)
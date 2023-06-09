"""
Найти спектральную плотность установившегося выходного сигнала линейной стационарной непрерывной системы с
уравнениями движения x′ = Ax + Bu, y = Cx и построить график спектральной плотности первой компоненты этого сигнала.
На вход системы подается стационарный случайный процесс со спектральной плотностью S(ω)=(σ^2)2λ/(2π(ω^2 + λ^2))
"""

import math
import sympy as sp
import sympy.plotting as plt
from sympy.abc import p, w, i

LAMBDA = 1
Ds = 6 * math.pi
Sw = sp.simplify((Ds / (2 * math.pi)) * ((2 * LAMBDA) / (w**2 + LAMBDA**2)))
A = sp.Matrix([[-1, 2, -4],
               [-2, 0, -1],
               [4, -1, -6]])
B = sp.Matrix([[1], [1], [1]])
C = sp.Matrix([[1, 0, 0],
               [0, 2, 1]])
D = sp.Matrix([[0],
               [0]])
print(Sw)

r = sp.Matrix.eigenvals(A)
print(r)

H = sp.eye(A.shape[0])
print(H)
Hp = p*H - A
print(Hp)
H1p = Hp.inv()
print(H1p)
Wp = sp.simplify(C * H1p * B - D)
print(Wp)

W1 = Wp.subs(p, i * w)
print(W1)
W2 = Wp.subs(p, -i * w)
print(W2)

Spectr = W1 * W2.T
print(f"Spectr = {Spectr}")

Sy_w = sp.simplify(Sw * Spectr)
print(f"Sy_w = {Sy_w}")

Sy1_w = sp.expand(Sy_w[0]).subs(i**2,-1)
print(f"Sy1_w = {Sy1_w}")
Sy1_w.doit()

p1 = plt.plot(Sw, legend=True, show=False)
p2 = plt.plot(Sy1_w, legend=True, show=False)

p1.extend(p2)

print(p1)
p1.show()
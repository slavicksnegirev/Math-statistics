"""
Решить одну задачу однофакторного дисперсионного анализа.
- Везде уровень значимости принять равным 0.05.
- В каждой задаче проверить гипотезу Но о равенстве средних. Если гипотеза Но принимается, то найти несмещенные
оценки среднего и дисперсии. Если же Но отклоняется, провести попарное сравнение средних, используя метод линейных
контрастов.

Вариант №3
В следующей таблице приведены результаты обследования 60 работников производства, у которых фиксировалась средняя
часовая выработка в натуральных единицах продукции. Принять за фактор - возраст работника.
"""
import math

import numpy as np
from scipy import stats as st
from scipy.stats import f_oneway

X1 = np.array([19, 20, 20, 20, 22, 30, 31, 32, 32, 34, 35, 35, 39, 40, 41, 40, 40, 41, 41, 42])
X2 = np.array([19, 20, 20, 23, 25, 20, 29, 30, 31, 31, 36, 40, 41, 42, 45, 28, 31, 35, 36, 40])
X3 = np.array([18, 19, 20, 21, 23, 19, 25, 25, 26, 26, 24, 24, 24, 25, 25, 20, 24, 25, 31, 32])

# X1 = np.array([5, 3, 3, 4, 2, 2, 2, 3, 2, 0, 4, 1])
# X2 = np.array([3, 3, 1, 5, 2, 0, 0, 0, 0, 1, 2, 2])
# X3 = np.array([15, 11, 18, 21, 6, 17, 10, 8, 13, 4, 11, 17])

X = np.concatenate((X1, X2, X3), axis=0)

k = 3
N = len(X1)
nn = k * N
alpha = 0.05

mX1 = X1.mean()
mX2 = X2.mean()
mX3 = X3.mean()
mmX = X.mean()

mX = np.array([mX1, mX2, mX3])

# Проверка основной гипотезы Но о равенстве групповых средних с помощью однофакторного дисперсионного анализа
Q1 = N * ((mX1)**2 + (mX2)**2 + (mX3)**2)-nn*(mmX**2)
Q2 = sum((X1) ** 2) + sum((X2 ) ** 2) + sum((X3 ) ** 2)-N * ((mX1)**2 + (mX2)**2 + (mX3)**2)
print(f"Q1 = {Q1}, Q2 = {Q2}")
Q_my = Q1+Q2
Q_def = sum((X1-mmX)**2)+sum((X2-mmX)**2)+sum((X3-mmX)**2)
print(f"Q = {Q_my}, Q1+Q2 = {Q1+Q2}")
# Статистика критерия
F = (nn - k)*Q1/((k-1) * Q2)
print(f"Статистика критерия F = {F}")

# Квантили распределения Фишера на уровне значимости а = 0.05
print(f"Квантили распределения Фишера на уровне значимости а = 0.05: ({st.f.ppf(alpha/2, k-1, nn-k)};"
       f" {st.f.ppf(1-alpha/2, k-1, nn-k)})")

# Поскольку статистика критерия F не входит в интервал принятия гипотезы (a/2; 1-a/2), то гипотезу Ho отвергаем.
# Попарное сравнение средних с использованием метода линейных контрастов
L1 = mX1 - mX2
D1 = Q2/(nn-k) * (1/N + 1/N)
L1_left = L1 - math.sqrt(D1)*math.sqrt(st.f.ppf(1-alpha, k-1, nn-k))
L1_right = L1 + math.sqrt(D1)*math.sqrt(st.f.ppf(1-alpha, k-1, nn-k))
print(f"L1 = {L1}, D1 = {D1}, L1_left = {L1_left}, L1_right = {L1_right}")

L2 = mX3 - mX2
D2 = Q2/(nn-k) * (1/N + 1/N)
L2_left = L2 - math.sqrt(D2)*math.sqrt(st.f.ppf(1-alpha, k-1, nn-k))
L2_right = L2 + math.sqrt(D2)*math.sqrt(st.f.ppf(1-alpha, k-1, nn-k))
print(f"L2 = {L2}, D2 = {D2}, L2_left = {L2_left}, L2_right = {L2_right}")

L3 = mX1 - mX3
D3 = Q2/(nn-k) * (1/N + 1/N)
L3_left = L3 - math.sqrt(D3)*math.sqrt(st.f.ppf(1-alpha, k-1, nn-k))
L3_right = L3 + math.sqrt(D3)*math.sqrt(st.f.ppf(1-alpha, k-1, nn-k))
print(f"L3 = {L3}, D3 = {D3}, L3_left = {L3_left}, L3_right = {L3_right}")

# Ранговый критерий Краскела
Z = sorted(X)
# Находим ранги каждого элемента в общем вариационном ряду:
R = st.rankdata(X)
print(f"Z = {Z}\nX = {X}\nR = {R}")

# Составляем статистику Критерия Краскела (H-критерий):
sumR = sum(R)
sumRY1 = sum(R[0:N])
sumRY2 = sum(R[N:N+N])
sumRY3 = sum(R[N+N:nn])
print(f"sumR = {sumR}, sumRY1 = {sumRY1}, sumRY2 = {sumRY2}, sumRY3 = {sumRY3}")

H = 12/(nn*(nn+1)) * (math.pow(sumRY1, 2)/N + math.pow(sumRY2, 2)/N + math.pow(sumRY3, 2)/N) - 3*(nn+1)
print(f"H = {H}")

# Есть совпадающие наблюдения, поэтому следует модифицировать статистику H
RR = st.rankdata(Z)
print(f"RR = {RR}")

# Совподающие наблюдения
T = sorted({x for x in RR if list(RR).count(x) > 1})
print(f"T = {T}")
for i in range(len(T)):
    count = 0
    for j in range(len(RR)):
        if RR[j] == T[i]:
            count += 1
    T[i] = math.pow(count, 3) - count
print(f"T = {T}")

# Статистика критерия с поправкой:
H1 = H/(1-sum(T)/(math.pow(nn,3)-nn))
print(f"H1 = {H1}")

# Квантиль распределения хи-квадрат на уровне значимости α = 0.05:
qchi2 = st.chi2.ppf(1-alpha, k-1)
print(f"qchi2 = {qchi2}")
# Поскольку статистика критерия 23.982 не входит в интервал принятия гипотезы (0; 5.991), то гипотезу Ho снова
# отвергаем.




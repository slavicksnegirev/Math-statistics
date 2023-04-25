import math
import statistics

import numpy as np
from scipy import stats

MX1 = 4
alpha = 0.1
MX2 = 5.5
DX1 = 4
DX2 = 7
size1 = 50
size2 = 100
STD1 = math.sqrt(DX1)
STD2 = math.sqrt(DX2)
firstSelection = np.random.normal(MX1, STD1, size=size1)
secondSelection = np.random.normal(MX2, STD2, size=size2)
print(firstSelection)
print(secondSelection)


# проверка первой гипотезы
print("\n\n1. Гипотеза о числовом значении параметра a(мат. ожидания) при известном параметре сигма^2")
firstMean = np.mean(firstSelection)
a = MX1
U = np.round((firstMean - a) / math.sqrt(DX1 / size1), 3)
xright = np.round(stats.norm.ppf(1 - alpha / 2, 0, 1), 3)
xleft = -xright
if (xleft < U < xright):
    print("1.1 Двусторонний критерий: Гипотеза принимается, т.к. выполняется неравенство: ", xleft, "<", U, "<", xright)
else:
    print("1.1 Двусторонний критерий: Гипотеза отклоняется, т.к. не выполняется неравенство: ", xleft, "<", U, "<",
          xright)
# Правостронний критерий
xright1 = np.round(stats.norm.ppf(1 - alpha, 0, 1), 3)
if (U < xright1):
    print("1.2 Правосторонний критерий (a>a0): Гипотеза принимается, т.к. выполняется неравенство: ", U, "<", xright1)
else:
    print("1.2 Правосторонний критерий (a>a0): Гипотеза отклоняется, т.к. не выполняется неравенство: ", U, "<",
          xright1)
# Левосторонний критерий
xleft1 = -np.round(stats.norm.ppf(1 - alpha, 0, 1), 3)
if (U > xleft1):
    print("1.3 Левосторонний критерий (a<a0): Гипотеза принимается, т.к. выполняется неравенство: ", U, ">", xleft1)
else:
    print("1.2 Правосторонний критерий (a<a0): Гипотеза отклоняется, т.к. не выполняется неравенство: ", U, ">",
          xleft1)


# проверка второй гипотезы
print("\n\n2. Гипотеза о числовом значении параметра a(мат. ожидания) при неизвестном параметре сигма^2")
Sx = statistics.stdev(firstSelection)  # выборочное ско
T = np.round((firstMean - a) / math.sqrt(Sx / size1), 3)
xright = np.round(stats.t.ppf(1 - alpha / 2, size1 - 1), 3)
xleft = -xright
if (xleft < T < xright):
    print("2.1 Двусторонний критерий: Гипотеза принимается, т.к. выполняется неравенство: ", xleft, "<", T, "<", xright)
else:
    print("2.1 Двусторонний критерий: Гипотеза отклоняется, т.к. не выполняется неравенство: ", xleft, "<", T, "<",
          xright)
# Правостронний критерий
xright2 = np.round(stats.t.ppf(1 - alpha, size1 - 1), 3)
if (T < xright2):
    print("2.2 Правосторонний критерий (a > a0): Гипотеза принимается, т.к. выполняется неравенство: ", T, "<", xright2)
else:
    print("2.2 Правосторонний критерий (a > a0): Гипотеза отклоняется, т.к. не выполняется неравенство: ", T, "<",
          xright2)
# Левосторонний критерий
xleft2 = -np.round(stats.t.ppf(1 - alpha, size1 - 1), 3)
if (T > xleft2):
    print("2.3 Левосторонний критерий (a < a0): Гипотеза принимается, т.к. выполняется неравенство: ", T, ">", xleft2)
else:
    print("2.3 Левосторонний критерий (a < a0): Гипотеза отклоняется, т.к. не выполняется неравенство: ", T, ">",
          xleft2)



# проверка 3-й гипотезы
print("\n\n3. Гипотеза о числовом значении сигма^2(дисперсии) при неизвестном параметре a")
X = np.round((Sx ** (2)* (size1 - 1)) / (DX1), 3)
xright = np.round(stats.chi2.ppf(1 - alpha / 2, size1 - 1), 3)
xleft = np.round(stats.chi2.ppf(alpha / 2, size1 - 1), 3)
if xleft < X < xright:
    print("3.1 Двусторонний критерий: Гипотеза принимается, т.к. выполняется неравенство: ", xleft, "<", X, "<", xright)
else:
    print("3.1 Двусторонний критерий: Гипотеза отклоняется, т.к. не выполняется неравенство: ", xleft, "<", X, "<",
          xright)
# Правостронний критерий
xright3 = np.round(stats.chi2.ppf(1 - alpha, size1 - 1), 3)
if (X < xright3):
    print("3.2 Правосторонний критерий (сигма^2 > сигма0^2): Гипотеза принимается, т.к. выполняется неравенство: ", X, "<", xright3)
else:
    print("3.2 Правосторонний критерий (сигма^2 > сигма0^2): Гипотеза отклоняется, т.к. не выполняется неравенство: ",
          X, "<", xright3)
# Левосторонний критерий
xleft3 = np.round(stats.chi2.ppf(alpha, size1 - 1), 3)
if (X > xleft3):
    print("3.3 Левосторонний критерий (сигма^2 < сигма0^2) : Гипотеза принимается, т.к. выполняется неравенство: ", X, ">", xleft3)
else:
    print("3.3 Левосторонний критерий (сигма^2 < сигма0^2) : Гипотеза отклоняется, т.к. не выполняется неравенство: ",
          X, ">", xleft3)

# проверка 4-й гипотезы
print("\n\n4. Гипотеза о равенстве мат. ожиданий 2-x выборок, если обе дисперсии известны")
secondMean = np.mean(secondSelection)
U = np.round((firstMean - secondMean) / math.sqrt((DX1 / size1) + (DX2 / size2)), 3)
xright = np.round(stats.norm.ppf(1 - alpha / 2, 0,1), 3)
xleft = -xright
if (xleft < U < xright):
    print("4.1 Двусторонний критерий: Гипотеза принимается, т.к. выполняется неравенство: ", xleft, "<", U, "<", xright)
else:
    print("4.1 Двусторонний критерий: Гипотеза отклоняется, т.к. не выполняется неравенство: ", xleft, "<", U, "<",
          xright)
# Правостронний критерий
xright4 = np.round(stats.norm.ppf(1 - alpha, 0, 1), 3)
if (U < xright4):
    print("4.2 Правосторонний критерий (ax > ay) : Гипотеза принимается, т.к. выполняется неравенство: ", U, "<", xright4)
else:
    print("4.2 Правосторонний критерий (ax > ay) : Гипотеза отклоняется, т.к. не выполняется неравенство: ", U, "<",
          xright4)
# Левосторонний критерий
xleft4 = -xright4
if (U > xleft4):
    print("4.3 Левосторонний критерий (ax < ay): Гипотеза принимается, т.к. выполняется неравенство: ", U, ">", xleft4)
else:
    print("4.3 Левосторонний критерий (ax < ay): Гипотеза отклоняется, т.к. не выполняется неравенство: ", U, ">",
          xleft4)


# проверка 5-й гипотезы
print("\n\n5. Гипотеза о равенстве мат. ожиданий 2-x выборок, если обе дисперсии неизвестны, но равны")
Sy = statistics.stdev(secondSelection)
T = np.round((firstMean - secondMean) / math.sqrt((1/size1+1/size2)*((size1-1)*Sx**2+(size2-1)*Sy**2)/(size1+size2-2)), 3)
xright = np.round(stats.t.ppf(1 - alpha / 2, size1 +size2- 2), 3)
xleft = -xright
if (xleft < T < xright):
    print("5.1 Двусторонний критерий: Гипотеза принимается, т.к. выполняется неравенство: ", xleft, "<", T, "<", xright)
else:
    print("5.1 Двусторонний критерий: Гипотеза отклоняется, т.к. не выполняется неравенство: ", xleft, "<", T, "<",
          xright)
# Правостронний критерий
xright5 = np.round(stats.t.ppf(1 - alpha, size1+size2-2), 3)
if (U < xright5):
    print("5.2 Правосторонний критерий (ax > ay) : Гипотеза принимается, т.к. выполняется неравенство: ", T, "<", xright5)
else:
    print("5.2 Правосторонний критерий (ax > ay) : Гипотеза отклоняется, т.к. не выполняется неравенство: ", T, "<",
          xright5)
# Левосторонний критерий
xleft5 = -xright5
if (U > xleft5):
    print("5.3 Левосторонний критерий (ax < ay): Гипотеза принимается, т.к. выполняется неравенство: ", T, ">", xleft5)
else:
    print("5.3 Левосторонний критерий (ax < ay): Гипотеза отклоняется, т.к. не выполняется неравенство: ", T, ">",
          xleft5)



# проверка 6-й гипотезы
print("\n\n6. Гипотеза о равенстве дисперсий 2-x выборок, если мат. ожидания неизвестны")
if Sx>Sy:
    F = np.round((Sy*Sy/(Sx*Sx)), 3)
else:
    F = np.round((Sx * Sx / (Sy * Sy)), 3)
xright = np.round(stats.f.ppf(1 - alpha / 2, size1-1,size2- 1), 3)
xleft = np.round(stats.f.ppf(alpha / 2, size1-1,size2- 1), 3)
if (xleft < F < xright):
    print("6.1 Двусторонний критерий: Гипотеза принимается, т.к. выполняется неравенство: ", xleft, "<", F, "<", xright)
else:
    print("6.1 Двусторонний критерий: Гипотеза отклоняется, т.к. не выполняется неравенство: ", xleft, "<", F, "<",
          xright)
# Односторонний критерий
xright6 = np.round(stats.f.ppf(1 - alpha, size1-1, size2-1), 3)
if (U < xright6):
    print("6.2 Односторонний критерий (сигмаy^2 > сигмаx^2) : Гипотеза принимается, т.к. выполняется неравенство: ", F, "<", xright6)
else:
    print("6.2 Односторонний критерий (сигмаy^2 > сигмаx^2) : Гипотеза отклоняется, т.к. не выполняется неравенство: ",
          F, "<", xright6)

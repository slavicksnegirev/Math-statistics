import math

import numpy as np
from scipy.stats import poisson
from scipy import stats
import pandas as pd

size = 1000
# numbers = np.arange(0, 1000)  # Массив от 0 до 99 включительно
selection = poisson.rvs(mu=5, size=size)
print(selection)
# точечныые оценки
mean = np.mean(selection)
var = np.var(selection)
print("Мат. ожидание : " ,mean)
print("Дисперсия : " ,var)

# Стандартное отклонение выборочной средней
sigma_of_mean = stats.sem(selection)
print("Стандартное отклонение : " , sigma_of_mean)
gamma = 0.95

t1 = poisson.ppf((1+gamma)/2,mean,sigma_of_mean)
e = np.sqrt(var/size) * t1
e1 = np.sqrt(2/(size-1)) * var * t1
print("Приближенный интервал для мат. ожидания: [", mean-e, ";", mean+e, "]")
print("Приближенный интервал для дисперсии: [", var - e1, ";", var + e1, "]")

interval = stats.norm.interval(gamma, loc=np.mean(selection), scale=stats.sem(selection))
print("Точный интервал для мат. ожидания: [", interval)

t3 = stats.chi2.ppf((1-gamma)/2, (size-1))
t4 = stats.chi2.ppf((1+gamma)/2, (size-1))
dxl1 = var * (size-1) / t4
dxr1 = var * (size-1) / t3
print("Точный интервал для дисперсии: [", dxl1, ";", dxr1, "]")




mMoment = stats.moment(selection, 2)
print("Метод моментов :", mMoment)

max_mean , max_std = stats.norm.fit(selection)
print("Метод максимального правдоподобия :\n" 
      "\tМат. ожидание: ", max_mean ,
      "\n\tДисперсия: ", max_std**2)# метод максимального правдоподобия


import numpy as np
from scipy.stats import poisson
from scipy import stats

numbers = np.arange(0, 100)  # Массив от 0 до 99 включительно
selection = poisson.rvs(mu=5, size=100)
print(selection)
# точечныые оценки
mean = np.mean(selection)
var = np.var(selection)
print("Мат. ожидание : " ,mean)
print("Дисперсия : " ,np.round(var,5))

# Стандартное отклонение выборочной средней
sigma_of_mean = stats.sem(selection)
print("Стандартное отклонение : " , sigma_of_mean)
gamma = 0.95

t1 = poisson.ppf((1+gamma)/2,mean,sigma_of_mean)
e = np.sqrt(var/100) * t1
e1 = np.sqrt(2/99) * var * t1
print("Приближенный интервал для мат. ожидания: [", mean-e, ";", mean+e, "]")
print("Приближенный интервал для дисперсии: [", var - e1, ";", var + e1, "]")

interval = stats.norm.interval(gamma, loc=np.mean(selection), scale=stats.sem(selection))
print("Точный интервал для мат. ожидания: [", interval)

t3 = stats.chi2.ppf((1-gamma)/2, 99)
t4 = stats.chi2.ppf((1+gamma)/2, 99)
dxl1 = var * 99 / t4
dxr1 = var * 99 / t3
print("Точный интервал для дисперсии: [", dxl1, ";", dxr1, "]")




mMoment = stats.moment(selection, 2)
print("Метод моментов :", np.round(mMoment,5))

max_mean , max_std = stats.norm.fit(selection)
print("Метод максимального правдоподобия :\n" 
      "\tМат. ожидание: ", max_mean ,
      "\n\tДисперсия: ", np.round(pow(max_std,2),5))# метод максимального правдоподобия



print('Доверительный интервал для математического ожидания: ', end='')
print(*stats.t.interval(0.95, len(selection), np.mean(selection), stats.sem(selection)), sep='-')
print('Доверительный интервал для дисперсии: ', end='')
print(*stats.t.interval(0.95, len(selection), np.var(selection), stats.sem(selection)), sep='-')
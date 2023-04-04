import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy import stats
from statsmodels.distributions import ECDF

numbers = np.arange(0, 100)  # Массив от 0 до 99 включительно


def draw_plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 0.25])


# pmf = poisson.pmf(numbers, mu=5)
# pmf = np.round(pmf, 5)
# print(pmf)
# draw_plot(numbers,pmf)

selection = poisson.rvs(mu=5, size=100)
# print(selection)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_xlim([0, 100])
# ax.set_ylim([0, 0.25])
# bins = list(np.arange(0, 20, 1))
# plt.hist(selection, bins=bins, density=True, color='lightgreen', edgecolor='black', rwidth=1)
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# точечныые оценки
# матожидание

mean = np.mean(selection)
var = np.var(selection)
print(mean)
print(var)

# Стандартное отклонение выборочной средней
sigma_of_mean = stats.sem(selection)
print(sigma_of_mean)

gamma = 0.95

interval = stats.poisson.interval(gamma, mean)
print(interval[0], interval[1], )
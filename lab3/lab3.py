import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from statsmodels.distributions import ECDF

numbers = np.arange(0, 100)  # Массив от 0 до 99 включительно


def draw_plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 0.4])
    plt.show()


def draw_plt(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 1.2])
    plt.show()


pmf = poisson.pmf(numbers, mu=5)
pmf = np.round(pmf, 5)
print(pmf)
draw_plot(numbers,pmf)

# cdf = poisson.cdf(numbers, mu=1)
# cdf = np.round(cdf, 5)
# print(cdf)
# draw_plt(numbers,cdf)

s = poisson.rvs(mu=5, size=100)
print(s)
fig = plt.figure()
ax = fig.add_subplot(111)
bins = list(np.arange(0, 20, 1))
plt.hist(s, bins=bins, color='lightgreen', edgecolor='black', rwidth=0.9)
plt.grid(axis='y', alpha=0.75)
plt.show()


# pmf = poisson.pmf(s, mu=1)
# ecdf = ECDF(s)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(ecdf.x, ecdf.y, marker='.', linestyle='dotted')
# ax.plot(bins, pmf, color='orange')
# plt.tight_layout()
# plt.show()
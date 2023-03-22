import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

numbers = np.arange(0, 100)  # Массив от 0 до 99 включительно

pmf = poisson.pmf(numbers, mu=1)
pmf = np.round(pmf, 5)
print(pmf)

plt.plot(numbers, pmf)
plt.title('Функция вероятности')
plt.show()

cdf = poisson.cdf(numbers, mu=1)
cdf = np.round(cdf, 5)
print(cdf)

plt.plot(numbers, cdf)
plt.title('Функция распределения')
plt.show()


def draw_plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlim([-1, 10])
    ax.set_ylim([-1, 2])
    plt.show()

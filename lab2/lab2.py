import numpy as np
from scipy.stats import norm
from scipy.stats import skew
from scipy.stats import kurtosis
from matplotlib import pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

n = 100         # объём выборки
mean = 3        # среднее значение
std = 2         # СКО

# # # # # # # # # # # #
# ТЕОРЕТИЧЕСКАЯ ЧАСТЬ #
# # # # # # # # # # # #

x1 = np.arange(mean - 5, mean + 5, 0.01)            # вариационный ряд нормального распределения
y1_pdf = norm.pdf(x1, mean, std)                    # плотность распределения
y1_cdf = norm.cdf(x1, mean, std)                    # функция распределения
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))
ax.plot(x1, y1_cdf, color='orange', label='F(x)')
ax.plot(x1, y1_pdf, label='f(x)')
fig.legend(loc='upper right',
           bbox_to_anchor=(1, 1),
           bbox_transform=ax.transAxes,
           prop={'size': 15})
ax.set_xlim([mean - 5, mean + 5])
ax.set_ylim([0, 1])
plt.show()

sum = sum(x1)                                       # сумма
median = np.median(x1)                              # медиана
var = np.var(x1)                                    # дисперсия
asd = np.std(x1)                                    # среднее квадратичное отклонение
mse = np.sqrt(asd) / n                              # cредняя квадратичная ошибка
minimum = np.min(x1)                                # минимум
maximum = np.max(x1)                                # максимум
uq = np.quantile(x1, 0.75)                          # верхний квантиль
lq = np.quantile(x1, 0.25)                          # нижний квантиль
coef_asym = skew(x1, axis=0, bias=True)             # коэффициент асимметрии
coef_kurtosis = kurtosis(x1, axis=0, bias=True)     # коэффициент эксцесса

print(f"+---------------------------------------------------------------------------+\n"
      f"|                               Основные статистики                         |\n"
      f"+---------------------------------------------------------------------------+\n")
print(f"Выборочное среднее = {1 / n * sum}")
print(f"Медиана = {median}")
print(f"Выборочная дисперсия = {var}")
print(f"Выборочное среднее квадратичное отклонение = {asd}")
print(f"Средняя квадратичная ошибка = {mse}")
print(f"Минимум = {minimum}")
print(f"Максимум = {maximum}")
print(f"Размах выборки = {maximum - minimum}")
print(f"Верхний квартиль = {uq}")
print(f"Нижний квартиль = {lq}")
print(f"IQR = {uq - lq}")
print(f"Коэффициент асимметрии = {coef_asym}")
print(f"Коэффициент эксцесса = {coef_kurtosis}\n"
      f"+---------------------------------------------------------------------------+")

# # # # # # # # # # # #
# ПРАКТИЧЕСКАЯ  ЧАСТЬ #
# # # # # # # # # # # #

x2 = np.random.normal(mean, std, n)
x2.sort()                                           # вариационный ряд нормального распределения
y2_pdf = norm.pdf(x2, mean, std)                    # плотность распределения
y2_cdf = norm.cdf(x2, mean, std)                    # функция распределения

# Гистограмма по частоте
bins = list(np.arange(np.min(x2), np.max(x2) + 0.2, 1.0))
plt.hist(x2, bins=bins, color='lightgreen', edgecolor='black', rwidth=0.9)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма по частоте')
plt.tight_layout()
plt.show()

# График эмперической функции
ecdf = ECDF(x2)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ecdf.x, ecdf.y, marker='.', linestyle='dotted')
ax.set_xlim([mean - 5, mean + 5])
ax.set_ylim([0, 1])
plt.show()

sum = np.sum(x2)                                    # сумма
median = np.median(x2)                              # медиана
var = np.var(x2)                                    # дисперсия
asd = np.std(x2)                                    # среднее квадратичное отклонение
mse = np.sqrt(asd) / n                              # cредняя квадратичная ошибка
minimum = np.min(x2)                                # минимум
maximum = np.max(x2)                                # максимум
uq = np.quantile(x2, 0.75)                          # верхний квантиль
lq = np.quantile(x2, 0.25)                          # нижний квантиль
coef_asym = skew(x2, axis=0, bias=True)             # коэффициент асимметрии
coef_kurtosis = kurtosis(x2, axis=0, bias=True)     # коэффициент эксцесса

print(f"\nВариационный ряд:\n{x2}\n")
print(f"+---------------------------------------------------------------------------+\n"
      f"|                               Основные статистики                         |\n"
      f"+---------------------------------------------------------------------------+\n"
      f"Объём выборки = {n}")
print(f"Выборочное среднее = {1 / n * sum}")
print(f"Медиана = {median}")
print(f"Выборочная дисперсия = {var}")
print(f"Выборочное среднее квадратичное отклонение = {asd}")
print(f"Средняя квадратичная ошибка = {mse}")
print(f"Минимум = {minimum}")
print(f"Максимум = {maximum}")
print(f"Размах выборки = {maximum - minimum}")
print(f"Верхний квартиль = {uq}")
print(f"Нижний кванриль = {lq}")
print(f"IQR = {uq - lq}")
print(f"Коэффициент асимметрии = {coef_asym}")
print(f"Коэффициент эксцесса = {coef_kurtosis}\n"
      f"+---------------------------------------------------------------------------+")

# Сравнение плотностей распределения
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x1, y1_pdf * n, color='r', label='f(x)')
ax.set_xlim([mean - 5, mean + 5])
ax.set_ylim([0, 25])
bins = list(np.arange(np.min(x2), np.max(x2) + 0.2, 1.0))
plt.hist(x2, bins=bins, color='lightgreen', edgecolor='black', rwidth=0.9)
plt.grid(axis='y', alpha=0.75)
plt.legend()
plt.show()

# Сравнение функций распределения
ecdf = ECDF(x2)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ecdf.x, ecdf.y, marker='.', linestyle='dotted')
ax.plot(x1, y1_cdf, color='orange', label='F(x)')
ax.set_xlim([mean - 5, mean + 5])
ax.set_ylim([0, 1])
plt.ylabel('$F(x)$', fontsize=20)
plt.xlabel('$x$', fontsize=20)
plt.tight_layout()
plt.show()
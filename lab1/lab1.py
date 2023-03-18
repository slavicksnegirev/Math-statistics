import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import skew
from scipy.stats import kurtosis
from matplotlib import pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

array = np.array([1.9, 3.1, 1.3, 0.7, 3.2, 1.1, 2.9, 2.7, 2.7, 4.0, 1.7, 3.2, 0.9, 0.8, 3.1,
                  1.2, 2.6, 1.9, 2.3, 3.2, 4.1, 1.3, 2.4, 4.5, 2.5, 0.9, 1.4, 1.6, 2.2, 3.1,
                  1.5, 1.1, 2.3, 4.3, 2.1, 0.7, 1.2, 1.5, 1.8, 2.9, 0.8, 0.9, 1.7, 4.1, 4.3,
                  2.6, 0.9, 0.8, 1.2, 2.1, 3.2, 2.9, 1.1, 3.2, 4.5, 2.1, 3.1, 5.1, 1.1, 1.9,
                  0.9, 3.1, 0.9, 3.1, 3.3, 2.8, 2.5, 4.0, 4.3, 1.1, 2.1, 3.8, 4.6, 3.8, 2.3,
                  3.9, 2.4, 4.1, 4.2, 0.9])

array.sort()

n = array.size                                      # размер массива
sum = sum(array)                                    # сумма
median = np.median(array)                           # медиана
mode = stats.mode(array)                            # мода
var = np.var(array)                                 # дисперсия
asd = np.std(array)                                 # среднее квадратичное отклонение
mse = np.sqrt(asd)/n                                # cредняя квадратичная ошибка
min = np.min(array)                                 # минимум
max = np.max(array)                                 # максимум
uq = np.quantile(array, 0.75)                       # верхний квантиль
lq = np.quantile(array, 0.25)                       # нижний квантиль
coef_asym = skew(array, axis=0, bias=True)          # коэффициент асимметрии
coef_kurtosis = kurtosis(array, axis=0, bias=True)  # коэффициент эксцесса

print(np.sqrt(asd**2/n))
print(f"\nВариационный ряд:\n{array}\n")
print(f"+---------------------------------------------------------------------------+\n"
      f"|                               Основные статистики                         |\n"
      f"+---------------------------------------------------------------------------+\n"
      f"Объём выборки = {n}")
print(f"Выборочное среднее = {1/n * sum}")
print(f"Медиана = {median}")
print(f"Мода = {mode[0]}")
print(f"Выборочная дисперсия = {var}")
print(f"Выборочное среднее квадратичное отклонение = {asd}")
print(f"Средняя квадратичная ошибка = {mse}")
print(f"Минимум = {min}")
print(f"Максимум = {max}")
print(f"Размах выборки = {max - min}")
print(f"Верхний квантиль = {uq}")
print(f"Нижний квантиль = {lq}")
print(f"IQR = {uq - lq}")
print(f"Коэффициент асимметрии = {coef_asym}")
print(f"Коэффициент эксцесса = {coef_kurtosis}\n"
      f"+---------------------------------------------------------------------------+")

# гистограмма по частоте
bins = list(np.arange(np.min(array), np.max(array) + 0.2, 0.1))
plt.hist(array, bins = bins, color = 'lightgreen', edgecolor = 'black', rwidth = 0.9)
plt.grid(axis = 'y', alpha = 0.75)
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма по частоте')
plt.tight_layout()
plt.show()

# график эмперической функции
ecdf = ECDF(array)
#plt.plot(ecdf.x, ecdf.y, marker = '.', linestyle='solid')
sns.kdeplot(array, cumulative=True)
plt.ylabel('$F(x)$', fontsize = 20)
plt.xlabel('$x$', fontsize = 20)
plt.tight_layout()
plt.show()
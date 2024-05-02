import numpy as np
import math
from prettytable import PrettyTable

N = 10000


def RNSTUD(n):
    z = np.random.normal(0, 1)
    Yn = np.random.chisquare(n)
    return z / math.sqrt(Yn / n)


gfg = []
for i in range(N):
    gfg.append(RNSTUD(10))

M = sum(gfg) / N
t = 0
for x in gfg:
    t += (x - M) ** 2

D = t / N

myTable = PrettyTable(["Момент", "RNSTUD", "Погрешность", "Теоретическое значение"])

myTable.add_row(["E(x)", M, abs(M), 0.0])
myTable.add_row(["V(x)", D, abs(D - 1.25), 1.25])

print(myTable)

import numpy as np
import matplotlib.pyplot as plt

data = gfg

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title('Плотность распределения')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sorted_data = np.sort(data)
y = np.arange(len(sorted_data)) / float(len(sorted_data))
plt.plot(sorted_data, y, color='b')
plt.title('Функция распределения')
plt.grid(True)
plt.show()
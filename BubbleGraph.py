#Pedro Salazar
#19/06/2021
#Program to graph data on bus stops and paved roads in neighborhoods of Cordoba Capital

import matplotlib.pyplot as plt
import numpy as np


#11 es barrios
x = [55, 55, 57, 59, 66, 67, 70, 70, 71, 76, 77, 78, 79, 80, 90, 83, 84, 84, 85, 85, 92, 86, 87, 90, 90, 91,
     92, 93, 96, 99]#percentage of paved roads

y = [0.62709457, 0.74180724, 0.728452, 2.52121127, 1.51176328, 1.10882262, 1.11239182, 1.41626441,
     1.4416134, 1.52295992, 1.55532254, 1.91853461, 2.14391002, 2.19008022, 1.52198872, 3.20284069,
     2.88957358, 2.9410206, 3.50037931, 3.0190726, 2.20906451, 2.4465844, 3.07426054,
     3.13078709, 3.47262501, 2.95270421, 3.75403437, 3.81678062, 2.97505069, 3.85879462]#bus stops per 1k

z = [377.69987656, 480.62477549, 873.14616278, 1156.81970198, 116.21484806, 1774.47230584,
     763.47362632, 1463.40016876, 1566.13850423, 1075.58509495, 714.95887229, 795.42149519,
     301.66367583, 842.15146397, 1335.73849268, 403.59012842, 1145.502635, 286.21409457, 1051.0408576,
     227.57989186, 1953.46328334, 1718.31467741, 901.65312715, 1872.43801039, 395.1023964, 593.99648437,
     1495.02818296, 1965.04865305, 1095.46235742, 434.31284205]#population normalized to 2k for circle size

colors = ['#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0',
          '#18E5D0','#FF0000','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0',
          '#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0','#18E5D0',
          '#18E5D0','#18E5D0','#18E5D0']#colors so interest one highlights


#section to normilize x and y data for mobility index
y_max = max(y)
y_norm = [1] * 30
x_max = max(x)
x_norm = [1] * 30

length_y = len(y)
length_x = len(x)

for i in range(length_y):
    y_norm[i] = y[i] / y_max

for i in range(length_x):
    x_norm[i] = x[i] / x_max

mob_score = [1] * 30

for i in range(len(mob_score)):
    mob_score[i] = (y_norm[i] + x_norm[i])/2


#drawing bubble graph
plt.scatter(x, y, c=colors, s=z, alpha=0.6, edgecolors="lightgrey", linewidth=1)

plt.xlabel("Porcentaje de Calles Pavimentadas")
plt.ylabel("Paradas por 1.000 habitantes")
plt.title("Calles Pavimentadas y Paradas por Barrio")
plt.show()


#calculates 10% margin of error for mob_score
error = []

for i in mob_score:
    error.append(i * 0.1)


#drawing mobility index graph
x_axis = np.linspace(0, 29, 30)
plt.bar(x_axis, mob_score, color = colors, yerr = error, capsize = 5)
plt.xlabel("Indice de Mobilidad Basado en Paradas y Pavimentación")
plt.ylabel("Indice de Mobilidad")
plt.title("Barrios")
plt.show()
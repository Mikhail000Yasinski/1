import pandas
import random
import matplotlib
import numpy as np
import matplotlib.pyplot as plts

mass = [float(m) for m in input("Введите все значение масс грузов через пробел").split()]
mass = np.array(mass)

plts.bar(list(range(len(mass))), mass)
plts.title('Experimental data')

df = pandas.DataFrame(data={
    'mass': mass
})

df.to_csv("mass.csv")

df1 = pandas.read_csv("mass.csv")

df1['mass'].plot(kind='bar')

df12 = pandas.DataFrame(data={
    'df1': df1['mass']})

df12.plot.kde()

from scipy import stats

d1 = df12['df1']

plts.show()

print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=5000))

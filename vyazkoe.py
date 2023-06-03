import numpy
import matplotlib.pyplot as plt
h = 0.1  # разбиение
gamma = numpy.sqrt(5/(9.81*1*4)) # sqrt(I/(g*l*m))
t = [i * h*gamma for i in range(1,int(100/h)+2)] # натуральное время
beta = 0.1  # коэф сопротивления
x = [0] #угол, уже в натуральных единицах
y = [1] #безразмерная угловая скорость
j = 0
while j < 100:
    i = int(j * (1 / h))
    k0 = h * y[i]
    l0 = h * (-beta * y[i] - numpy.sin(x[i]))
    k1 = h * (y[i] + 0.5 * l0)
    l1 = h * (-beta * (y[i] + 0.5 * l0) - numpy.sin(x[i] + 0.5 * k0))
    k2 = h * (y[i] + 0.5 * l1)
    l2 = h * (-beta * (y[i] + 0.5 * l1) - numpy.sin(x[i] + 0.5 * k1))
    k3 = h * (y[i] + l2)
    l3 = h * (-beta * (y[i] + l2) - numpy.sin(x[i] + k2))
    x.append(x[i] + (1 / 6) * (k0 + 2 * k1 + 2 * k2 + k3))
    y.append(y[i] + (1 / 6) * (l0 + 2 * l1 + 2 * l2 + l3))
    j = round(j+ h,1)

plt.plot(t, x)
y_ticks = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
plt.yticks(ticks=y_ticks)
plt.xlabel('t, c')
plt.ylabel('$\phi$, рад')
plt.show()

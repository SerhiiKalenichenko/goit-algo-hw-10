import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2

N = 1_000_000
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)

integral_mc = (b - a) * np.mean(y_rand)

integral_quad, error_quad = spi.quad(f, a, b)

print("Метод Монте-Карло:", integral_mc)
print("Quad:", integral_quad)
print("Похибка:", abs(integral_mc - integral_quad))
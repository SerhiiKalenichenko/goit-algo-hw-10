import numpy as np

def f(x):
    return x ** 2

a = 0
b = 2

N = 1_000_000
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)

integral_mc = (b - a) * np.mean(y_rand)

# Аналітичне значення інтеграла f(x)=x² → x³/3
integral_exact = (b**3 / 3) - (a**3 / 3)

print("Метод Монте-Карло:", integral_mc)
print("Аналітичне:", integral_exact)
print("Похибка:", abs(integral_mc - integral_exact))
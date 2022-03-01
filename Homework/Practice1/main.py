from math import *

def f1(x):
    return x**42

def f2(x):
    if x<0.5:
        return x**2
    else:
        return sqrt(x - 0.5)

def f3(x):
    return sqrt((x**3 + x**8 / 26) / (x**7 - cos(x))) + sqrt(log(x) + x**3 + 29) + sqrt(67 * x**4 - sin(x))

def f4(x):
    s = 0
    for i in range(11):
        s += 17 * i**5 - i**7 + 27
    return 75 * s

def f5(x):
    s = 0
    for i in range(11):
        s += x**5 - x
    return 42 * s

def f6(x):
    p = 1
    for i in range(1, 11):
        p *= x * sqrt(i)
    return p

def f7(x):
    s = 0
    for i in range(11):
        for j in range(1, 11):
            s += x**i + x**(2 * j)
    return 0.5 * s

def f8(x):
    if x == 0:
        return 3
    else:
        return sin(f8(x - 1)) - (1 / 16) * (f8(x - 1)**3)

def f9(y):
    n = len(y)
    s = 0
    for i in range(n):
        s += y[i]**2
    return sqrt(s)

print(f1(0.5), f1(0.75))
print(f2(0.4), f2(0.5), f2(0.7))
print(f3(1.5), f3(15))
print(f4(0.1), f4(0.5), f4(1.5))
print(f5(0.1), f5(0.5), f5(1.5))
print(f6(0.1), f6(0.5), f6(1.5))
print(f7(0.1), f7(0.5), f7(1.5))
print(f8(8), f8(9), f8(0))
print(f9([1, 1, 1]), f9([3, 4, 5]), f9([1, 0, 0, 2, 4, 5, 7, 10]))
import math


def f1(x, z):
    a1 = 75 * math.tan(z) ** 7 + (x ** 3) / 58
    a2 = 26 - 92 * math.sin(x ** 3 + z ** 2 + 91) ** 2
    a3 = 27 * (z ** 2) - 34 * math.asin(z - 1 - x ** 2) ** 3
    a4 = math.sqrt(a2 / a3)
    return a1 - a4


f1(0.08, 0.47)
f1(-0.89, 0.98)

print(f1(0.08, 0.47))
print(f1(-0.89, 0.98))
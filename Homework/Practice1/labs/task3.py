import math


def main(m, a, b, n, x):
    s = 0
    for k in range(1, a + 1):
        for i in range(1, m + 1):
            s += 32 + 31 * math.log(k + 23 * i ** 3) ** 6 + 19 * k ** 3

    for c in range(1, n + 1):
        for j in range(1, b + 1):
            p = 1
            for i in range(1, a + 1):
                a1 = (68 * j + c ** 3 + 1) ** 6
                a2 = (i ** 3 - j ** 2) ** 7
                p *= a1 + 77 * x ** 5 + a2
            s -= p

    return s


main(6, 8, 2, 3, -0.61)
main(5, 8, 4, 3, 0.71)

print(main(6, 8, 2, 3, -0.61))
print(main(5, 8, 4, 3, 0.71))

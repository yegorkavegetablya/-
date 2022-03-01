from math import *


def filler():
    print("\n--------------------------------------------------------\n")


def task1():
    print(1 + 3 - 2 / 5 * 7 % 2)


def task2():
    print(1.0/3)
    print(frexp(10))
    # print(2**2**2**2**2**2**2**2)

    a1 = 42
    #a2 = 42l
    a3 = 42.0
    #a4 = 42L
    a5 = 0b101010
    a6 = 0x2a
    a7 = 0o52
    #a8 = 4_2

    print(a1 == 42)
    #print(a2 == 42)
    print(a3 == 42)
    #print(a4 == 42)
    print(a5 == 42)
    print(a6 == 42)
    print(a7 == 42)


def mul1(x):
    a = x + x
    b = a + a
    c = b + b
    return c + b


def mul2(x):
    a = x + x
    b = a + a
    c = b + b
    return c + c


def mul3(x):
    y = x
    x += x
    x += x
    x += x
    y -= x
    x -= y
    return x  #6


def mul4(x):
    a = x + x #2
    b = a + a #4
    c = b + b #8
    d = c - x #7
    e = d + d #14
    f = e + e #28
    return f + x #29

    # 29 = 28 + 1 = 7 * 4 + 1 = (4 + 2 + 1) * 4 + 1 = (8 - 1) * 4 + 1


def task4(x):
    print(mul1(x))
    print(mul2(x))
    print(mul3(x))
    print(mul4(x))


def task6(x):
    #1 = 2
    #return x x
    #print(unknown_name)
    #print("1" - [1, 3])
    #if 1 == 1:
    #print(1 / 0)
    #print(sqrt(-1))
    #print(exp(100000))
    return 0


def naive_mul(x, y):
    r = 0
    for i in range(y):
        r += x
    return r


def task9():
    for i in range(101):
        for j in range(101):
            try:
                assert i * j == naive_mul(i, j)
            except AssertionError:
                print("Something gone wrong")
            else:
                print("The function works fine")


def fast_mul(x, y):
    res = 0
    while x != 0:
        if x % 2 == 1:
            res += y
        x //= 2
        y *= 2
    return res


def fast_pow(x, y):
    res = 1
    while y != 0:
        if y % 2 == 1:
            res *= x
        y //= 2
        x *= x
    return res


def task10():
    for i in range(101):
        for j in range(101):
            try:
                assert i * j == fast_mul(i, j)
            except AssertionError:
                print("Something gone wrong")
            else:
                print("The function works fine")
    for i in range(11):
        for j in range(11):
            try:
                assert i ** j == fast_pow(i, j)
            except AssertionError:
                print("Something gone wrong")
            else:
                print("The function works fine")


def fast_mul_gen(y):
    print("def f(x):")
    print("\ts = 0")
    n = 1
    while y != 0:
        print("\t" + ("x1 = x" if n // 2 == 0 else "x" + str(n) + " = x" + str(n // 2) + " + x" + str(n // 2)))
        if y % 2 == 1:
            print("\ts += x" + str(n))
        y //= 2
        n *= 2
    print("\treturn s")


def fast_pow_gen(y):
    print("def f(x):")
    print("\tp = 1")
    n = 1
    while y != 0:
        print("\t" + ("x1 = x" if n // 2 == 0 else "x" + str(n) + " = x" + str(n // 2) + " * x" + str(n // 2)))
        if y % 2 == 1:
            print("\tp *= x" + str(n))
        y //= 2
        n *= 2
    print("\treturn p")


def task11():
    fast_mul_gen(int(input("Введите число для тестирования умножения из 11 задания: ")))
    fast_pow_gen(int(input("Введите число для тестирования умножения из 11 задания: ")))


task1()
filler()
task2()
filler()
task4(3)
filler()
task6(3)
filler()
#task9()
filler()
#task10()
filler()
#task11()
filler()
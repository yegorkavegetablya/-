def f1(s):
    return [float(el) for el in s]


def f2(s):
    return len(set(s))


def f3(s):
    return s[::-1]


def f4(s, x):
    return [i for i in range(len(s)) if s[i] == x]


def f5(s):
    return sum(s[1::2])


def f6(s):
    return sorted(s, key=lambda x: len(x))[-1]


s1 = ["1", "2", "123345567", "3.45", "0.00000001123", "2"]
s2 = [1, 2, 123345567, 3.45, 0.00000001123, 2]
print(f1(s1))
print(f2(s2))
print(f3(s2))
print(f4(s2, 2))
print(f5(s2))
print(f6(s1))

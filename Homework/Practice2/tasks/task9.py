a = 1
b = 1
c = 300000 # проверено в Python 3.10
d = 300000
print(a is b, c is d)
# В python все числа, используемые в программе, хранятся в отдельном метсе,
# и поэтому когда создаётся переменная какого-либо числа, интерпритатор проверяет,
# есть ли уже переменная с таким числом и если есть, просто указывает ссылку на него.
# По этой причине они по сути являются одним и тем же

a, b = 'py', 'py'
c = ''.join(['p', 'y'])
print(a is b, a == c, a is c, a == c)
# То же самое, что и с числами
# Причина по которой интерпритатор посчитал последнюю строку за другую (не смотря на то что она такая же как и первые две),
# в том, что изначаль она была пустой, а результат получился путём преобразований в методе join, из-за чего это стала
# другая строка
def print_table(t):
    if len(t) == 0:
        print("Таблица должна содержать элемнеты! Ваша таблица:\n" + str(t))
        return

    longest = -1
    for el in t:
        if type(el) is not list:
            print("Таблица должна состоять из списков! Ваша таблица:\n" + str(t))
            return
        if len(el) != len(t[0]):
            print("Строки таблицы должны быть той же длины, что и количество столбцов! Ваша таблица:\n" + str(t))
            return
        for el_el in el:
            longest = max(longest, len(str(el_el)))

    for i in range(len(t)):
        if i == 0:
            print(" " * longest, end=" | ")
        else:
            print(" " * (longest - len(str(i))) + str(i), end=" | ")

        for j in range(len(t[i])):
            print(" " * (longest - len(str(t[i][j]))) + str(t[i][j]), end=(" | " if j != len(t[i]) - 1 else "\n"))

        if i == 0:
            print("-" * longest, end=" | ")
            for j in range(len(t[i])):
                print("-" * longest, end=(" | " if j != len(t[i]) - 1 else "\n"))


print_table([
    ["First", "Second"],
    [123, 456],
    [111, 222]
])
print_table([
    ["First", "Second"],
    [123, 456],
    [111, 222, 333]
])
print_table([])
print_table([
    ["First", "Second"],
    123123123,
    [111, 222]
])

def remove_same_rows_func_1(t, odds):
    for el in odds:
        while t.count(el) > 1:
            t.pop(len(t) - t[::-1].index(el) - 1)


def remove_same_rows_func_2(t, odds, i, j):
    if j > i:
        for k in range(len(t[i])):
            if t[i][k] != t[j][k]:
                break
        else:
            odds.append(t[i])


def remove_same_rows(t):
    odds = []
    for i in range(len(t)):
        for j in range(len(t)):
            remove_same_rows_func_2(t, odds, i, j)
    remove_same_rows_func_1(t, odds)


def remove_same_columns_func_1(t, odds):
    for el in odds:
        for i in range(len(t)):
            while t[i].count(el) > 1:
                t[i].remove(el)


def remove_same_columns_func_2(t, odds, i, j):
    for k in range(len(t)):
        if j > i and t[k][j] != t[k][i]:
            break
    else:
        for index in range(len(t)):
            odds.append(t[index][j])


def remove_same_columns(t):
    odds = []
    for i in range(len(t[0])):
        for j in range(len(t[0])):
            remove_same_columns_func_2(t, odds, i, j)
    remove_same_columns_func_1(t, odds)


def remove_blank_rows_func_1(t, odds):
    for el in odds:
        while el in t:
            t.remove(el)


def remove_blank_rows(t):
    odds = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] is not None:
                break
        else:
            odds.append(t[i])
    remove_blank_rows_func_1(t, odds)


def remove_blank_columns_1(t, odds):
    for el in odds:
        for i in range(len(t)):
            while el in t[i]:
                t[i].remove(el)


def remove_blank_columns_2(t, odds, i):
    for j in range(len(t)):
        if t[j][i] is not None:
            break
    else:
        for index in range(len(t)):
            odds.append(t[index][i])


def remove_blank_columns(t):
    odds = []
    for i in range(len(t[0])):
        remove_blank_columns_2(t, odds, i)
    remove_blank_columns_1(t, odds)


def change_table(t):
    for ti in t:
        new_value_0 = "Не выполнено" if ti[0] == "нет" else "Выполнено"
        ti[0] = new_value_0

        new_value_1 = "(" + ti[1][3:6] + ") " + ti[1][7:13] + "-" + ti[1][13:]
        ti[1] = new_value_1

        new_value_2 = ti[2][:6] + ti[2][8:]
        ti[2] = new_value_2

        new_value_3 = ti[3].split()[-1]
        ti[3] = new_value_3

        ti[1], ti[3] = ti[3], ti[1]
        ti[2], ti[3] = ti[3], ti[2]


def main(t):
    remove_blank_rows(t)
    remove_blank_columns(t)
    remove_same_rows(t)
    remove_same_columns(t)
    change_table(t)
    return t


t1 = [
    ['нет', 'Марат А. Довотиди', '+7 710 704-2158', '05/04/2003',
     None, 'Марат А. Довотиди'],
    ['да', 'Амир М. Мигабин', '+7 739 369-3630', '16/11/1999',
     None, 'Амир М. Мигабин'],
    [None, None, None, None, None, None],
    ['да', 'Амир М. Мигабин', '+7 739 369-3630', '16/11/1999',
     None, 'Амир М. Мигабин'],
    ['да', 'Амир М. Мигабин', '+7 739 369-3630', '16/11/1999',
     None, 'Амир М. Мигабин'],
    [None, None, None, None, None, None],
    ['да', 'Глеб В. Зомко', '+7 845 775-1576', '28/12/2000',
     None, 'Глеб В. Зомко'],
    ['да', 'Ян З. Тецовий', '+7 581 816-2307', '06/10/2004',
     None, 'Ян З. Тецовий']]
t2 = [
    ['нет', 'Дмитрий Б. Цацибман', '+7 803 284-3073', '19/02/1999',
     None, 'Дмитрий Б. Цацибман'],
    ['нет', 'Дмитрий Б. Цацибман', '+7 803 284-3073', '19/02/1999',
     None, 'Дмитрий Б. Цацибман'],
    ['да', 'Данила З. Локошак', '+7 795 875-9730', '01/10/2000',
     None, 'Данила З. Локошак'],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    ['нет', 'Дмитрий Б. Цацибман', '+7 803 284-3073', '19/02/1999',
     None, 'Дмитрий Б. Цацибман'],
    ['нет', 'Макар К. Дозозский', '+7 984 587-0829', '16/11/2004',
     None, 'Макар К. Дозозский']]

main(t1)
main(t2)

print(t1)
print(t2)

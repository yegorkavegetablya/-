import pandas


def remove_same_rows(t):
    t.drop_duplicates(inplace=True)


def remove_same_columns(t):
    odds = set()
    for i in range(len(t.columns)):
        for j in range(len(t.columns)):
            if i < j and list(t[str(i + 1)]) == list(t[str(j + 1)]):
                odds.add(str(j + 1))
    t.drop(list(odds), axis=1, inplace=True)


def remove_blank_rows(t):
    empty = []
    for i in t.index:
        for j in t.columns:
            if t.at[i, j] is not None:
                break
        else:
            empty.append(i)
    t.drop(empty, axis=0, inplace=True)


def remove_blank_columns(t):
    empty = []
    for i in t.columns:
        for j in t.index:
            if t.at[j, i] is not None:
                break
        else:
            empty.append(i)
    t.drop(empty, axis=1, inplace=True)


def change_table(t):
    counter = 1
    for c in t.columns:
        t.rename(columns={c: str(counter)}, inplace=True)
        counter += 1

    counter = 0
    for r in t.index:
        t.rename(index={r: counter}, inplace=True)
        counter += 1

    c1 = list(t["1"].values)
    for i in range(len(c1)):
        new_value = "Не выполнено" if c1[i] == "нет" else "Выполнено"
        t.at[i, "1"] = new_value

    c2 = list(t["2"].values)
    for i in range(len(c2)):
        new_value = c2[i].split()[-1]
        t.at[i, "2"] = new_value

    c3 = list(t["3"].values)
    for i in range(len(c3)):
        new_value = "(" + c3[i][3:6] + ") " + c3[i][7:13] + "-" + c3[i][13:]
        t.at[i, "3"] = new_value

    c4 = list(t["4"].values)
    for i in range(len(c4)):
        new_value = c4[i][:6] + c4[i][8:]
        t.at[i, "4"] = new_value


def main(t):
    remove_same_rows(t)
    remove_same_columns(t)
    remove_blank_rows(t)
    remove_blank_columns(t)
    change_table(t)


t1 = pandas.DataFrame({
    "1": ["нет", "да", None, "да", "да", None, "да", "да"],
    "2": ["Марат А. Довотиди", "Амир М. Мигабин", None, "Амир М. Мигабин",
          "Амир М. Мигабин", None, "Глеб В. Зомко", "Ян З. Тецовий"],
    "3": ["+7 710 704-2158", "+7 739 369-3630", None, "+7 739 369-3630",
          "+7 739 369-3630", None, "+7 845 775-1576", "+7 581 816-2307"],
    "4": ["05/04/2003", "16/11/1999", None, "16/11/1999", "16/11/1999",
          None, "28/12/2000", "06/10/2004"],
    "5": [None, None, None, None, None, None, None, None],
    "6": ["Марат А. Довотиди", "Амир М. Мигабин", None, "Амир М. Мигабин",
          "Амир М. Мигабин", None, "Глеб В. Зомко", "Ян З. Тецовий"]
                      })
t2 = pandas.DataFrame({
    "1": ["нет", "нет", "да", None, None, "нет", "нет"],
    "2": ["Дмитрий Б. Цацибман", "Дмитрий Б. Цацибман", "Данила З. Локошак",
          None, None, "Дмитрий Б. Цацибман", "Макар К. Дозозский"],
    "3": ["+7 803 284-3073", "+7 803 284-3073", "+7 795 875-9730", None, None,
          "+7 803 284-3073", "+7 984 587-0829"],
    "4": ["19/02/1999", "19/02/1999", "01/10/2000", None, None, "19/02/1999",
          "16/11/2004"],
    "5": [None, None, None, None, None, None, None],
    "6": ["Дмитрий Б. Цацибман", "Дмитрий Б. Цацибман", "Данила З. Локошак",
          None, None, "Дмитрий Б. Цацибман", "Макар К. Дозозский"]
})

main(t1)
t1
main(t2)
t2

print(t1)
print(t2)

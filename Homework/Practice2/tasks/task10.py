import re


def parse_subj(text):
    pattern_variant = r"(вариант|Вариант|ВАРИАНТ|вариант№|Вариант№|ВАРИАНТ№|вариант#|Вариант#|ВАРИАНТ#){0,1}\s*"
    pattern_group = r"(группа|Группа|ГРУППА|группа№|Группа№|ГРУППА№|группа#|Группа#|ГРУППА#){0,1}\s*"
    pattern_group_name = "([нквбиНКВБИnkvbiNKVBI]|инбо|ивбо|инбо|иббо|иибо|ИНБО|ИКБО|ИВБО|ИББО|ИИБО){1}"
    pattern_group_number = r"((-[0-9]{1,2}){0,2}\s*[0-9]{1,2}\s*){0,1}"
    pattern_variant_number = r"\s*[0-9]{1,2}"
    pattern = pattern_group + pattern_group_name + pattern_group_number + pattern_variant + pattern_variant_number
    #print(pattern)

    return re.compile(pattern).findall(text)


bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py', 'В 11 4',
            '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23',
            '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3',
            'В104', 'В1013', 'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10',
            'ПитонН4 н11', 'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3',
            '2_1.py, 2_2.py', "инбо 11"]


result = []
for current_text in bad_subj:
    current_result = parse_subj(current_text)
    if len(current_result) == 0:
        print(current_text)
    else:
        result.append(current_text)


print("\n\nНазвания сообщений, в которых есть необходимая информация:")
for elem in result:
    print(elem)

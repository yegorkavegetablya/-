import dis
print(dis.dis("[0xfor _ in 'abc']"))  # Выводит [15]

# Интерпритатор начинает считывать строку
# 1. Видит открывающую квадратную скобку, понимает что дальше будет список или генератор списка
# 2. Видит "0", так как с числа переменная начинаться не может, то это число (в каком-то формате)
# 3. Видит после 0 "x", понимает, что это число в шестнадцатиричном формате
# 4. Видит "f". Думает, что это часть числа в шестнадцатиричном формате
# 5. Видит "o". Так как в шестнадцатиричной системе счисления нет цифры "о", то делает вывод что это часть следующего слова
# 6. Видит "r" и пробел после него.Думает, что это служебный оператор "or"
# 7. Видит _ и пробел после, думает, что это переменная, однако такой переменной не существует, выдаёт ошибку
# 8. Видит in - служебное слово, ищет в чём находится то что было обозначено словом "in"
# 9. Видит 'abc' - обычная строка
# 10. Видит закрывающую квадратную скобку, контекста для генератора списков не было, значит это список, пытается его составить
# Для этого он смотрит результат: в списке должен быть либо первый операнд операции or, либо второй.
# Так как первый операнд - это число не равное 0, то or выбирает его, игнорируя второй операнд (поэтому ошибки нет).
# Вот так и получается список из одного элемента - 0xf или 15 в десетяричной системе счисления
# Вот несколько приммеров которые показывают как бы себя вела программа если бы что-то было бы изменено:

#print([0x0 or _ in 'abc'])  # Выдаёт ошибку
# Так как первый операнд равен 0, что приравнивается к False, то проверяется второй, а там неинициализированная переменная _

_ = "a"
print([0x0 or _ in 'abc'])  # Выводит [True]
# Так как первый операнд равен 0, что приравнивается к False, то проверяется второй, а там _ = 'a' содержится в 'abc', то есть in выдаёт результат True

_ = "z"
print([0x0 or _ in 'abc'])  # Выводит [False]
# Так как первый операнд равен 0, что приравнивается к False, то проверяется второй, а там _ = 'z' не содержится в 'abc', то есть in выдаёт результат False
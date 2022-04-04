import random


def generate_last_name():
    result = ""
    endings = ["ич", "ян", "нц", "ли", "ко", "як"]
    vowel = ["а", "е", "и", "о", "у", "я"]
    consonant = ["б", "в", "г", "д", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ш"]
    now = random.randint(0, 1)
    for i in range(random.randint(6, 10)):
        if now == 0:
            if i == 0:
                result += vowel[random.randint(0, len(vowel) - 1)].upper()
            else:
                result += vowel[random.randint(0, len(vowel) - 1)]
        else:
            if i == 0:
                result += consonant[random.randint(0, len(consonant) - 1)].upper()
            else:
                result += consonant[random.randint(0, len(consonant) - 1)]
        print(now)
        now = (now + 1) % 2
    result += endings[random.randint(0, len(endings) - 1)]
    return result


def generate_names(number):
    f = open("names.txt", "r")
    names = f.readline().split(", ")
    result = []
    for i in range(number):
        name = names[random.randint(0, len(names) - 1)]
        second_name = names[random.randint(0, len(names) - 1)]
        last_name = generate_last_name()
        result_name = name + " " + second_name[0] + ". " + last_name
        result.append(result_name)
    return result


names_list = generate_names(10)
for n in names_list:
    print(n)

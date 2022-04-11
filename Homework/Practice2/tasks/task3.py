def generate_groups():
    a = []
    for i in range(1, 61):
        num = i
        if i <= 8 or i == 13:
            a.append("ИВБО-" + f'{num:02}' + "-20")
        if 13 < i <= 40 or i == 43:
            a.append("ИКБО-" + f'{num - 13:02}' + "-20")
        if 43 < i <= 54 or i == 56 or i == 58:
            a.append("ИНБО-" + f'{num - 43:02}' + "-20")
        if 58 < i <= 60:
            a.append("ИМБО-" + f'{num - 58:02}' + "-20")
    return a


print(generate_groups())
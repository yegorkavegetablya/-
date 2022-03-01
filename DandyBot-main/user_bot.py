def script(check, x, y):
    if check("gold", x, y) != 0:
        return "take"

    # Задаём константные размеры поля в зависимости от уровня
    width, height = 0, 0
    if check("level") == 1:
        width, height = 28, 9
    elif check("level") == 2:
        width, height = 28, 11
    elif check("level") == 3:
        width, height = 28, 25
    elif check("level") == 4:
        width, height = 28, 25
    elif check("level") == 5:
        width, height = 18, 17

    # Стром список посещений клеток поля
    used = []
    for i in range(height):
        used.append([])
        for j in range(width):
            used[i].append(False)

    # Запускаем BFS для поиска ближайшего золота
    query = [[y, x, None]]
    while len(query) != 0:
        current_tile_info = query[0]
        query.pop(0)

        if current_tile_info[0] - 1 >= 0:
            if not used[current_tile_info[0] - 1][current_tile_info[1]]:
                if not check("wall", current_tile_info[1], current_tile_info[0] - 1) and not check("player", current_tile_info[1], current_tile_info[0] - 1):
                    new_tile = [current_tile_info[0] - 1, current_tile_info[1], None]
                    if current_tile_info[0] == y and current_tile_info[1] == x:
                        new_tile[2] = get_direction(new_tile, x, y)
                    else:
                        new_tile[2] = current_tile_info[2]

                    if check("gold", current_tile_info[1], current_tile_info[0] - 1):
                        return new_tile[2]

                    query.append(new_tile)
                    used[new_tile[0]][new_tile[1]] = True

        if current_tile_info[0] + 1 < height:
            if not used[current_tile_info[0] + 1][current_tile_info[1]]:
                if not check("wall", current_tile_info[1], current_tile_info[0] + 1) and not check("player", current_tile_info[1], current_tile_info[0] + 1):
                    new_tile = [current_tile_info[0] + 1, current_tile_info[1], None]
                    if current_tile_info[0] == y and current_tile_info[1] == x:
                        new_tile[2] = get_direction(new_tile, x, y)
                    else:
                        new_tile[2] = current_tile_info[2]

                    if check("gold", current_tile_info[1], current_tile_info[0] + 1):
                        return new_tile[2]

                    query.append(new_tile)
                    used[new_tile[0]][new_tile[1]] = True

        if current_tile_info[1] - 1 >= 0:
            if not used[current_tile_info[0]][current_tile_info[1] - 1]:
                if not check("wall", current_tile_info[1] - 1, current_tile_info[0]) and not check("player", current_tile_info[1] - 1, current_tile_info[0]):
                    new_tile = [current_tile_info[0], current_tile_info[1] - 1, None]
                    if current_tile_info[0] == y and current_tile_info[1] == x:
                        new_tile[2] = get_direction(new_tile, x, y)
                    else:
                        new_tile[2] = current_tile_info[2]

                    if check("gold", current_tile_info[1] - 1, current_tile_info[0]):
                        return new_tile[2]

                    query.append(new_tile)
                    used[new_tile[0]][new_tile[1]] = True

        if current_tile_info[1] + 1 < width:
            if not used[current_tile_info[0]][current_tile_info[1] + 1]:
                if not check("wall", current_tile_info[1] + 1, current_tile_info[0]) and not check("player", current_tile_info[1] + 1, current_tile_info[0]):
                    new_tile = [current_tile_info[0], current_tile_info[1] + 1, None]
                    if current_tile_info[0] == y and current_tile_info[1] == x:
                        new_tile[2] = get_direction(new_tile, x, y)
                    else:
                        new_tile[2] = current_tile_info[2]

                    if check("gold", current_tile_info[1] + 1, current_tile_info[0]):
                        return new_tile[2]

                    query.append(new_tile)
                    used[new_tile[0]][new_tile[1]] = True

    return "pass"


def get_direction(current_tile, x, y):
    if current_tile[0] < y:
        return "up"
    elif current_tile[0] > y:
        return "down"
    elif current_tile[1] < x:
        return "left"
    else:
        return "right"

import matplotlib.pyplot as plt


def get_old_games():
    f = open("old_games.txt", "r", encoding="utf-8")
    old_games = []
    while True:
        line = f.readline()
        if not line:
            break
        current_old_game = line.split(";")
        for i in range(len(current_old_game)):
            current_old_game[i] = current_old_game[i][1:len(current_old_game[i]) - 1]
        old_games.append(current_old_game)
    return old_games


old_games = get_old_games()

years_activity = dict([(old_game[3], 0) for old_game in old_games])
for old_game in old_games:
    years_activity[old_game[3]] += 1
plt.bar(years_activity.keys(), years_activity.values())
plt.show()

genres = set([old_game[1] for old_game in old_games])
for genre in genres:
    years_activity = dict([(old_game[3], 0) for old_game in old_games])
    for old_game in old_games:
        years_activity[old_game[3]] += (1 if old_game[1] == genre else 0)
    plt.bar(years_activity.keys(), years_activity.values())
    plt.title(genre)
    plt.show()
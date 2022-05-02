import matplotlib.lines
import matplotlib.patches
import matplotlib.path
import matplotlib.pyplot as plt


def get_planets_list():
    file = open("planets_discriptions.txt", "r")
    result = []
    while True:
        line = file.readline()
        if not line:
            break

        index = 0
        while not line[index].isalpha():
            index += 1

        name = ""
        while line[index].isalpha():
            name += line[index]
            index += 1

        index += 2
        first_number = 0
        while line[index].isdigit():
            first_number = first_number * 10 + int(line[index])
            index += 1

        index += 1
        second_number = 0
        while line[index].isdigit():
            second_number = second_number * 10 + int(line[index])
            index += 1

        result.append([name, first_number, second_number])

    return result


def draw_plot(planets):
    names = []
    x = []
    y = []
    for planet in planets:
        names.append(planet[0].upper())
        x.append(planet[1])
        y.append(planet[2])

    # plt.xlim(0, 256)
    # plt.ylim(0, 256)

    plt.axis("off")
    plt.title("")

    fig, ax = plt.subplots()

    fig.set_figwidth(256)
    fig.set_figheight(256)

    ax.legend

    ax.set_facecolor('black')  # цвет области Axes

    plt.scatter(x, y, c=["#FFFFFF"]*len(x), s=2)
    for i in range(len(names)):
        plt.text(x[i] + 2, y[i] + 2, names[i], c="white")

    plt.show()


draw_plot(get_planets_list())

def main(y):
    if y < -32:
        return 4 * (45 * y - y ** 3 - y ** 2) ** 7 - y ** 2
    elif -32 <= y < -10:
        return (88 * y ** 2 - y) ** 2 - y / 18
    elif -10 <= y < 89:
        return 85 * (y ** 3 + 24 * y + 0.1) + 25 * y ** 2
    else:
        return (y ** 2 / 98) ** 2


main(120)
main(71)

print(main(120))
print(main(71))
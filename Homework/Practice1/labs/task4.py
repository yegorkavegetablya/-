def main(n):
    if n == 0:
        return 0.44
    else:
        a = main(n - 1) ** 3
        return 0.02 + a + ((20 * a) ** 2) / 84


main(7)
main(4)

print(main(7))
print(main(4))
import sys


def my_print(*args, sep=", ", end="\n", file=None):
    if file is None:
        for i in range(len(args)):
            sys.stdout.write(str(args[i]))
            if i != len(args) - 1:
                sys.stdout.write(sep)
        sys.stdout.write(end)
    else:
        for i in range(len(args)):
            file.write(str(args[i]))
            if i != len(args) - 1:
                file.write(sep)
        file.write(end)


my_print("asddd", "rtegc", "123354")
my_print("asddd", "rtegc", "123354", sep=":")
my_print("asddd", "rtegc", "123354", end="\n\n\n")
my_print("asddd", "rtegc", "123354", sep="; ", end=" Вот и всё(\n")
file = open("test.txt", "w+")
my_print("asddd", "rtegc", "123354", file=file)
my_print("asddd", "rtegc", "123354", sep=":", file=file)
my_print("asddd", "rtegc", "123354", end="\n\n\n", file=file)
my_print("asddd", "rtegc", "123354", sep="; ", end=" Вот и всё(\n", file=file)

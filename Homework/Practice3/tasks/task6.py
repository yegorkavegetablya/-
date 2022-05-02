import sys


def run_with_log(func):
    usual_stderr = sys.stderr
    sys.stderr = open("log_file.txt", "w+")
    func()
    sys.stderr.write("\n\n")
    sys.stderr = usual_stderr


def func():
    a = 0
    b = 1
    print(b / a)


run_with_log(func)

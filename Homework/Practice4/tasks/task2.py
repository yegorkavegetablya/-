import matplotlib.pyplot as plt


class TestClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 12424535

    def foo(self):
        print("Тестовый метод")


def print_all_variables(obj):
    print(vars(obj))


def start_method(obj, method_name):
    getattr(obj, method_name)()


print_all_variables(TestClass())
start_method(TestClass(), "foo")
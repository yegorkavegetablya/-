def f(*, name_arg1=1, name_arg2=2):
    print(name_arg1, name_arg2)


#f(3, 4)
#f(name_arg1=3, 4)
f(name_arg1=3, name_arg2=4)
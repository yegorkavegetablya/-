# whitespace before '('.
def f0 ():
    pass


# missing whitespace around operator.
a = 1+ 2

# missing whitespace after ','.
b = [1,2]


# unexpected spaces around keyword / parameter equals.
def f1(param = 1):
    print(param)

# expected 2 blank lines, found 1.
def f3():
    pass


# multiple statements on one line (colon).
if 1 == 2: pass

# multiple statements on one line (semicolon).
c = 1; d = 2

# comparison to None should be 'if cond is None:'.
if a == None:
    pass

# comparison to True should be 'if cond is True:' or 'if cond:'.
if c == True:
    pass

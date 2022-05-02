import matplotlib.pyplot as p
import random

a = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = random.randint(0, 255)
        if j > len(a[i]) // 2:
            a[i][j] = a[i][len(a[i]) - 1 - j]

p.imshow(a)
p.show()

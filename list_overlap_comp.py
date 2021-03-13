import random

r = random.sample(range(100), 10)
t = random.sample(range(100), 13)
print(r)
print(t)

# a = [3, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [4, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def no_duplicate(x, y):
    c = {i for i in r if i in t}
    print(c)
#   c = {i for i in a if i in b}
#    print(c)


p = no_duplicate(r, t)
#p = no_duplicate(a, b)
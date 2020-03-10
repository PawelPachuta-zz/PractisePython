
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for x in a:
    if x < 5:
        print(x)

# extras
for x in a:
    if x < 5:
        b.append(x)
print(b)


c = [x for x in a if x < 5]
print(c)

d = int(input('Give a number: '))
e = []
for x in a:
    if x < d:
        e.append(x)
print(e)

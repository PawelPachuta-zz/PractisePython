a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

x = set(a)
y = set(b)

for item in x and y:
    d = x.intersection(y)
print(list(d))

c = []
for i in b:
    if i in a:
        c.append(i)
print(c)
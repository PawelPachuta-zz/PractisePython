num = int(input('Give a number: '))
divisors = list(range(1, num + 1))
div = []

for x in divisors:
    if num % x == 0 :
        div.append(x)
print(div)



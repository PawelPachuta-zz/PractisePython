import random

g_num = random.randint(1, 9)
print(g_num)
count = 0
while True:
    your_num = input("Type your number: ")

    if your_num == "Exit":
        print("Thanks for your game")
        break

    your_num = int(your_num)
    count += 1

    if your_num > g_num:
        print("This number is too high")
    elif your_num < g_num:
        print("This number is too low")
    else:
        print("This is correct !")
        print(f"It takes you {count} tries")





















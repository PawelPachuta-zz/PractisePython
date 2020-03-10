x = int(input("Given number: "))



if x % 4 != 0 and x % 2 == 0:
    print(f"The number {x} is even")
elif x % 4 == 0 :
    print(f"{x} could by multiplied by 4")
else :
    print(f"This number -  {x} is odd")
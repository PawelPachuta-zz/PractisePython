
a = 0
while (a < 3):
    weapons = ["scisors", "rock", "paper"]
    player1 = input("Player 1 choose your weapon: ")
    player2 = input("Player 2 choose your weapon: ")
    if player1 == weapons[0] and player2 == weapons[1]:
        print("Player2 is winner")
    elif player1 == weapons[0] and player2 == weapons[2]:
        print("Player1 is winner")
    elif player1 == weapons[1] and player2 == weapons[0]:
        print("Player1 is winner")
    elif player1 == weapons[1] and player2 == weapons[2]:
        print("Player2 is winner")
    elif player1 == weapons[2] and player2 == weapons[0]:
        print("Player2 is winner")
    elif player1 == weapons[2] and player2 == weapons[1]:
        print("Player1 is winner")
    a+=1
print("The Game is over, count the point")









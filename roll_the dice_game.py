# Game of dice
import random
again = True
while again:
    choice = input("would you like to roll the dice ? y/n :")
    if choice =='y':
        user = random.randint(1,6)
        print("you rolled a",user,"!")
        c_c = random.randint(1,6)
        print("c_c rolled a", c_c, "!")
        if user > c_c:
            print("you win")
        elif user < c_c:
            print("you lose")
        else:
            print("It's a draw")
    elif choice == 'n':
        print("thanks for playing")
        break
    else:
        print("Error .please input 'Y' OR 'N' ")

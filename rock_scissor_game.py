# Rock,paper, scissor game:
import random
ls = ['Rock','Scissor','Paper']
c_c = random.choice(ls)
max_attempt = 3
print("lets start the game ")
while max_attempt:
    player_choice = input("ENTER YOUR CHOICE :")
    print("player chose = ", player_choice)
    print("computer chose = ", c_c)
    if player_choice == c_c:
     print("it's a tie ")
    elif player_choice == 'Rock' and c_c == 'scissor':
     print("YOU WIN")
    elif player_choice == 'Scissor' and c_c == 'Paper':
     print("YOU WIN")
    elif player_choice == 'Paper' and c_c == 'Rock':
     print("YOU WIN")
    max_attempt -= 1
    print("you have only", max_attempt, " turn left")
else:
  print("COMPUTER WIN YOU LOSE THE GAME")

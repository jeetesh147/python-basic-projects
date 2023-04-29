# Guess the number Game:
import random
print("!!!!!WELCOME!!!!!!")
user_name = input("enter a player name :")
print(user_name,"i hope you are ready for the game")
print("lets start the game")
# define the countdown func.
import time
# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)  #{:02d = it is the short code }
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
t = 10
countdown(int(t))
max_attempt = 6
# pick a one number by a system
c_c = random.randint(1,50)
while max_attempt:
   num = int(input("Guess the number :"))
   if num > c_c:
      print("too large")
   elif num < c_c:
      print("too small")
   elif num == c_c:
      print("congratulation you won the game")
   max_attempt -=1
   print("you have left only",max_attempt,"attempt")
else:
   print("you loose the game")
   print("never give up try again ")

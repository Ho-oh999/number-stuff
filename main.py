import random

print ("welcome to number guesser")

comp_num = random.randint(0, 10)
tries = 3
win = False
play = True


while play == True:
  while trise > 0:
    print()
    player_num = input("enter a number between 0-10")
    player_num = float( player_num)
    if  player_num <0 or  player_num > 10:
      print ("bad number")
      break
import random
import time
import datetime

def delay():
   time.sleep(0.5)

player = False

while player == False:
   n=random.randint(1,6)
   time.sleep(1)
   print("---------------------------------")
   print("This is a Dice Simulator")
   delay()
   print("The number is " + str(n))
   delay()
   print("---------------------------------")
   
   

   print("Do you want to play again (y/n)")
   input_=input()
   if input_ in ['y']:
      player= False
   else:
      player = True

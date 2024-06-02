#Having fun with making game using conditional statement in python...
#this set of character are taken from the website called. https://ascii.co.uk/art/treasure
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to treasure island.")
print("Your mission is to find the treasure..")
direction = str(input("You're at middle of nowhere. Where do you want to go? Type 'left' or 'right': ")) 
if direction =='right':
  print(" You fell to the hole. Game over.")
else:
  choice = str(input("There is a river. What do you want to do? 'swim' or search for 'boat': "))
  if choice =='swim':
    print("There is the dangerous creature in the river. Game over.")
  else:
    door_select = str(input("Now you are in the treasure house. Through which door do you want to go? 'red', 'blue' and 'yellow': "))  
    if door_select =='red':
      print("The room is full of cobra. Game over..")
    elif door_select == 'blue':  
      print("The room is full of lava. Game over..")
    else:
      print("Wow you made it... !!Victory!!")  


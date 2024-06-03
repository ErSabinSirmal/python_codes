#rock paper scissors game Day-4 final project....
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)
print("\n")
print(f"You choose {choice}:\n")
print(f"Computer choose {computer_choice}:\n")
print("Your choice: \n")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computers choice: \n")
if computer_choice == 0:
    print(rock)

elif computer_choice == 1:
    print(paper)

else: 
    print(scissors)

#Game logic:

if choice == computer_choice:
    print("Draw..")
elif choice == 0 and computer_choice == 1:
    print("You lose..")
elif choice == 1 and computer_choice == 0:
    print("You win..")
elif choice == 1 and computer_choice == 2:
    print("You lose..")
elif choice == 2 and computer_choice == 1:
    print("You win..")
elif choice == 0 and computer_choice == 2:
    print("You win..")
elif choice == 2 and computer_choice == 0:
    print("You lose..")





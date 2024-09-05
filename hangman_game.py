word_list = ["aardvark", "baboon", "camel"]
stages = []

#TODO-1 -Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it
import random
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-1 -Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-2 Create a "Placeholder" with the same number of blanks as the chosen_word
planceholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    planceholder += "_"
print(planceholder)

#TODO 3-Use a while loop to let the user guess again.
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower() #to make the guessed letter into the lowercase.
    print(guess)

    #TODO-1 -Check if the letter the user guessed(guess) is one of the letters in the chosen_word. Print "Right" if it is 
    #, "Wrong" if it's not.

    #TODO -2 Creat4 a "display" that puts the guess letter in the right positions and _ in

    display = ""
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")    
#TODO 3- Change the for loop so that you keep the previous correct letter in display

    for letter in chosen_word:
        if letter ==guess:
             display+= letter
             correct_letters.append(letter)
        elif letter in correct_letters:
            display +=letter
                 
        else:
            display +="_"    
    print(display) 

    if guess not in chosen_word:
        lives -=1
        if lives ==0:
            game_over = True
            print("You lose ")   


    if "_" not in display:
        game_over = True
        print("You Win. ")    

## step 4 todos
#TODO 1 - Create a variable called lives to keep track of the umber of lives left.
  # set lives to equal 6.

#TODO 2 - If guess is not a leter in the chosen_word. Then reduce lives by 1.
    # if lives goes down to 0 then the game should end, and it should print "You lose".

#TODO 3 - Print the ASCII art from te list stages that corresponds to the current number of lives the user has remaining.    
    
    print(stages[lives])

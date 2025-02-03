#Day 4
#Randomisation and Python Lists
import random
friends = ["Alice","Bob","Charlie","david","Emanuel"]

#Ist option
print(random.choice(friends))

#2nd option
random_index = random.randint(0,4)
print(friends[random_index])

# IndexError : list index out of range

# project:RockPaper scissors
rock = r'''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\

'''
paper = r'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   

'''
scissor = r'''
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''

game_images = [rock,paper,scissor]
print("Welcome to the Rock Paper Scissors Game"
      "What dou you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user_choice = int(input("Enter your choice: "))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")
print(game_images[computer_choice])


if user_choice >=3 or user_choice <0:
      print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
      print("You win!")
elif computer_choice == 0 and user_choice == 2:
      print("You lose!")
elif user_choice > computer_choice:
      print("You win!")
elif computer_choice > user_choice:
      print("You lose!")
elif user_choice == computer_choice:
      print("It's a draw!")




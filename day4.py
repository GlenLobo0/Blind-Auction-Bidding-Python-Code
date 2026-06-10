# # import random

# # random_integer =random.randint(1,10)
# # print(random_integer)


# #LIST
# states_of_america = ("Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut")
# import random
# friends = ["Alice","Bob","Charlie KIRK","David","Emanuel"]
# bills = random.choice(friends)
# print(f"{bills} has to pay the bill lol.")





# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images= [rock,paper,scissors]
computer_choice =random.randint(0,2)
user_input = int(input("Enter a number between 0 to 2, \n0 for rock\n1 for paper\n2 for scissors : "))
if user_input >= 0 and user_input<= 2:
    print(game_images[computer_choice])

print("Computer chose: ")
print(game_images[computer_choice])

if user_input >= 3 or user_input < 0 :
    print("U typed it wrong")
elif user_input == 0 and computer_choice == 2 :
    print(  "you win!")
elif computer_choice == 0 and user_input == 2:
    print("U lost")
elif computer_choice > user_input:
    print ("you lost")
elif user_input > computer_choice:
    print("Won homes")
elif computer_choice == user_input:
    print("its a draw")



























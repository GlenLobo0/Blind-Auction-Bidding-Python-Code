#user_input = int(input("Enter a number between 1 to 10 : "))
#modulo_input= user_input % 2
#if modulo_input == 0:
#  print("Even number boi")
#else:
#    print("Odd number gang")

#pizza order
# print("Welcome to Python Pizza Deliveries!")
# size = input("What type of pizza do you want? S,M or L: ")
# pepperoni =input("Do you want pepperoni on your pizza? Y or N :")
# extra_cheese = input("Do you want extra? Y or N: ")
# bill = 0 

# if size == "S":
#     bill+=15
# elif size=="M":
#     bill +=20
# else :
#     bill +=25
#  # hmm


# if pepperoni == "Y":
#     if size == "S":
#         bill+=2
# else:
#     bill+=3
# if extra_cheese =="Y":
#     bill+=1
# print(f"Your final Bill is ${bill}.")


print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
choice1= input('You\'re at a crossroad, where do you want to go ? Type "left" or "right".').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")

else: 
    print("Game Over")



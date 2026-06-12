""""This is a simple "Guess the Number" game where the user has to guess a randomly generated number between 1 and 100.
  The user can choose a difficulty level which determines the number of attempts they have to guess the number. """
import random
#defining a function to set the number of attempts based on the difficulty level chosen by the user
def difficulty_mode(difficulty):
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    return attempts
#defining the main function to run the game
def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    
    number_to_guess = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = difficulty_mode(difficulty)
    
    while True:
        user_guess = int(input("Guess the number between 1 to 100: "))
        attempts -= 1
        
        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the number! Remaining attempts: {attempts}")
            break
            
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
            print(f"You have {attempts} attempts remaining.")
        else:
            print("Too high! Try again.")
            print(f"You have {attempts} attempts remaining.")
            
        if attempts == 0:
            print(f"Game over! The number was {number_to_guess}.")
            break   

# Game starts here
guess_the_number()
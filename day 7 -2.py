import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create placeholder
placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check if the guess is wrong BEFORE the loop
    if guess not in chosen_word:
        lives -= 1

    # Create the display string for the current guess
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print(display)
    print(f"Lives remaining: {lives}")
    
    if "_" not in display:
        print("You Win!")
        game_over = True
    elif lives == 0:
        print("You Lose!")
        game_over = True

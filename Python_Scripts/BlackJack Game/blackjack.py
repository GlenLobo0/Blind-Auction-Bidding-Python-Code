import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score of the given cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1) # Change Ace from 11 to 1
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print("Welcome to Blackjack!")
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_input.lower() == 'y':
        # --- Setting up the deck ---
        user_cards = []  
        computer_cards = []
        game_is_running = True
        
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
            
        # --- Player's Turn ---
        while game_is_running:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            
            if user_score == 0 or computer_score == 0 or user_score > 21:
                game_is_running = False
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_deal == 'y':
                    user_cards.append(deal_card())
                else:
                    game_is_running = False
                    
        # --- Computer's Turn ---
        computer_score = calculate_score(computer_cards)
        
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            
        # --- Final Results ---
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

play_game()
print("Thanks for playing!")
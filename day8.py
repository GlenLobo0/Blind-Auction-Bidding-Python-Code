# 1. Changed to a list using square brackets []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount  % 26
        cipher_text += alphabet[shifted_position]
    print(f"The encoded text is {cipher_text}") 

def decrypt(cipher_text, shift_amount):
    original_text = ""
    for letter in cipher_text:
        shifted_position = alphabet.index(letter) - shift_amount
        original_text += alphabet[shifted_position]
    print(f"The decoded text is {original_text}")

# 2. Re-structured your master function to take your inputs
def caesar(user_direction, text_input, shift_input):
    if user_direction == "encode":
        encrypt(original_text=text_input, shift_amount=shift_input)
    elif user_direction == "decode":
        decrypt(cipher_text=text_input, shift_amount=shift_input)
    else:
        print("Invalid input. Please type 'encode' or 'decode'.")

# 3. Call the master function to run the logic
caesar(user_direction=direction, text_input=text, shift_input=shift)
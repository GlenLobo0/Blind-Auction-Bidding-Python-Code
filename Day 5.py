# student_scored = [150,142,138,120,110,100,90,85,80,75,70,65,60,55,50,45,40,35,30,25]
# max_score =0
# for scored in student_scored:
#     if scored > max_score:
#         max_score = scored

# print(max_score) 

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 ==0:
#         print("Fizz")
#     elif number % 5 ==0:
#         print("Buzz")
#     else:
#             print(number)
import random
letter =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','^','&','*','(',')','-','+']

print("Welcome to the PyPassword generator")
nr_letters=int(input("How many letters would you like in the password??\n"))
nr_symbols=int(input("How many symbols would you like??\n"))
nr_numbers=int(input("How many numbers would you like in the password??\n"))

password = ""
for char in range(0, nr_letters):
    password += random.choice(letter)
for char in range(0, nr_symbols):
    password += random.choice(symbols)
for char in range(0, nr_numbers):
    password += random.choice(number)
print(password)

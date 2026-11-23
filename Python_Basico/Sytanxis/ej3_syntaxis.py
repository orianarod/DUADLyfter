import random #importing this module to use random.randint function

secret_number = random.randint(1,10) 
guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))

print(f"You have guessed the number! It is: {guess}")

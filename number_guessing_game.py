import random

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
secret_number = random.randint(1, 100)
print("Can you guess what it is?")

while True:

    guess = input("Enter your guess (or type 'exit' to quit): ")

    if guess.lower() == 'exit':
        print("Thank you for playing. Goodbye!")
        break
    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break
        
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100 or 'exit' to quit.")
   
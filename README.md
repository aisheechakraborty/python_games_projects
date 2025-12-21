import random

print("Welcome to the Dice Game!")
print("Roll two dice and if the total is greater than 10, you win!")
print("Otherwise, you lose.")
print("Do you want to play a game of Dice?")
print("Type 'y' to play or 'n' to quit.")

while True:
    
    a = input("Type 'y' or 'n': ")

    if a == 'n' or a == 'N':
        print("Thank you for playing. Goodbye!")
        break

    elif a == 'y' or a == 'Y':
        strt = 1
        stop = 6
        dice1 = random.randint(strt, stop)
        dice2 = random.randint(strt, stop)
        total = dice1 + dice2
        print(f"You rolled a {dice1} and a {dice2}. Your total is {total}.")
        if total > 10:
            print("You win!")
        else:
            print("You lose!")

    else:
        print("Invalid input. Please type 'y' or 'n'.")

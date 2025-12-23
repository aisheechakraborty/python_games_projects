import random

print("Welcome to the Stone-Paper-Scissor Game!")

while True:
    choice= input("Do you want to play? (yes/no): ").lower()
    if choice == 'no':
        print("Thank you for playing. Goodbye!")
        break
    print("Choose your option:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissor")
    user_choice = int(input("Enter 1, 2, or 3: "))

    if user_choice not in [1, 2, 3]:
        print("Invalid choice. Please select 1, 2, or 3.")
        continue        
    computer_choice = random.randint(1, 3)
    choices = {1: "Stone", 2: "Paper", 3: "Scissor"}
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):   
        print("You win!")
    else:
        print("Computer wins!")
    
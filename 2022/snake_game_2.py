import random

# Set the initial values for the game
lives = 3
score = 0
level = 1
power_ups = ["skip", "reveal"]

# Main game loop
while lives > 0:
    # Generate a random number between 1 and the level * 10
    secret_num = random.randint(1, level * 10)
    
    # Get the user's guess
    guess = int(input(f"Guess a number between 1 and {level * 10}: "))
    
    # Check if the guess is correct
    if guess == secret_num:
        print("You guessed correctly! You earn 1 point.")
        score += 1
        level += 1
    else:
        print("You guessed incorrectly. You lose 1 life.")
        lives -= 1
    
    # Check if the player has any power-ups
    if power_ups:
        # Ask the player if they want to use a power-up
        use_power_up = input("Would you like to use a power-up? (y/n) ")
        
        if use_power_up == "y":
            # Let the player choose a power-up
            print("Choose a power-up:")
            for i, power_up in enumerate(power_ups):
                print(f"{i + 1}. {power_up}")
            power_up_choice = int(input("Enter the number of your choice: "))
            
            # Use the chosen power-up
            if power_up_choice == 1:
                # Skip the current level
                print("Skipping level.")
                level += 1
                power_ups.remove("skip")
            elif power_up_choice == 2:
                # Reveal the secret number
                print(f"The secret number was {secret_num}.")
                power_ups.remove("reveal")
    
    # Print the current score, lives, and level
    print("Score:", score)
    print("Lives:", lives)
    print("Level:", level)

# Print the final score
print("Game over! Your final score is:", score)

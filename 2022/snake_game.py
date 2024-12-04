import random

# Set the initial values for the game
lives = 3
score = 0

# Main game loop
while lives > 0:
    # Generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    
    # Get the user's guess
    guess = int(input("Guess a number between 1 and 10: "))
    
    # Check if the guess is correct
    if guess == secret_num:
        print("You guessed correctly! You earn 1 point.")
        score += 1
    else:
        print("You guessed incorrectly. You lose 1 life.")
        lives -= 1
    
    # Print the current score and lives
    print("Score:", score)
    print("Lives:", lives)

# Print the final score
print("Game over! Your final score is:", score)

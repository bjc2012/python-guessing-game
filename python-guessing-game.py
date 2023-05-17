# Python Guessing Game
# The User has 3 tries to guess the correct word
# If the user fails 3 times, they lose the game
# Hint: The greatest basketball player of all-time. Must enter first and last name

secret_word = "Lebron James"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("You Lose! You must be a Jordan fan!")
else:
    print("Winner Winner Goat Dinner!")   

    
        

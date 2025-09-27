import random

def play_hangman():
    words = ["python", "flower", "planet", "silver", "garden"]  # list of 5 words
    secret = random.choice(words)  # random
    max_incorrect = 6
    incorrect = 0
    guessed_letters = []  # list to store guessed letters

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect} incorrect guesses. Guess one letter at a time.\n")

    # Helper to show current word state
    def display_word():
        displayed = ""
        for ch in secret:  # loop through characters in the string
            if ch in guessed_letters:
                displayed += ch + " "
            else:
                displayed += "_ "
        return displayed.strip()

    # Main game loop
    while incorrect < max_incorrect:
        print("Word: ", display_word())
        print(f"Incorrect guesses left: {max_incorrect - incorrect}")
        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one.\n")
            continue

        # Record the guess
        guessed_letters.append(guess)

        if guess in secret:
            print("Good guess!\n")
        else:
            incorrect += 1
            print("Wrong guess.\n")

        # Check if all letters are guessed
        all_guessed = all(ch in guessed_letters for ch in secret)
        if all_guessed:
            print("Congratulations! You guessed the word:", secret)
            break
    else:
        # This else runs if the while loop ends normally (no break) -> player lost
        print("Sorry, you've run out of guesses. The word was:", secret)

if __name__ == "__main__":
    play_hangman()
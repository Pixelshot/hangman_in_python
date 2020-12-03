# Step 5
from hangman_words import word_list
from hangman_art import logo, game_over, stages
import random
import os


def clear():
    os.system('clear')


# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Stop printing display when game is over
stop_display = False

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"{guess} has already been chosen")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(sion}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the word. Remaining life: {lives - 1}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(game_over)
            stop_display = True
            print(f"The correct word was {chosen_word}")

    if not stop_display:
        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
    # if lives == 0:
    #     print(game_over)

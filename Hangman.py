import random

import Hangman_words

chosen_word = random.choice(Hangman_words.word_list)

lives = 6

from hangman_art import logo, stages
print(logo)

display = []

for letter in chosen_word:
    display += "_"
print (display)

end_of_game = False

while not end_of_game:
    guess = (input("Guess a letter: ")).lower()

    if guess in display:
        print(f"You already guesses {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print (display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

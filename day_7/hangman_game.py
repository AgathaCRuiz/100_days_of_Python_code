import random
import hangman_art as art
import hangman_words as words

lives = 6

print(art.logo)

chosen_word= random.choice(words.word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

#TODO-2: Use a while loop to let the user guess again

game_over = False
correct_letters = []

while not game_over:

    print(f"======= {lives}/6 Lives left =======")
    guess = input("Guess a letter: ").lower()
    # TODO-3: If the user has entered a letter they've already guessed
    if guess in correct_letters:
        print(f"You've already guessed {guess}")


    # TODO-4: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string

    display = ""

    # TODO-5: Change the for loop so that you keep the previous correct letters in display
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f"It was {chosen_word}! You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(art.stages[lives])
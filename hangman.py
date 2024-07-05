import random
from hangman_drawings import display_hangman


def get_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.split(" | ")[0].strip() for line in file.readlines()]
    return words


def get_random_word(words):
    return random.choice(words)


def display_word_state(word, correct_guesses):
    displayed_word = ""
    for letter in word:
        if letter.lower() in correct_guesses:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def display_menu():
    print("Choose difficulty level:")
    print("1. Easy (10 lives)")
    print("2. Medium (7 lives)")
    print("3. Hard (5 lives)")


def set_lives_based_on_difficulty(difficulty):
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 7
    elif difficulty == 3:
        return 5
    else:
        return 7  # Default


def main():
    words = get_words_from_file('countries-and-capitals.txt')
    if not words:
        print("No words found in the configuration file.")
        return

    display_menu()
    difficulty = int(input("Select difficulty level (1, 2, 3): "))
    lives = set_lives_based_on_difficulty(difficulty)

    word_to_guess = get_random_word(words)
    correct_guesses = set()
    incorrect_guesses = set()

    print("Welcome to Hangman!")
    print("Word to guess:", display_word_state(word_to_guess, correct_guesses))

    while lives > 0 and set(word_to_guess.lower()) != correct_guesses:
        guess = input("Guess a letter (or type 'quit' to exit): ").lower()

        if guess in ["quit", "Quit", "QUIT", "QuIT", "QUIt", "QUit"]:
            print("Game over.")
            break

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed this letter.")
        elif guess in word_to_guess.lower():
            correct_guesses.add(guess)
            print("Correct guess!")
        else:
            incorrect_guesses.add(guess)
            lives -= 1
            print(f"Incorrect guess. Lives left: {lives}")
            display_hangman(lives)

        print("Word status:", display_word_state(word_to_guess, correct_guesses))
        print("Incorrect guesses:", ", ".join(sorted(incorrect_guesses)))

        if set(word_to_guess.lower()) == correct_guesses:
            print("Congratulations! You guessed the word:", word_to_guess)
        elif lives == 0:
            display_hangman(lives)
            print("Game over. The word was:", word_to_guess)


if __name__ == "__main__":
    main()

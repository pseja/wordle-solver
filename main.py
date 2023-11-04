from words import wordle_words, unique_set
from random import choice


def f_position(words, letter, position, include=True):
    filtered_words = set()
    position = int(position) - 1

    for word in words:
        if len(word) > position:
            if (word[position] == letter and include) \
                or (word[position] != letter and not include):
                filtered_words.add(word)

    return filtered_words


def f_letter(words, target_letter):
    filtered_words = set()

    for word in words:
        if target_letter in word:
            filtered_words.add(word)

    return filtered_words


def f_not(words, letters):
    filtered_words = set()

    for word in words:
        if not any(letter in letters for letter in word):
            filtered_words.add(word)

    return filtered_words


def main():
    words = wordle_words
    filtered = set()
    unique_words = unique_set
    used = set()

    first_word = choice(tuple(unique_words))
    used.add(first_word)

    print(first_word)

    while True:
        green = input("\nInput green letters (a1 / a1b2)\n> ")
        yellow = input("\nInput yellow letters (a / a1b2)\n> ")
        grey = input("\nInput grey letters (a / ab)\n> ")

        green_letters = [char for char in green]
        yellow_letters = [char for char in yellow]
        grey_letters = [char for char in grey]

        for i in range(0, len(green_letters), 2):
            if filtered == set():
                filtered = f_position(words, green_letters[i], green_letters[i+1])
            else:
                filtered = f_position(filtered, green_letters[i], green_letters[i+1])

        for j in range(0, len(yellow_letters), 2):
            if filtered == set():
                filtered = f_letter(words, yellow_letters[j])
                filtered = f_position(filtered, yellow_letters[j], yellow_letters[j+1], include=False)
            else:
                filtered = f_letter(filtered, yellow_letters[j])
                filtered = f_position(filtered, yellow_letters[j], yellow_letters[j+1], include=False)

        for k in range(len(grey_letters)):
            if filtered == set():
                filtered = f_not(words, grey_letters[k])
            else:
                filtered = f_not(filtered, grey_letters[k])

        guess = choice(tuple(filtered))
        if guess in used:
            guess = choice(tuple(filtered))

        if len(filtered) > 1:
            print(f"\n{guess}\nPossible words: {len(filtered)}")
        elif len(filtered) == 1:
            print(f"\nThe word is '{guess}'")
        else:
            break


if __name__ == "__main__":
    main()
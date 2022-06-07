import random


def menu():
    while True:
        option = input(
            'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: '
        ).lower()
        if option in {"play", "results", "exit"}:
            break
    return option


def play(attempts: int, hidden_word: str):
    word = "-" * len(hidden_word)
    input_letter = set()
    won, lost = 0, 0

    while attempts > 0:
        print(word)
        if "-" not in word:
            break
        letter = input("Input a letter: ")
        if len(letter) > 1 or letter == "":
            print("Please, input a single letter.")
        elif not letter.islower() or not letter.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in input_letter:
            print("You've already guessed this letter.")
        elif hidden_word.find(letter) == -1:
            attempts -= 1
            print("That letter doesn't appear in the word.")
            input_letter.add(letter)
        else:
            input_letter.add(letter)
            for i in range(len(hidden_word)):
                if hidden_word[i] == letter:
                    word = word[:i] + letter + word[i + 1 :]
        print()

    if "-" in word:
        print("\nYou lost!")
        lost += 1
    else:
        print("\n", f"You guessed the word {hidden_word}!", "You survived!", sep="\n")
        won += 1
    return won, lost


def main():
    print("HANGMAN\n")
    attempts = 8
    random_word = random.choice(["python", "java", "swift", "javascript"])
    stats = {"won": 0, "lost": 0}

    while True:
        option = menu()
        if option == "play":
            won, lost = play(attempts, random_word)
            stats["won"] += won
            stats["lost"] += lost
        elif option == "results":
            print(
                f"You won: {stats['won']} times.",
                f"You lost: {stats['lost']} times.",
                sep="\n",
            )
        elif option == "exit":
            break


if __name__ == "__main__":
    main()

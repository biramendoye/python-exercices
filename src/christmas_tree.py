from colorama import Back, Fore, Style


def line(number_of_characters: int, character: str, color: str) -> None:
    print(
        color + character * number_of_characters,
        end=""
    )


def space(number_of_spaces: int) -> None:
    print(
        " " * number_of_spaces,
        end=""
    )


def tree_trunk(height: int) -> None:
    space(height - 1)
    print("II")
    space(height - 1)
    print("II")
    space(height - 1)
    print("II")


def triangle(height: int) -> str:
    i: int = height - 1
    j = 1

    while i != -1:
        space(i)
        line(j, "^", Fore.GREEN)
        print()  # Go to next line

        i = i - 1
        j = j + 2


def main():
    triangle(13)

    line(26, "#", Fore.RED)

    print()

    tree_trunk(13)

if __name__ == "__main__":
    main()

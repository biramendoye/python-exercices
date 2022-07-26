"""
You’ll get to know the basic syntax of Python and write a simple program using 
variables, conditions, loops, and functions.
Here, at the beginning of your programmer’s path, creating a simple console chat 
bot will do wonders to guide you through the basics of coding. During this journey 
you will also play some word and number games that you are going to implement all 
on your own. Pack up and let’s hit the road, my friend!
"""
def greet(bot_name: str, birth_year:int) -> None:
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f"What a great name you have, {name}!")


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    while (answer := int(input())) != 2:
        print("Please, try again.")

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


if __name__ == '__main__':
    greet('Sheikh', 2022)
    remind_name()
    guess_age()
    count()
    test()
    end()
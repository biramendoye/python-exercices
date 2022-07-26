"""
Learn how to handle input and output, employ the random number generator, 
and write the output to a file.
Many people are fond of interactive learning. In this project, you will learn 
how to write an application that can facilitate solving arithmetic operations in 
a quick manner. The application will generate a mathematical expression for a user 
to solve. Implement various levels of difficulty and let the application save the 
results and show the progress of learning.
"""
import random


def generate_simple_ops() -> tuple:
    return random.randint(2, 9), random.choice(["+", "-", "*"]), random.randint(2, 9)


def generate_integral_square() -> int:
    return random.randint(11, 29)


def menu():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")


def integer_square():
    n = 5
    mark = 0
    while n > 0:
        n -= 1
        task = generate_integral_square()
        while True:
            print(task)
            square = input()
            if square.isdigit():
                break
            else:
                print("Wrong format! Try again.")
        if (task ** 2) == int(square):
            print("Right!")
            mark += 1
        else:
            print("Wrong!")
    return mark


def simple_operations():
    n = 5
    mark = 0
    while n > 0:
        n -= 1
        a, operand, b = generate_simple_ops()
        print(f"{a} {operand} {b}")
        while True:
            answer = input()
            if answer.isdigit():
                break
            elif answer.startswith('-'):
                break
            else:
                print("Incorrect format.")
        result = int(answer)
        if operand == "+":
            if result == a + b:
                print("Right!")
                mark += 1
            else:
                print("Wrong!")
        if operand == "-":
            if result == a - b:
                print("Right!")
                mark += 1
            else:
                print("Wrong!")
        if operand == "*":
            if result == a * b:
                print("Right!")
                mark += 1
            else:
                print("Wrong!")
    return mark


def save_file(name, mark, level=None):
    with open('results.txt', 'a') as f:
        if level == 1:
            result = f"{name}: {mark}/5 in level {level} (simple operations with numbers 2-9)."
        else:
            result = f"{name}: {mark}/5 in level {level} (integral squares of 11-29)."
        f.write(result + '\n')


def main():
    mark = 0
    while True:
        menu()
        choice = int(input())
        if choice == 1 or choice == 2:
            break
        else:
            print("Incorrect format.")

    if choice == 1:
        mark = simple_operations()
    if choice == 2:
        mark = integer_square()

    save_or_not = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.\n")
    if save_or_not in ["yes", "YES", "y", "Yes"]:
        name = input("What is your name?\n")
        save_file(name, mark, choice)
        print('The results are saved in "results.txt".')


if __name__ == '__main__':
    main()
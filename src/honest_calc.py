"""
The International Union Against Idleness (IUAI) announced a competition for an application 
that would motivate users. There are prizes involved. Since you like competing and know a 
little bit about programming, you asked your friend to prepare an interesting algorithm 
for a quick buck. Unfortunately, you weren't clear enough, and instead of a ready-made program, 
a friend prepared a flowchart of Honest Calculator. You will have to put some effort into 
assembling it.

Working on the project, you're at first required to build a simple calculator which later on is going 
to motivate users to try and do the math themselves by becoming more and more honest with them. 
For example, if they need to do calculations with multidigit numbers, that, okay, might be tricky, 
so the calculator won't be very hard on them and just solve it. However, if the equation is a simple 
sum of two integers like 2 + 3, maybe it should suggest solving it themselves. Even worse, 
if it's multiplication by one or zero, that is just of the line! After all, it's a competition 
organized by the International Union Against Idleness.
"""
from typing import List


msg_0: str = "Enter an equation"
msg_1: str = "Do you even know what numbers are? Stay focused!"
msg_2: str = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3: str = "Yeah... division by zero. Smart move..."
msg_4: str = "Do you want to store the result? (y / n):"
msg_5: str = "Do you want to continue calculations? (y / n):"
msg_6: str = " ... lazy"
msg_7: str = " ... very lazy"
msg_8: str = " ... very, very lazy"
msg_9: str = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_one_digit(v : float)-> bool:
    """
    check whether it has an integer value in the mathematical sense, 
    e.g. 3.0 is an integer, 3.1 is a non-integer number. 
    """
    return v > -10 and v < 10 and v.is_integer()

def check(v1, v2, v3)-> None:
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg = msg + msg_7
    if v1 == 0 or v2 == 0 and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg

    print(msg)

def main() -> None:
    is_end: bool = False
    memory: float = 0
    msg_: List = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
    while not is_end:
        try:
            x, oper, y = input(msg_0 + "\n").split()

            if x == 'M':
                x = memory
            if y == 'M':
                y = memory

            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)

        if len(oper) == 1 and oper in ["+", "-", "*", "/"]:
            check(x, y, oper)
            result: float = 0
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/":
                if y == 0:
                    print(msg_3)
                else:
                    result = x / y
            else:
                print(msg_1)
            
            print(result)

            if input(msg_4 + "\n").lower() == "y":
                if is_one_digit(result):
                    msg_index = 10
                    answer = ""
                    while True:
                        answer = input(msg_[msg_index] + "\n").lower()
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                        else:
                            continue
                else:
                    memory = result
            if input(msg_5 + "\n").lower() == "n":
                is_end = True
        else:
            print(msg_2)


if __name__ == "__main__":
    main()
import random
import time

MAX_MOVE: int = 5
MAX_NUMBER_INPUT: int = 100

def main():
    while True:
        print("GAME INITIALIZATION")
        move: int = 0
        mystery_number: int = random.randint(0, MAX_NUMBER_INPUT)
        time.sleep(1)
        print("*=" * 10)
        
        while True:
            if move == MAX_MOVE:
                print("\nYou lost!!! (insufficient number of moves)\n")
                break

            try:
                user_input_number: int = int(input("Guess the number => "))
            except ValueError:
                print("You must input an integer number!!")
            
            if mystery_number > user_input_number:
                move += 1
                print("The mystery number is greater!")
            elif mystery_number < user_input_number:
                move += 1
                print("The mystery number is smaller!")
            else:
                print(f"\nCongratulations, you have found the mystery number in {move} move!!\n")
                break
        
        replay = input("Would you want to replay: (yes or no)? ").lower()
        if replay == "no":
            break

    # while (mystery_number := int(input())) > 0:
    #     print(mystery_number)


if __name__ == "__main__":
    main()
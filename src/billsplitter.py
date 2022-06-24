import random


def main():
    num_friends = int(input("Enter the number of friends joining (including you):\n"))
    if num_friends <= 0:
        print("No one is joining for the party")
    else:
        friends = {}
        print("Enter the name of every friend (including you), each on a new line:")
        for _ in range(num_friends):
            name = input()
            friends[name] = 0

        total_bill_value = int(input("Enter the total bill value:\n"))
        bill = round(total_bill_value / num_friends, 2)
        for key in friends.keys():
            friends[key] = bill

        use_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if use_lucky == 'Yes':
            lucky = random.choice(list(friends.keys()))
            print(f"{lucky} is the lucky one!")
            bill = round(total_bill_value / (len(friends)-1), 2)
            for key in friends.keys():
                friends[key] = bill
            friends[lucky] = 0
        elif use_lucky == 'No':
            print("No one is going to be lucky")
        print(friends)


if __name__ == '__main__':
    main()

"""
What can be better than a cup of coffee during a break? A coffee that you don’t 
have to make yourself. It’s enough to press a couple of buttons on the machine and 
you get a cup of energy; but first, we should teach the machine how to do it. 
In this project, you will work on programming a coffee machine simulator. 
The machine works with typical products: coffee, milk, sugar, and plastic cups; 
if it runs out of something, it shows a notification. 
You can get three types of coffee: espresso, cappuccino, and latte. 
Since nothing’s for free, it also collects the money.
"""
class CoffeeMachine:
    def __init__(self) -> None:
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        # self.state = ""
    
    def _set_quantity(self, water: int, milk: int, beans: int, cups: int, money:  int) -> None:
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += money
    
    def __str__(self) -> str:
        output: str = ""
        output += "The coffee machine has:\n"
        output += f"{self.water} of water\n"
        output += f"{self.milk} of milk\n"
        output += f"{self.beans} of coffee beans\n"
        output += f"{self.cups} of disposable cups\n"
        output += f"${self.money} of money\n"
        return output
    
    def _take_money(self) -> None:
        print(f"I gave you ${self.money}\n")
        self.money = 0
    
    def _fill(self, water: int, milk: int, beans: int, cups: int) -> None:
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def _buy(self, coffee_type: int) -> None:
        if coffee_type == 1:
            if self._check_amount_espresso():
                self._set_quantity(250, 0, 16, 1, 4)
        elif coffee_type == 2:
            if self._check_amount_latte():
                self._set_quantity(350, 75, 20, 1, 7)
        elif coffee_type == 3:
            if self._check_amount_cappuccino():
                self._set_quantity(200, 100, 12, 1, 6)

    def _check_amount_espresso(self) -> bool:
        if self.water >= 250 and self.milk >= 75 and self.beans >= 16 and self.cups >= 1:
            print("I have enough resources, making you a coffee!\n")
            return True
        else:
            if self.water < 250:
                print("Sorry, not enough water!\n")
            if self.milk < 75:
                print("Sorry, not enough milk!\n")
            if self.beans < 16:
                print("Sorry, not enough coffee beans!\n")
            if self.cups < 1:
                print("Sorry, not enough cups!\n")
            return False

    def _check_amount_latte(self) -> bool:
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            print("I have enough resources, making you a coffee!\n")
            return True
        else:
            if self.water < 350:
                print("Sorry, not enough water!\n")
            if self.milk < 75:
                print("Sorry, not enough milk!\n")
            if self.beans < 20:
                print("Sorry, not enough coffee beans!\n")
            if self.cups < 1:
                print("Sorry, not enough cups!\n")
            return False

    def _check_amount_cappuccino(self) -> bool:
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            print("I have enough resources, making you a coffee!\n")
            return True
        else:
            if self.water < 200:
                print("Sorry, not enough water!\n")
            if self.milk < 100:
                print("Sorry, not enough milk!\n")
            if self.beans < 12:
                print("Sorry, not enough coffee beans!\n")
            if self.cups < 1:
                print("Sorry, not enough cups!\n")
            return False

    def run(self) -> None:
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            print()
            if action == "buy":
                coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
                print()
                if coffee_type == "back":
                    continue
                self._buy(int(coffee_type))
            elif action == "fill":
                water = int(input("Write how many ml of water do you want to add:\n"))
                milk = int(input("Write how many ml of milk do you want to add:\n"))
                beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
                cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
                self._fill(water, milk, beans, cups)
            elif action == "take":
                self._take_money()
            elif action == "remaining":
                print(self)
            elif action == "exit":
                break
            else:
                print("Wrong action!\n")


def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.run()


if __name__ == "__main__":
    main()
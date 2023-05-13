from random import randint
try:
    class BankAccount():
        def __init__(self, account_number, Money, balance):
            self.account_number = account_number
            self.Money = Money
            self.balance = balance

        def deposit(self):
            print(f"Your account number is {self.account_number}")
            print(f"You have topped up your account ${self.Money}")
            print(f"Your account balance is ${self.Money + self.balance}")

        def withdraw(self):
            if self.balance - self.Money >= 0:
                print(f"You have successfully cashed out ${self.Money}")
                print(f"Your account balance is ${self.balance - self.Money}")
            else:
                print("An error occurred\nInsufficient funds")

        def print_balance(self):
            print(f"Your account balance is ${self.balance}")


    account_number = int(input("Please enter your account number\n"))
    if account_number == 123456789:
         Transaction = input("Select the transaction\nTransaction deposit <<entre A>>"
                             "\nTransaction withdraw <<enter B>>"
                             "\nTransaction print_balance <<enter C>>\n")
        if Transaction == "A":
            Money = int(input("Please enter your MONEY\n"))
            balance = randint(0, 1000)
        elif Transaction == "B":
            Money = int(input("Please select the amount to withdraw\n"))
            balance = randint(0, 50000)
        elif Transaction == "C":
            Money = None
            balance = randint(0, 50000)
        else:
            print("An error occurred\nPlease start again")
        Customer = BankAccount(account_number, Money, balance)

        if Transaction == "A":
            Customer.deposit()
        elif Transaction == "B":
            Customer.withdraw()
        elif Transaction == "C":
            Customer.print_balance()
        else:
            print("An error occurred\nPlease start again")
    else:
        print("wrong account\nplease start again")
except ValueError:
        print("An error occurred\nPlease start again")

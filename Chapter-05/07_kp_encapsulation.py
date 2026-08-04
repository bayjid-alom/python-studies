class Bank:
    def __init__(self):
        self.__balance = 50000  # private variable

    def show_balance(self):
        print("Balance = ", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print(amount, "TK deposited")


# object make
b = Bank()

b.show_balance()

b.deposit(20000)

b.show_balance()


# print(b.__balance)  # Error❌ Private attribute

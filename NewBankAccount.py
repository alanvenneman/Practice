class NewBankAccount:
    def __init__(self):
        self.__balance = 0.0

    def create(self, initial_amount):
        account_File = open('bank_balance.txt', 'w')
        account_File.write(str(initial_amount))
        account_File.close()

    def deposit(self, amount):
        account_File = open('bank_balance.txt', 'w')
        account_File.write(str(self.__balance + amount))
        account_File.close()

    def withdraw(self, amount):
        account_File = open('bank_balance.txt', 'w')
        account_File.write(str(self.__balance - amount))
        account_File.close()

    def get_balance(self):
        account_File = open('bank_balance.txt', 'r')
        bal = float(account_File.readline().strip())
        self.__balance = bal

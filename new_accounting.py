from NewBankAccount import NewBankAccount


choice = int(input("Welcome! Choose 1 for create account, 2 for deposit and 3 for withdraw: "))
account1 = NewBankAccount()
if choice == 1:
    amount = float(input("Enter the opening deposit amount: "))
    account1.create(amount)
elif choice == 2:
    amount = float(input("Enter an amount for deposit: "))
    account1.get_balance()
    account1.deposit(amount)
elif choice == 3:
    amount = float(input("Enter an amount to withdraw: "))
    account1.get_balance()
    account1.withdraw(amount)
else:
    print("Wrong choice")

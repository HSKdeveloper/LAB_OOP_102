from bank_account import BankAccount

customer1 = BankAccount("Bora")
print(f"{customer1.get_account_holder()} is created and current balance account is: {customer1.get_balance()}")

customer1.depoist(15)
print(f"current amount of balance account is: {customer1.get_balance()}")

customer1.withdraw(5)
print(f"current amount of balance account is: {customer1.get_balance()}")

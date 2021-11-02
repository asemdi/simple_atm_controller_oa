from atm import ControllerATM
from atm import DEPOSIT, WITHDRAW, BALANCE

atm = ControllerATM()
atm.bank.createCard(1234, 1, "checking")
"""
I assume that the input will only be numerical, since there are only numbers on the ATM keyboard.
"""

while True:
    cardNumber = int(input("Please insert your card: "))
    pin = int(input("Please enter your pin: "))
    authenticated = atm.authenticate(cardNumber, pin)
    if authenticated:
        accountType = input("Please choose an account. For checking, enter C; for savings, enter S: ").upper()
        if atm.setAccount(accountType):
            while True:
                action = input("For depositing, enter D; for withdrawing, enter W; for seeing balance, enter B: ").upper()
                if action == DEPOSIT or action == WITHDRAW:
                    while True:
                        amount = int(input("Enter the amount: "))
                        if amount == 0:
                            print("Enter a valid amount")
                        else:
                            break
                    result, message = atm.execute(action, amount)
                    break
                elif action == BALANCE:
                    result, balance = atm.execute(action)
                    message = "Current balance: " + str(balance)
                    break
                else:
                    print("Invalid action")
            print(message)
            atm.current = None
        else:
            print("Account type does not exist")
        continue
        
    else:
        print("Card number and pin do not match")

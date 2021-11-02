DEPOSIT = "D"
WITHDRAW = "W"
BALANCE = "B"
ACCOUNT_TYPES = {
    "C": "checking",
    "S": "savings"
}

class Bank:
    def __init__(self):
        self.database = {}
    def checkPin(self, cardNumber, pin):
        if self.database[cardNumber]["pin"] == pin:
            return True
        else:
            return False
    def createCard(self, cardNumber, pin, accountType):
        if cardNumber in self.database:
            return False
        else:
            self.database[cardNumber] = { "pin": pin, "accounts": { accountType: 0 } }
            return True
    def addAccount(self, cardNumber, accountType):
        if cardNumber in self.database:
            self.database[cardNumber]["accounts"][accountType] = 0
            return True
        else:
            return False
    def deposit(self, cardNumber, accountType, amount):
        self.database[cardNumber]["accounts"][accountType] += amount
        return True
    def withdraw(self, cardNumber, accountType, amount):
        if self.database[cardNumber]["accounts"][accountType] < amount:
            return False
        self.database[cardNumber]["accounts"][accountType] -= amount
        return True
    def balance(self, cardNumber, accountType):
        return self.database[cardNumber]["accounts"][accountType]

class ControllerATM:
    def __init__(self):
        self.bank = Bank()
        self.current = None
        self.account = None
    def authenticate(self, cardNumber, pin):
        if cardNumber in self.bank.database and self.bank.checkPin(cardNumber, pin):
            self.current = cardNumber
            return True
        else:
            return False
    def setAccount(self, accountType):
        if accountType in ACCOUNT_TYPES and ACCOUNT_TYPES[accountType] in self.bank.database[self.current]["accounts"]:
            self.account = ACCOUNT_TYPES[accountType]
            return True
        else:
            return False
    def execute(self, action, amount = 0):
        if action == DEPOSIT:
            if self.bank.deposit(self.current, self.account, amount):
                return (True, "Deposit successful.")
        elif action == WITHDRAW:
            if self.bank.withdraw(self.current, self.account, amount):
                return (True, "Withdraw successful.")
            else:
                return (False, "FAIL: Not enough funds.")
        elif action == BALANCE:
            return (True, self.bank.balance(self.current, self.account))

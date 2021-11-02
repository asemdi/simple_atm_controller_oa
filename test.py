from atm import ControllerATM

atm = ControllerATM()
atm.bank.createCard(1234, 1, "checking")

assert atm.authenticate(1234, 1) == True
assert atm.authenticate(1234, 2) == False

assert atm.setAccount("C") == True
assert atm.setAccount("S") == False

assert atm.execute("D", 10)[0] == True
assert atm.execute("W", 10)[0] == True
assert atm.execute("W", 1)[0] == False
assert atm.execute("B")[0] == True
assert atm.execute("B")[1] == 0

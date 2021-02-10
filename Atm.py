class Atm(object):
    def __init__(self):
        self.cardNo=input("Enter your card number")
        self.pinNo=input("Enter you pin number")
        
    def CashWithdrawl(self):
        print("Cash Withdrawl")
    def BalanceEnquiry(self):
        print("Balance Enquiry")
atm=Atm()
print("Card Number: ",atm.cardNo)
print("Pin Number: ",atm.pinNo)

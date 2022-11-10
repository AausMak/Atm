class ATM(object):
    def __init__ (self,pin,acc_no,amount,card_type):
        self.pin=pin
        self.acc_no=acc_no
        self.amount=amount
        self.card_type=card_type
        
Aaus=ATM("1919","1011010","100000","Platinum")

print(Aaus.pin)

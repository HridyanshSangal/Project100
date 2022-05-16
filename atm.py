from types import new_class


class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def check_balance(self):
        print('Your balance is 50000')

    def withdrawal(self,amount):
        new_amount = 50000-amount
        print('You have withdrawn amount' +str(amount)+ '.Your remaining balance is' +str(new_amount))
def main():
    card_number = input('Insert your card number: ')
    pin_number  = input('Insert your pin number: ')
    new_user = Atm(card_number,pin_number)
    print('Choose your activity')
    print('1. Balance Inquiry 2. Withdrawal')
    activity = int(input('Enter Ativity number: '))
    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input('Enter the amount: '))
        new_user.withdrawal(amount)
    else:
        print('Enter a valid number')

if __name__ == '__main__':
    main()
/*
====================================================================
1. The program starts with an initial balance of ₹500 (minimum balance requirement).
                                                       
2. It imports custom exceptions: DepositError, WithdrawError, and InsufficientAmountError.

3. The deposit() function:
   * Takes user input for deposit amount.
   * Checks if the amount is greater than 0.
   * If valid, adds it to the balance.
   * Otherwise, raises DepositError.

4. The withdraw() function:
   * Takes user input for withdrawal amount.
   * Checks if the amount is greater than 0.
   * Ensures minimum balance of ₹500 is maintained after withdrawal.
   * If conditions fail, raises appropriate exceptions.
   * Otherwise, deducts the amount from balance.

5. The balance_inquiry() function:
   * Displays the current available balance.

6. The program uses global balance to update and track transactions across functions.

====================================================================
*/


from ATMException import DepositError,WithdrawError,InsufficientAmountError
balance=500.00  #Minimum amount requirement is Rs.500.00
def deposit():
    global balance
    deposit_amount=float(input("Enter Your Deposit Amount: "))
    if deposit_amount<=0:
        raise DepositError
    else:
        balance+=deposit_amount
    print(f"XYZ Bank a/c is credited with Rs.{deposit_amount}. Available Bal:{balance}")

def withdraw():
    global balance
    withdraw_amount=float(input("Enter Your Withdraw Amount: "))
    if withdraw_amount<=0:
        raise WithdrawError
    else :
        if ((withdraw_amount+500)>balance):
            raise InsufficientAmountError
        else:
            balance-=withdraw_amount
            print(f"Rs.{withdraw_amount} debited from XYZ Bank. Available Bal:{balance}")


def balance_inquiry():
    print(f"Available Balance:{balance}")

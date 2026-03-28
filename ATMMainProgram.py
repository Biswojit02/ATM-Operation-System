/*
=====================================================================
1. The program imports custom exceptions, menu function, and ATM operations (deposit, withdraw, balance inquiry).

2. It runs inside an infinite loop to continuously display ATM services until the user exits.

3. The menu() function is called to show available options to the user.

4. The user enters a choice, which is converted into an integer.

5. Using match-case:

   * Case 1: Calls deposit() function.
     * Handles DepositError for invalid amounts (zero or negative).
     * Handles ValueError for invalid input types.

   * Case 2: Calls withdraw() function.
     * Handles WithdrawError for invalid amounts.
     * Handles InsufficientAmountError if minimum balance (₹500) is violated.
     * Handles ValueError for invalid input types.

   * Case 3: Calls balance_inquiry() to display current balance.

   * Case 4: Displays exit message and breaks the loop.

   * Default case (_): Handles invalid menu choices.

6. The outer try-except block handles invalid input (non-numeric) for menu choice.

7. The program ensures safe execution by handling all possible user input errors and exceptions.

=====================================================================
*/


from ATMException import DepositError,WithdrawError,InsufficientAmountError
from ATMMenu import menu
from ATMOperation import deposit,withdraw,balance_inquiry
while True:
    try:
        menu()
        choice=int(input("Enter Your choice: "))
        match (choice):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("Don't enter Zero or -Ve values for Deposit Amount... Try again!")
                except ValueError:
                    print("Don't enter Alnums, Str & Symbols for Deposit amount... Try again!")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("Don't enter Zero or -Ve values for Withdraw amount... Try again!")
                except InsufficientAmountError:
                    print("Minimum amount requirement is Rs.500.00 for Your a/c of XYZ Bank")
                    print("Don't Enter an Exceed amount than Available amount for withdraw. Your a/c doesn't contains Sufficient fund that you are entered... Try Again")
                    
                except ValueError:
                    print("Don't enter Alnums, Str & Symbols for Withdraw amount... Try again!")
            case 3:
                balance_inquiry()
            case 4:
                print("Thank You... Visiting Again")
                break
            case _:
                print("Invalid Input... Try Again!")
        
    except ValueError:
        print("Don't enter Alphabets & Symbols for Choice... Try again!")


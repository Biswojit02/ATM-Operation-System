/*
====================================================================
This file defines 3 custom exception classes for an ATM system.
   
    - Raised when something goes wrong during deposit
    (e.g. depositing negative or zero amount)
    - Raised when something goes wrong during withdrawal
    (e.g. withdrawing invalid amount)
    - Raised when balance is not enough to withdraw
    (e.g. withdrawing ₹5000 when balance is ₹1000)

===================================================================
*/


class DepositError(Exception):pass
class WithdrawError(Exception):pass
class InsufficientAmountError(Exception):pass

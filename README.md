# 🏧 ATM Operation System — Python

A console-based ATM simulation built with Python that demonstrates
**custom exception handling**, **modular programming**, and
**real-world banking logic**.

---

## 📁 Project Structure

ATM-Operation-System/
├── ATMException.py       # Custom Exception Classes
├── ATMMenu.py            # ATM Menu Display
├── ATMOperation.py       # Core Banking Operations
└── ATMMainProgram.py     # Main Driver Program

---

## ⚙️ Features

- 💰 **Deposit** — Add funds to your account with input validation
- 🏧 **Withdraw** — Withdraw funds with minimum balance enforcement
- 📊 **Balance Inquiry** — Check current available balance
- 🚪 **Exit** — Safely exit the ATM session
- 🔒 **Minimum Balance** — Rs.500 must be maintained at all times
- ⚠️ **Custom Exceptions** — Meaningful error messages for every case
- 🔁 **Continuous Loop** — Runs until user chooses to exit

---

## 🧩 Module Breakdown

### 1. `ATMException.py`
Defines three custom exception classes:

| Exception | Triggered When |
|---|---|
| `DepositError` | Deposit amount is zero or negative |
| `WithdrawError` | Withdraw amount is zero or negative |
| `InsufficientAmountError` | Withdrawal exceeds balance minus Rs.500 |

---

### 2. `ATMMenu.py`
Displays the ATM menu with 4 options:
- 1 → Deposit
- 2 → Withdraw
- 3 → Balance Inquiry
- 4 → Exit

---

### 3. `ATMOperation.py`
Contains three core functions:

**`deposit()`**
- Takes deposit amount as input
- Raises `DepositError` if amount ≤ 0
- Adds amount to global balance

**`withdraw()`**
- Takes withdrawal amount as input
- Raises `WithdrawError` if amount ≤ 0
- Raises `InsufficientAmountError` if
  (withdraw + 500) > balance
- Deducts amount from global balance

**`balance_inquiry()`**
- Displays current available balance

---

### 4. `ATMMainProgram.py`
- Main driver using `while True` loop
- Uses `match-case` (Python 3.10+) for menu selection
- Handles all exceptions gracefully with user-friendly messages

---

## 🚀 How to Run

**Step 1 — Clone the repository**
git clone https://github.com/Biswojit02/ATM-Operation-System.git

**Step 2 — Navigate to the folder**
cd ATM-Operation-System

**Step 3 — Run the main program**
python ATMMainProgram.py

> ⚠️ Requires Python 3.10+ (for match-case support)

---

## ⚠️ Exception Handling Coverage

| Scenario | Exception Handled |
|---|---|
| Deposit amount = 0 or negative | `DepositError` |
| Withdraw amount = 0 or negative | `WithdrawError` |
| Withdraw exceeds balance - 500 | `InsufficientAmountError` |
| Entering letters for amount | `ValueError` |
| Entering letters for menu choice | `ValueError` |
| Invalid menu choice number | `case _` default |

---

## 🛠️ Tech Stack

- **Language** — Python 3.10+
- **Concepts Used** — Custom Exceptions, Modular Programming,
  Global Variables, Match-Case, Exception Handling, Loops

---

## 📌 Key Concepts Demonstrated

- ✅ Custom Exception Classes (`Exception` subclassing)
- ✅ Modular code split across multiple files
- ✅ `match-case` statement (Python 3.10+)
- ✅ `global` variable usage
- ✅ Nested `try-except` blocks
- ✅ Real-world banking constraint (minimum balance)
- ✅ Input validation for all user entries

---

## 📜 License

This project is open source and available under the
[MIT License](LICENSE).

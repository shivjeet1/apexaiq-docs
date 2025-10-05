import datetime

class EmptyFundsError(Exception):
    def __init__(self, balance, a_to_withdraw):
        self.balance = balance
        self.a_to_withdraw=a_to_withdraw

        super().__init__(
        f"Withdrawal Failed: Attempted to withdraw {a_to_withdraw}, but only {balance} is available."
        )

class Money:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Money value must be a number.")
        if value < 0:
            raise ValueError("Money value cannot be negative.")
        self._value = float(value)

    def get_value(self):
        return self._value

    def __str__(self):
        return f"${self._value:,.2f}"

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self._value +other.get_value())

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self._value -other.get_value())

    def __lt__(self,other):
        if not isinstance(other, Money):
            return NotImplemented
        return self._value <other.get_value()

class AccountHolder:
    def __init__(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Account holder name must be a non-empth string.")
        self._name = name

    def __str__(self):
        return self._name

class TransactionLogger:
    def __init__(self, filename):
        self._filename = filename
        self._file_handle = open(self._filename, 'a', encoding='utf-8')
        self.log(f"--- Log Session Started: {datetime.datetime.now():%Y-%m-%d %H:%M:%S} ---")


    def log(self, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        self._file_handle.write(log_entry + '\n')
        self._file_handle.flush()

    def close(self):
        self.log("--- Log Session Ended --")
        self._file_handle.close()

class BankAccount:
    def __init__(self, owner_obj, initial_bal_obj, logger_object):
        self._owner = owner_obj
        self._balance = initial_bal_obj
        self._logger = logger_object
        self._logger.log(f"Account created for '{self._owner}' with initial balance of {self._balance}.")

    def deposit(self, amount_obj):
        if not isinstance(amount_obj, Money):
            self._logger.log("ERROR: Deposit amount must be a Money Object.")
            return
        self._balance = self._balance + amount_obj
        self._logger.log(f"Deposit successful, Amount: {amount_obj}, New Balance: {self._balance}.")


    def withdraw(self, amount_object):
        if not isinstance(amount_object, Money):
            self._logger.log("ERROR: Withdrawal amount must be a Money object.")
            return

        if amount_object < self._balance or amount_object.get_value() == self._balance.get_value():
            self._balance = self._balance - amount_object
            self._logger.log(f"Withdrawal successful. Amount: {amount_object}. New Balance: {self._balance}.")
        else:
            self._logger.log(f"ALERT: Insufficient funds for withdrawal of {amount_object}.")
            raise EmptyFundsError(self._balance, amount_object)

    def check_balance(self):
        """Logs the current account balance."""
        self._logger.log(f"Balance check for '{self._owner}': {self._balance}")
        return self._balance

if __name__ == "__main__":
    output_filename="bankop.txt"
    logger=TransactionLogger(output_filename)

    try:
        account_holder = AccountHolder("Shivam Lavhale")
        initial_deposit = Money(10000)
        my_account = BankAccount(account_holder, initial_deposit, logger)

        my_account.check_balance()

        logger.log("\n--- Performing a deposit ---")
        deposit_amount = Money(1500)
        my_account.deposit(deposit_amount)

        logger.log("\n--- Attempting a withdrawal with insufficient funds ---")
        overdraft_amount = Money(2000)
        my_account.withdraw(overdraft_amount)

    except (EmptyFundsError, ValueError, TypeError) as e:
        logger.log(f"OPERATION HALTED DUE TO ERROR: {e}")

    finally:
        logger.log("\nAll Operations Completed successfully")
        logger.close()
        print(f"\nFull transaction log has been saved to '{output_filename}'")




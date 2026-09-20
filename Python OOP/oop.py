# Static vs Instance Method Example

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self._log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def _is_valid_amount(self, amount):
        return amount > 0 

    def _log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New Balance: ${self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5 


account = BankAccount("Alice", 500)
account.deposit(200)


        
        
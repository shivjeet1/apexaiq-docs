import re

class Value:
    def __init__(self, original_input: str):
        self._original = str(original_input)
        
        processed_str = self._original.lower()
        self._sanitized = "".join(re.findall("[a-z0-9]", processed_str))

    def is_palindrome(self) -> bool:
        return self._sanitized == self._sanitized[::-1]

    def __str__(self) -> str:
        return f"'{self._original}'"

class Result:
    def __init__(self, outcome: bool):
        self._outcome = outcome

    def __str__(self) -> str:
        if self._outcome:
            return "is a Palindrome"
        else:
            return "is NOT a Palindrome"

class Checker:
    def check(self, val_obj: Value):
        outcome = val_obj.is_palindrome()
        return Result(outcome)

def main():
    print("--- Interactive Palindrome Checker ---")
    print("(Enter 'exit' or 'quit' to stop)")
    checker = Checker()

    while True:
        user_input = input("\nEnter a string or number to check: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting application.")
            break
        
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        try:
            value_to_check = Value(user_input)
            check_result = checker.check(value_to_check)
            
            print(f"Result: The input {value_to_check} {check_result}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

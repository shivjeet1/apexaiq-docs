
class Num:
    def __init__(self, val: int):
        if not isinstance(val, int):
            raise TypeError("Num can only be initialized with an integer.")
        self._val = val

    def get_val(self) -> int:
        return self._val

    def __str__(self) -> str:
        return str(self._val)

    def __add__(self, other):
        if not isinstance(other, Num):
            return NotImplemented
        new_val = self._val + other.get_val()
        return Num(new_val)

class Fibonacci:
    def __init__(self, terms: Num):
        if not isinstance(terms, Num) or terms.get_val() < 0:
            raise ValueError("Number of terms must be a non-negative Num object.")
        self._terms = terms
        self._sequence = []

    def generate(self):
        self._sequence = []
        limit = self._terms.get_val()

        if limit == 0:
            return

        a = Num(0)
        self._sequence.append(a)
        
        if limit == 1:
            return

        b = Num(1)
        self._sequence.append(b)

        for _ in range(2, limit):
            next_val = a + b
            self._sequence.append(next_val)
            a = b
            b = next_val
            
    def display(self):
        seq_str = ", ".join([str(num_obj) for num_obj in self._sequence])
        print(f"Fibonacci sequence with {self._terms} terms:")
        print(f"-> [ {seq_str} ]")

def main():
    print("--- Interactive Fibonacci Series Generator ---")
    print("(Enter a non-negative integer, or 'exit'/'quit' to stop)")

    while True:
        user_input = input("\nEnter the number of terms to generate: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting application.")
            break
        
        try:
            # First, validate the input as a standard integer
            num_val = int(user_input)
            if num_val < 0:
                print("Error: Please enter a non-negative number.")
                continue

            # If valid, create the required Num object
            terms_obj = Num(num_val)
            
            # Create the generator and run the process
            fib_gen = Fibonacci(terms_obj)
            fib_gen.generate()
            fib_gen.display()

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except TypeError as e:
            # This catches errors from the class constructors
            print(f"An internal error occurred: {e}")

if __name__ == "__main__":
    main()



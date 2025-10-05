import datetime

class Dimension:
    def __init__(self, val: int):
        if not isinstance(val, int) or val <= 0:
            raise ValueError("Dimension must be a positive integer.")
        self._val = val

    def get_val(self) -> int:
        return self._val

    def __str__(self) -> str:
        return str(self._val)

class Symbol:
    def __init__(self, char: str):
        if not isinstance(char, str) or len(char) != 1:
            raise TypeError("Symbol must be a single character string.")
        self._char = char

    def __str__(self) -> str:
        return self._char

    def __mul__(self, count: int):
        if not isinstance(count, int):
            return NotImplemented
        return self._char * count

class Pattern:
    def __init__(self, pattern_str: str):
        self._pattern_str = pattern_str

    def __str__(self) -> str:
        return self._pattern_str

class PatternWriter:
    def __init__(self, filename: str):
        self._filename = filename
        self._file_handle = open(self._filename, 'a', encoding='utf-8')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._file_handle.write(f"\n--- New Session: {timestamp} ---\n")
        self._file_handle.flush()

    def write(self, title: str, pattern_obj: Pattern):
        content = f"{title}\n{str(pattern_obj)}\n"
        self._file_handle.write(content)
        self._file_handle.flush()

    def get_filename(self) -> str:
        return self._filename

    def close(self):
        self._file_handle.close()

class PyramidDrawer:
    @staticmethod
    def draw(dim_obj: Dimension, sym_obj: Symbol, space_sym: Symbol):
        rows = dim_obj.get_val()
        lines = []
        for i in range(rows):
            spaces = space_sym * (rows - i - 1)
            symbols = sym_obj * (2 * i + 1)
            lines.append(f"{spaces}{symbols}")
        return Pattern("\n".join(lines))

class TriangleDrawer:
    @staticmethod
    def draw(dim_obj: Dimension, sym_obj: Symbol):
        rows = dim_obj.get_val()
        lines = []
        for i in range(1, rows + 1):
            symbols = sym_obj * i
            lines.append(symbols)
        return Pattern("\n".join(lines))

class AlphabetDrawer:
    @staticmethod
    def draw(dim_obj: Dimension):
        rows = dim_obj.get_val()
        lines = []
        for i in range(rows):
            line_str = ""
            for j in range(i + 1):
                line_str += chr(ord('A') + j)
            lines.append(line_str)
        return Pattern("\n".join(lines))

class SquareDrawer:
    @staticmethod
    def draw(dim_obj: Dimension, sym_obj: Symbol):
        size = dim_obj.get_val()
        lines = []
        line = sym_obj * size
        for _ in range(size):
            lines.append(line)
        return Pattern("\n".join(lines))

class DiamondDrawer:
    @staticmethod
    def draw(dim_obj: Dimension, sym_obj: Symbol, space_sym: Symbol):
        rows = dim_obj.get_val()
        lines = []
        for i in range(rows):
            spaces = space_sym * (rows - i - 1)
            symbols = sym_obj * (2 * i + 1)
            lines.append(f"{spaces}{symbols}")
        for i in range(rows - 2, -1, -1):
            spaces = space_sym * (rows - i - 1)
            symbols = sym_obj * (2 * i + 1)
            lines.append(f"{spaces}{symbols}")
        return Pattern("\n".join(lines))

def get_dimension_input():
    while True:
        try:
            val = int(input("Enter the size (e.g., number of rows): "))
            return Dimension(val)
        except (ValueError, TypeError) as e:
            print(f"Invalid input. {e}. Please try again.")

def main():
    print("--- OOP Pattern Generator ---")
    writer = PatternWriter("pattern.txt")
    star_obj = Symbol('*')
    space_obj = Symbol(' ')

    try:
        while True:
            print("\n" + "="*30)
            print("Select a pattern to draw:")
            print("  1. Pyramid\n  2. Star Triangle\n  3. Alphabet Triangle\n  4. Square\n  5. Diamond\n  6. Exit")
            print("="*30)
            choice = input("Enter your choice (1-6): ")

            if choice in ["6", "exit", "quit"]:
                break
            
            if choice not in ["1", "2", "3", "4", "5"]:
                print("Invalid choice. Please select a valid option.")
                continue
                
            try:
                dim_obj = get_dimension_input()
                pattern_result = None

                if choice == '1':
                    pattern_result = PyramidDrawer.draw(dim_obj, star_obj, space_obj)
                elif choice == '2':
                    pattern_result = TriangleDrawer.draw(dim_obj, star_obj)
                elif choice == '3':
                    pattern_result = AlphabetDrawer.draw(dim_obj)
                elif choice == '4':
                    pattern_result = SquareDrawer.draw(dim_obj, star_obj)
                elif choice == '5':
                    pattern_result = DiamondDrawer.draw(dim_obj, star_obj, space_obj)
                
                title = f"--- Pattern '{choice}' of size {dim_obj} ---"
                writer.write(title, pattern_result)
                print(f"\nPattern successfully saved to '{writer.get_filename()}'")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")
    finally:
        print("Exiting application.")
        writer.close()

if __name__ == "__main__":
    main()


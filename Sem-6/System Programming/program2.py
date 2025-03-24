class SymbolTable:
    def __init__(self):
        self.table = set()  # Using a set for O(1) lookup and insertion

    def is_lexeme_present(self, lexeme):
        """Check if the lexeme is already in the symbol table."""
        return lexeme in self.table

    def insert_lexeme(self, lexeme):
        """Insert a lexeme if it is not already present."""
        if self.is_lexeme_present(lexeme):
            print(f"Lexeme '{lexeme}' is already present in the symbol table.")
            return False
        else:
            self.table.add(lexeme)
            print(f"Lexeme '{lexeme}' inserted into the symbol table.")
            return True

    def display_table(self):
        """Display all lexemes stored in the symbol table."""
        print("Symbol Table:", self.table)


# Example usage
if __name__ == "__main__":
    symbol_table = SymbolTable()

    symbol_table.insert_lexeme("x")
    symbol_table.insert_lexeme("y")
    symbol_table.insert_lexeme("x")  # Duplicate, should not be added again

    symbol_table.display_table()

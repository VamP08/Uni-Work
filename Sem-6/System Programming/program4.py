
class TwoPassAssembler:
    def __init__(self):
        self.symbol_table = {}  
        self.opcode_table = {   
            "LDA": "00",
            "STA": "01",
            "ADD": "02",
            "SUB": "03",
            "MUL": "04",
            "DIV": "05",
            "JMP": "06",
            "JNZ": "07",
            "HLT": "08"
        }
        self.location_counter = 0  
        self.intermediate_code = [] 
        self.machine_code = []  

    def pass_one(self, code):
        """First pass: Build symbol table and intermediate code."""
        for line in code:
            tokens = line.strip().split()
            if not tokens or tokens[0].startswith("#"): 
                continue

            if tokens[0].endswith(":"):
                label = tokens[0][:-1]
                self.symbol_table[label] = self.location_counter  
                tokens.pop(0)  

            if tokens:  # Process instruction
                self.intermediate_code.append((self.location_counter, tokens))
                self.location_counter += 1

    def pass_two(self):
        """Second pass: Generate machine code using symbol table."""
        for address, tokens in self.intermediate_code:
            mnemonic = tokens[0]
            operand = tokens[1] if len(tokens) > 1 else None

            if mnemonic in self.opcode_table:
                opcode = self.opcode_table[mnemonic]
                operand_address = f"{self.symbol_table.get(operand, 'XX'):02d}" if operand else "00"
                instruction = f"{opcode} {operand_address}"
                self.machine_code.append(f"{address:02d} {instruction}")
            else:
                print(f"Error: Unknown instruction '{mnemonic}'")

    def display(self):
        """Displays the machine code and symbol table."""
        print("\nGenerated Machine Code:")
        for line in self.machine_code:
            print(line)

        print("\nSymbol Table:")
        for label, address in self.symbol_table.items():
            print(f"{label}: {address}")

assembly_code = [
    "START:",
    "LDA A",
    "ADD B",
    "STA C",
    "JNZ START",
    "HLT",
    "A: 10",
    "B: 20",
    "C: 00"
]

assembler = TwoPassAssembler()
assembler.pass_one(assembly_code)
assembler.pass_two() 
assembler.display()  

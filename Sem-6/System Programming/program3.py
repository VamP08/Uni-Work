class OnePassAssembler:
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
        self.machine_code = [] 

    def assemble(self, code):
        """
        Process each line of assembly code and generate machine code.
        """
        for line in code:
            tokens = line.strip().split()  
            if not tokens or tokens[0].startswith("#"):  
                continue

            if tokens[0].endswith(":"):  
                label = tokens[0][:-1]
                self.symbol_table[label] = self.location_counter
                tokens.pop(0)  

            if tokens:  
                mnemonic = tokens[0]
                operand = tokens[1] if len(tokens) > 1 else None

                if mnemonic in self.opcode_table:
                    opcode = self.opcode_table[mnemonic]
                    operand_address = self.symbol_table.get(operand, "XX") if operand else "00"
                    instruction = f"{opcode} {operand_address}"
                    self.machine_code.append(f"{self.location_counter:02d} {instruction}")
                    self.location_counter += 1
                else:
                    print(f"Error: Unknown instruction '{mnemonic}'")

    def display(self):
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

assembler = OnePassAssembler()
assembler.assemble(assembly_code)
assembler.display()

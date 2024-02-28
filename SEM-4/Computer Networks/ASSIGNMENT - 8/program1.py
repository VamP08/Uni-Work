def main():
    # Take input from the user
    size = int(input("Enter the size of data: "))
    data = list(map(int, input("Enter the data bits (space-separated): ").split()))
    divisor = list(map(int, input("Enter the divisor bits (space-separated): ").split()))
    
    # Call sender function
    code = sender(data, divisor)
    # Call receiver function
    receiver(code, divisor)

def sender(data, div):
    # Append n-1 zeroes to the data array
    data += [0] * (len(div) - 1)
    remainder = divide(data, div)
    size = len(div)
    # Replace the extra 0's with remainder values
    code = data[:size] + remainder
    return code

def receiver(code, div):
    remainder = divide(code, div)
    
    # Check if remainder is all zeros
    if all(bit == 0 for bit in remainder):
        print("Data is Correct")
    else:
        print("Data is Corrupted")

def divide(data, div):
    # Initialize remainder with first n bits of data
    remainder = data[:len(div)]
    
    # Loop through the data
    for i in range(len(data) - len(div) + 1):
        # Perform XOR operation
        if remainder[0] == 1:
            for j in range(len(div)):
                remainder[j] = remainder[j] ^ div[j]
        else:
            for j in range(len(div)):
                remainder[j] = remainder[j] ^ 0
        
        # Shift remainder to the right
        if i != len(data) - len(div):
            remainder = remainder[1:] + [data[i + len(div)]]
    
    return remainder[1:]

main()

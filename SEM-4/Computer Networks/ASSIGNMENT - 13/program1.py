def find_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])
    
    if first_octet >= 1 and first_octet <= 126:
        return "Class A address"
    elif first_octet >= 128 and first_octet <= 191:
        return "Class B address"
    elif first_octet >= 192 and first_octet <= 223:
        return "Class C address"
    elif first_octet >= 224 and first_octet <= 239:
        return "Class D address"
    elif first_octet >= 240 and first_octet <= 255:
        return "Class E address"
    else:
        return "Invalid IP address"

def convert_to_binary(ip_address):
    binary_octets = []
    for octet in ip_address.split('.'):
        binary_octets.append(format(int(octet), '08b'))
    return ' '.join(binary_octets)

def convert_to_hex(ip_address):
    hex_octets = []
    for octet in ip_address.split('.'):
        hex_octets.append(format(int(octet), '02X'))
    return ' '.join(hex_octets)

ip_address = input("Write down address in Dotted Decimal Notation: ")
ip_class = find_ip_class(ip_address)
print("Class of the IP address:", ip_class)

binary_address = convert_to_binary(ip_address)
print("Address in Binary is:")
print(binary_address)

hex_address = convert_to_hex(ip_address)
print("\nAddress in Hexadecimal is:", hex_address)

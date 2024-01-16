def string_to_binary(input_string):
    binary_list = [format(ord(char), '08b') for char in input_string]
    return binary_list

def calculate_parity(bits):
    parity = bits.count('1') % 2
    return parity

def add_parity_bit(frame):
    frame_with_parity = []
    for bits in frame:
        parity_bit = calculate_parity(bits)
        frame_with_parity.append(bits + str(parity_bit))
    return frame_with_parity

def calculate_lrc(frame_with_parity):
    lrc = ['0' for _ in range(8)]

    print("Frame before Padding:")
    for bits in frame_with_parity:
        print(" ".join(bits))
        for i in range(8):
            lrc[i] = str((int(lrc[i]) + int(bits[i])) % 2)

    print("\nFrame to be sent:", "  ".join(frame_with_parity))
    lrc_result = ''.join(lrc)
    print(f"LRC for '{input_name}' is '{lrc_result}' (Note: {lrc_result} is ASCII for character {chr(int(lrc_result, 2))} in Binary)")

input_name = "PRATHAM"
binary_frame = string_to_binary(input_name)
print("Frame before Padding:", " ".join(binary_frame))

frame_with_parity = add_parity_bit(binary_frame)

calculate_lrc(frame_with_parity)

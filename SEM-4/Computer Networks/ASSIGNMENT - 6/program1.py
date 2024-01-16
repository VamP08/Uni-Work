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

def vrc_error_detection(input_string):
    binary_frame = string_to_binary(input_string)
    print("Frame before Padding:", " ".join(binary_frame))

    frame_with_parity = add_parity_bit(binary_frame)
    print("Frame after Padding using VRC:", "  ".join(frame_with_parity))

input_name = "PRATHAM"
vrc_error_detection(input_name)

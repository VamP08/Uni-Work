def bit_stuffing(frame):
    stuffed_frame = []
    count = 0
    for bit in frame:
        if bit == '1':
            count += 1
        else:
            count = 0
        stuffed_frame.append(bit)
        if count == 5:
            stuffed_frame.append('0')
            count = 0
    return ''.join(stuffed_frame)

frame = input("Enter the bit frame: ")

print( "->" ,bit_stuffing(frame))
def stuff(frame, FLAG, ESC):
    stuffed_frame = []
    for char in frame:
        if char == FLAG or char == ESC:
            stuffed_frame.append(ESC)
        stuffed_frame.append(char)
    return [FLAG] + stuffed_frame + [FLAG]

frame = input("Enter the unstuffed frame as a list of characters: ")
FLAG = input("Enter     the character for FLAG: ")
ESC = input("Enter the character for ESC: ")

print(stuff(eval(frame), FLAG, ESC))

def stuff(frame, FLAG, ESC):
    stuffed_frame = []
    for char in frame:
        if char == FLAG or char == ESC:
            stuffed_frame.append(ESC)
        stuffed_frame.append(char)
    return [FLAG] + stuffed_frame + [FLAG]

frame = input("Enter the unstuffed frame as a list of characters: ")
FLAG = input("Enter the character for FLAG: ")
ESC = input("Enter the character for ESC: ")

print(stuff(eval(frame), FLAG, ESC))
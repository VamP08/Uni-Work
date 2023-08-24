import random
import string

def random_color_hex():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color

def random_alphabetical_string(length):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

def random_value_between(min_value, max_value):
    return random.randint(min_value, max_value)

def random_multiple_of_seven():
    return random.randint(0, 10) * 7

random_hex_color = random_color_hex()
random_string = random_alphabetical_string(10)  
random_int = random_value_between(1, 100)  
random_multiple = random_multiple_of_seven()

print("Random Color Hex Code:", random_hex_color)
print("Random Alphabetical String:", random_string)
print("Random Integer between 1 and 100:", random_int)
print("Random Multiple of 7 between 0 and 70:", random_multiple)

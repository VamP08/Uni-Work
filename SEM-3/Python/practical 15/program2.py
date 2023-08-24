import random
import os

def random_from_list(input_list):
    return random.choice(input_list)

def random_from_set(input_set):
    return random.choice(list(input_set))

def random_from_dict(input_dict):
    key = random.choice(list(input_dict.keys()))
    value = input_dict[key]
    return key, value

def random_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return random.choice(lines)

my_list = [1, 2, 3, 4, 5]
my_set = {10, 20, 30, 40, 50}
my_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry', 'd': 'date', 'e': 'elderberry'}

directory_path = './'

random_element_list = random_from_list(my_list)
print("Random element from list:", random_element_list)

random_element_set = random_from_set(my_set)
print("Random element from set:", random_element_set)

random_key, random_value = random_from_dict(my_dict)
print("Random key-value pair from dictionary:", random_key, "->", random_value)

files_in_directory = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

if files_in_directory:
    random_file_name = random.choice(files_in_directory)
    random_file_path = os.path.join(directory_path, random_file_name)
    random_line = random_from_file(random_file_path)
    print("Random line from a random file:", random_line)
else:
    print("No files found in the directory.")

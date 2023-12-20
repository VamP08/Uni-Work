def convert_case_and_remove_duplicates(input_sequence):

    lowercase_sequence = list(map(str.lower, input_sequence))
    unique_sequence = list(set(lowercase_sequence))
    
    uppercase_sequence = list(map(str.upper, unique_sequence))
    return uppercase_sequence + unique_sequence

input_sequence = ['a', 'A', 'b', 'B', 'c', 'C', 'a', 'A', 'b', 'B', 'c', 'C']
print(convert_case_and_remove_duplicates(input_sequence))

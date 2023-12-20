def convert_to_list(input_tuple):
    new_list = []
    for item in input_tuple:
        if isinstance(item, str):
            new_list.append(int(item))
        else:
            new_list.append(item)
    return new_list


tuple_example = (1, '2', 3, '4', 5)

print(convert_to_list(tuple_example))
def convert_to_string(int_list, int_tuple):
    str_list = list(map(str, int_list))

    str_tuple = list(map(str, int_tuple))

    combined_list = str_list + str_tuple

    return combined_list

int_list = [1, 2, 3]
int_tuple = (4, 5, 6)

print(convert_to_string(int_list, int_tuple))
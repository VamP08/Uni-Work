def display_numbers(group):
    even_numbers = list(filter(lambda x: x % 2 == 0, group))
    odd_numbers = list(filter(lambda x: x % 2 != 0, group))

    print("Number of Even Numbers: ", len(even_numbers))
    print("Number of Odd Numbers: ", len(odd_numbers))
group = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
display_numbers(group)
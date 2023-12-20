list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result_list = list(map(lambda x, y: x + y, list1, list2))

result_difference = list(map(lambda x, y: x - y, list1, list2))

print("Result List:", result_list)
print("Result Difference:", result_difference)
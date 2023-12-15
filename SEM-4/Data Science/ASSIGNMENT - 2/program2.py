def is_even(num):
    return num % 2 == 0

l = [11, 1, 20, 50, 5, 40]

print("Even numbers using for loop and User-defined function:")
for i in range(len(l)):
    if is_even(l[i]):
        print(l[i])

even_numbers = list(filter(lambda x: x % 2 == 0, l))

print("\nEven numbers using filter and lambda:")
for number in even_numbers:
    print(number)

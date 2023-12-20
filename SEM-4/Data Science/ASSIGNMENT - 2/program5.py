lst = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

squared_list = list(map(square, lst))

print(squared_list)
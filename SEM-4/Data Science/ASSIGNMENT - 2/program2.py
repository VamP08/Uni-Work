def compute(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")

    if not all(isinstance(i, int) for i in lst):
        raise ValueError("All elements in the list must be integers")
    
    square = lambda x: x ** 2

    cube = lambda x: x ** 3
    
    result = [(square(i), cube(i)) for i in lst]
    
    return result

lst = [1, 2, 3, 4, 5]
print(compute(lst))

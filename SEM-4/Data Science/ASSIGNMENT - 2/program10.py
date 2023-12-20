def compute_square_of_first_n_fibonacci_numbers(n):
    fibonacci_numbers = [0, 1]

    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])

    square_of_fibonacci_numbers = list(map(lambda x: x ** 2, fibonacci_numbers))

    return square_of_fibonacci_numbers

n = 10
result = compute_square_of_first_n_fibonacci_numbers(n)
print("The square of the first", n, "Fibonacci numbers is:", result)


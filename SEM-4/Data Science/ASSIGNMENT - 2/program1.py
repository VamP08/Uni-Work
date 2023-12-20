def multiply_with_unknown(number):
    try:
        value = float(number)
        result = value * 5

        print(f"The result of the multiplication is: {result}")
    except ValueError:
        print("Please provide a valid number.")

multiply_with_unknown(4)
multiply_with_unknown('A')
multiply_with_unknown(2.5)
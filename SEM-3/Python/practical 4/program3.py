#3)
i=input("Enter the character: ")

if i.isupper():
    print(i," is a UpperCase Character")
elif i.islower():
    print(i," is a LowerCase Character")
elif i.isdigit():
    print(i," is a Number")
else:
    print(i," is a Special Character")
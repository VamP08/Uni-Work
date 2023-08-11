#1)
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))

print("Operation available: \nAddition : +\nSubtraction : -\nMultiplication : *\nDivision : /\nFloor Division : //\nExponential : **\nModulus : %")
op=input("Enter the Operation you want to perform: ")

if op=="+":
    print("Addition = ",n1+n2)
elif op=="-":
    print("Subtraction = ",n1-n2)
elif op=="*":
    print("Multiplition = ",n1*n2)
elif op=="/":
    print("Division = ",n1/n2)
elif op=="//":
    print("Floor Division = ",n1//n2)
elif op=="**":
    print("Exponential = ",n1**n2)
elif op=="%":
    print("Modulus = ",n1%n2)

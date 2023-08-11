import random

l=[0,1,2,3,4,5,6,7,8,9,10]
num=random.choice(l)
ans=int(input("Enter your guess (0,10) : "))

if ans==num:
    print("Lucky guess correct ans")
else:
    print("Wrong choice guess again.")
    if num%2==0:
        print("Number is an even number.")
        ans=int(input("Enter your guess (0,10) : "))
        if num==ans:
            print("Correct answer. Number was ",num)
        else:
            print("Wrong Again, Thanks for Playing.")
    else:
        print("Number is an odd number.")
        ans=int(input("Enter your guess (0,10) : "))
        if num==ans:
            print("Correct answer. Number was ",num)
        else:
            print("Wrong Again, Thanks for Playing.")
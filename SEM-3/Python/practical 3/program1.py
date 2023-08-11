#1)
marks=0
i=0
while i<5:
    n=int(input("Enter marks of subjects: "))
    marks+=n
    i+=1
marks/=5
if marks>=60:
    print("Your Grade is A")
elif 40<marks<60:
    print("Your Grade is B")
else:
    print("Your Grade is C")
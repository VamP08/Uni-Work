from array import *

arr1= array('i')
for i in range(5):
    arr1.append(int(input("Enter array element: ")))
num=int(input("Enter the number for occurance count: "))

c=arr1.count(num)
print("\nArray :")

for i in range(5):
    print(arr1[i],end=" ")
print("\nNumber of occurance of",num,"=",c)
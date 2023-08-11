from array import *

arr1= array('i',[0,0,0,0,0])
for i in range(5):
    arr1[i]=int(input("Enter array element: "))

print("\nArray: ")
for i in range(5):
    print(arr1[i],end=" ")
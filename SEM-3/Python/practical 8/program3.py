from array import *

arr1= array('i')
for i in range(5):
    arr1.append(int(input("Enter array element: ")))

arr1.reverse()
for i in range(5):
    print(arr1[i],end=" ")
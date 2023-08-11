list=[1,2,3,4,5]
print("List before modification : ",list)
temp=list[-1]
list[-1]=list[0]
list[0]=temp
print("List after modification : ",list)

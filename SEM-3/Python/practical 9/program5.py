list=[]
n=int(input("Enter the length of list: "))
for i in range(n):
    num=int(input("Enter the element: "))
    list.append(num)
print("List: ",list)
print("Smallest element in list:",min(list))
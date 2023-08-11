list=[]
n=int(input("Enter the length of list: "))
for i in range(n):
    num=int(input("Enter the element: "))
    list.append(num)

print("List: ",list)
print("Largest element in list:",max(list))
print("Count of Largest element in list:",list.count(max(list)))

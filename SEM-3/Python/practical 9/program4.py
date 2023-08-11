list=[]
n=int(input("Enter the length of list: "))
for i in range(n):
    num=int(input("Enter the element: "))
    list.append(num)

print("List before reversing:",list)
list.reverse()
print("List after reversing:",list)
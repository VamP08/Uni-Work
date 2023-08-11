str=input("Enter Your String: ")
key=input("Enter the character you want to slice at: ")
i=0
while(True):
    if str[i]==key:
        str=str[0:i:]
        print(str)
        break
    if i==len(str):
        print("Character does not exist in string")
        break
    else:
        i+=1
        continue
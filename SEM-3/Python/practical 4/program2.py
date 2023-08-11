#2)
l=[1,3,5,6,99,134,55]
ECount,OCount=0,0

for i in range(len(l)):
    if l[i]%2==0:
        print(l[i],": Even")
        ECount+=1
    else:
        print(l[i],": Odd")
        OCount+=1

print("Count of Even Numbers in series = ",ECount)
print("Count of Odd Numbers in series = ",OCount)

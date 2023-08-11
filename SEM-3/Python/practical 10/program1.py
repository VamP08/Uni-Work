menu={1:"Small Rs.200/-",2:"Medium Rs.350/-",3:"Large Rs.500/-"}
bill=[0,0,0]
cost=0 

def order():
    print(menu)
    i=int(input("What would you like to order(1/2/3): "))
    amm=int(input("How many of those would you like: "))
    if i==1:
        bill[0]+=amm
    if i==2:
        bill[1]+=amm
    if i==3:
        bill[2]+=amm
    
    ans=input("Would you like to order again: ")
    if ans=="y":
        order()
        

order()
cost=(bill[0]*200)+(bill[1]*350)+(bill[2]*500)
print("Total Cost of your order: ",cost)
print("Thank You")
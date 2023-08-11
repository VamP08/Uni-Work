#2)(a)
i=0
L=[]
while(i<3):
    BS=int(input("Enter Basic Salary of Employee :"))
    L.append(BS)
    i+=1
i=0
while(i<3):
    BS=L[i]
    HRA=(5*100)/BS
    DA=(20*100)/BS
    MA=(10*100)/BS
    GS=BS+HRA+DA+MA
    print("Gross Salary of Employee",i,"is Rs",GS)
    i+=1
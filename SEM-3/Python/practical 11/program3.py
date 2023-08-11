dict1={
    100:"Dhoni",
    40:"Kohli",
    5:"Rohit"
}

l=list(dict1.keys())
l.sort()
dict2 = {i:dict1[i] for i in l}

i=dict2.keys()
print("\nKey=",i,end=" ")
j=dict2.values()
print("\nValues=",j,end=" ")


dict1={"s1":"My","s2":"Name","s3":"is"}

i=dict1.keys()
print("\nKey=",i,end=" ")
j=dict1.values()
print("\nValues=",j,end=" ")

dict1["s4"] = "Pratham"

del dict1['s1']
i=dict1.keys()
print("\nKey=",i,end=" ")
j=dict1.values()
print("\nValues=",j,end=" ")

key='s1'
if key in dict1:
    print(key,"is present in dictionary.")
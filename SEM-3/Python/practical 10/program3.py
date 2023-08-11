tuple1 = ("disco", 10, 1.2)
print(tuple1)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

print(tuple1[-1])  
print(tuple1[-2])  
print(tuple1[-3])  

tuple2 = ("Hard Rock", 10)
tuple3 = tuple1 + tuple2
print(tuple3) 

sliced_tuple = tuple3[0:3]
print(sliced_tuple) 

tuple_length = len(tuple3)
print(tuple_length)
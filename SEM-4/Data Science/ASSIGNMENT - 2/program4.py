import math

def create_list(number):
   indices = list(range(1, number+1))
   return list(map(lambda index: math.pow(number, index), indices))

print(create_list(3))
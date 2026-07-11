from functools import reduce

numbers=[5,10,15,20]
result=reduce(lambda x,y : x+y,numbers)
print(result)

numbers=[2,3,5]
result=reduce(lambda x,y : x*y,numbers)
print(result)

numbers=[12,45,7,89,34]
result=reduce(lambda x,y : x if x>y else y,numbers)
print(result)

numbers=[12,45,7,89,34]
result=reduce(lambda x,y : x if x<y else y,numbers)
print(result)
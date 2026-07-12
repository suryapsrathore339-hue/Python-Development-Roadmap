numbers=[1,2,3,4,5]
cubes=[x**3 for x in numbers]
print(cubes)

words=["AI","ML","PYTHON","DATA"]
lower=[x.lower() for x in words]
print(lower)

numbers=[3,5,6,8,9,12,14]
result=[x for x in numbers if x%3==0]
print(result)

numbers=[1,2,3,4,5,6]
result=[x**2 for x in numbers if x%2==0]
print(result)
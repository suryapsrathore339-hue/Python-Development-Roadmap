numbers=(x**2 for x in range(1,6))
print(list(numbers))

words=(word.upper() for word in ["AI","Python","ML"])
print(list(words))

numbers=(x for x in range(1,11) if x%2==0)
print(list(numbers))

cubes=(x**3 for x in range(1,6))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
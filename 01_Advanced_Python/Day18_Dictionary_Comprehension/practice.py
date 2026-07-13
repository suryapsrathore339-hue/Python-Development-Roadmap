numbers=[1,2,3,4,5]
result={x:x**2 for x in numbers}
print(result)

words = ['apple', 'banana', 'cherry']
result2 = {x: len(x) for x in words}
print(result2)

numbers2 = [1, 2, 3, 4, 5]
result3 ={x: x**3 for x in numbers2 if x % 2 == 1}
print(result3)

names=["surya","sai","kiran"]
upper={x:x.upper() for x in names}
print(upper)
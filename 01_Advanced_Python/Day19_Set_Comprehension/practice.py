numbers=[1,2,2,3,4,4,5]
unique_numbers={x for x in numbers}
print(unique_numbers)

words=["Apple","Banana","APPLE","banana"]
lowercase={x.lower() for x in words}
print(lowercase)

numbers=[1,2,3,4,5,6]
cubed={x**3 for x in numbers if x%2==0}
print(cubed)

sentence="machine learning"
unique_characters={x for x in sentence if x.isalpha()}
print(unique_characters)
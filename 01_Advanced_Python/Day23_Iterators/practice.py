numbers=[5,10,15]
it=iter(numbers)
print(next(it))
print(next(it))
print(next(it))

gen=(x*x for x in range (1,6))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def even_numbers():
    yield 2
    yield 4
    yield 6
    yield 8 
    yield 10

gen=even_numbers()

for num in range(1,6):
    print(next(gen))

# bonus ques prints
# 0
# 1
# 2

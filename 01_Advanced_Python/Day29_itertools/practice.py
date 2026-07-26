from itertools import count
c=count(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

from itertools import cycle
colors=cycle(["Red", "Green"])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))

from itertools import repeat

for x in repeat("Python",4):
    print(x)

from itertools import product

for x in product([1,2],["A","B"]):
    print(x)

# a)before training
# b)learned during training
# b)grid search
# b)Random Search
# it improves generalisation

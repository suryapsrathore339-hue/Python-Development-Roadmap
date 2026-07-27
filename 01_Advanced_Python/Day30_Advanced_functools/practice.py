from functools import partial
def power(base,exponent):
    return base**exponent

square=partial(power,exponent=2)
print(square(5))
print(square(8))

from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

# ans1- output-25 64
# ans2- output-120
# 1.c)scikit-learn
# 2.b)collect data
# 3.a)evaluate on test data
# 4.b)before evaluating the initial data
# 5.as it helps in implementing the classic ml algorithms
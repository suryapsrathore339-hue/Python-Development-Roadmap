numbers=[2,4,6,7]
result=any(map(lambda x:x%2==1,numbers))
print(result)

marks=[85,92,78,88]
result=all(map(lambda x:x>70,marks))
print(result)

words=["AI","ML","Python"]
result=any(map(lambda x:len(x)>5,words))
print(result)

numbers=[10,20,30,40]
result=all(map(lambda x:x%10==0,numbers))
print(result)
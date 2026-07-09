numbers=[2,4,6,8]
result=map(lambda x:x**2,numbers)
print(list(result))

name=["surya","iiitdm","python","machine learning"]
result=map(lambda x:x.upper(),name)
print(list(result))

prices=[100,250,400,150]
new_prices=map(lambda x:x*1.18,prices)
print(list(new_prices))
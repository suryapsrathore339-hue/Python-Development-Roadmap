numbers=[5,8,12,15,20,23]
result=list(filter(lambda x:x%2==0,numbers))
print(result)

numbers=[-10,5,-3,8,0,12]
result=list(filter(lambda x:x>=0,numbers))
print(result)

students=["Ram","Shyam","Python","AI","ML","Machine Learning"]
result=list(filter(lambda x:len(x)>4,students))
print(result)
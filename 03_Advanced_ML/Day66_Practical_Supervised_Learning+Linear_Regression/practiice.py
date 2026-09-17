from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import(mean_absolute_error,mean_squared_error,r2_score)

import pandas as pd
data={
    "YearsExperience":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    "Age":[25,27,28,30,31,34,35,36,37,39,40,42,43,45,46],
    "EducationYears":[4,5,3,6,4,6,5,6,7,6,4,8,6,5,5],
    "Salary(in K)":[30,32,40,87,56,90,70,50,60,57,60,75,90,65,70]
}

df=pd.DataFrame(data)

X=df[["YearsExperience","Age","EducationYears"]]
y=df["Salary(in K)"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)

rmse=mse**0.5

r2=r2_score(y_test,y_pred)

print("MAE:",mae)
print("MSE:",mse)
print("RMSE:",rmse)
print("R2:",r2)

print("Coefficient:",model.coef_)
print("Intercept:",model.intercept_)

import matplotlib.pyplot as plt
X_exp=df[["YearsExperience"]]
y_salary=df["Salary(in K)"]

model_exp=LinearRegression()
model_exp.fit(X_exp,y_salary)

y_line=model_exp.predict(X_exp)

plt.scatter(X_exp,y_salary)
plt.plot(X_exp,y_line)

plt.xlabel("Years of Experience")
plt.ylabel("Salary(K)")
plt.title("Years of Experience vs Salary")

plt.show()
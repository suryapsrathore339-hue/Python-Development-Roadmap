from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import(mean_absolute_error,mean_squared_error,r2_score)

import numpy as np

X=np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y=np.array([3,5,10,17,26,37,50,65,82,101])

poly=PolynomialFeatures(degree=2)
model=LinearRegression()

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)

model.fit(X_train_poly, y_train)

y_pred=model.predict(X_test_poly)

model1=LinearRegression()

model1.fit(X_train, y_train)

y_pred1=model1.predict(X_test)

# Model 1
mae1=mean_absolute_error(y_test,y_pred1)
mse1=mean_squared_error(y_test,y_pred1)
rmse1=mse1**0.5
r21=r2_score(y_test,y_pred1)

print("Linear Regression:")
print("MAE:",mae1)
print("RMSE:",rmse1)
print("R2:",r21)


# Model 2
mae2=mean_absolute_error(y_test, y_pred)
mse2=mean_squared_error(y_test, y_pred)
rmse2=mse2**0.5
r22=r2_score(y_test,y_pred)

print("\nPolynomial Regression:")
print("MAE:",mae2)
print("RMSE:",rmse2)
print("R2:",r22)

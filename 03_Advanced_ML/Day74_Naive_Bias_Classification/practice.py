import numpy as np

X=np.array([
    [1,20],
    [2,21],
    [1,22],
    [2,23],
    [8,80],
    [9,82],
    [8,78],
    [10,85]
])

y=np.array([0,0,0,0,1,1,1,1])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.naive_bayes import GaussianNB

model=GaussianNB()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(y_test,y_pred)

print("Predictions:",y_pred)
print("Actual:",y_test)
print("Accuracy:",accuracy)
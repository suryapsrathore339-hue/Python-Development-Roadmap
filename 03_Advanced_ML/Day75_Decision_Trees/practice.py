import numpy as np

X=np.array([
    [1,20],
    [2,21],
    [3,22],
    [4,23],
    [8,40],
    [9,41],
    [10,42],
    [11,43]
])

y=np.array([
    0,0,0,0,
    1,1,1,1
])

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

from sklearn.tree import DecisionTreeClassifier

model=DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(y_test,y_pred)

print("Predictions:",y_pred)
print("Actual:",y_test)
print("Accuracy:",accuracy)
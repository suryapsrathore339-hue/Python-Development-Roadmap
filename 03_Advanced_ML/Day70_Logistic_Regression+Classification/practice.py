import numpy as np

X=np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])

y=np.array([
    0,0,0,0,0,
    1,1,1,1,1
])

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()

model.fit(X_train,y_train)

y_pred=model.predict(X_test)
y_prob=model.predict_proba(X_test)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(y_test,y_pred)

print("Predictions:", y_pred)
print("Probabilities:", y_prob)
print("Accuracy:", accuracy)

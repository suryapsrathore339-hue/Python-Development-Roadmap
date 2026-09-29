import numpy as np

X=np.array([
    [1,2],
    [2,3],
    [2,1],
    [3,2],
    [8,8],
    [9,7],
    [8,9],
    [10,8]
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

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier

model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

y_pred=model.predict(X_test_scaled)

print("Predictions:",y_pred)
print("Actual:",y_test)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy)

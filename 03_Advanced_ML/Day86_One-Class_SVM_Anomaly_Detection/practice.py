import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM

rng=np.random.RandomState(42)
normal_data=rng.normal(
    loc=0,scale=1,size=(200,2)
)

anomalies=np.array([
    [7,7],
    [-8,8],
    [9,-7]
])

X=np.vstack([normal_data,anomalies])

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

model=OneClassSVM(
    kernel="rbf",
    nu=0.02,
    gamma="scale"
)

predictions=model.fit_predict(X_scaled)

print("Total observations:",len(X_scaled))
print("Predicted normal:",np.sum(predictions==1))
print("Predicted anomalies:",np.sum(predictions==-1))
print("Last three predictions:",predictions[-3:])

scores = model.decision_function(X_scaled[-3:])
print("Last three decision scores:",scores.ravel())


import numpy as np
from sklearn.ensemble import IsolationForest

rng=np.random.RandomState(42)
normal_data=rng.normal(loc=0,scale=1,size=(200,2))

anomalies=np.array([
    [7,7],
    [-8,8],
    [9,-7]
])

X=np.vstack([normal_data,anomalies])

model=IsolationForest(
    n_estimators=100,
    contamination=3/len(X),
    random_state=42
)

predictions=model.fit_predict(X)

print("Total observations:", len(X))
print("Predicted normal:", np.sum(predictions == 1))
print("Predicted anomalies:", np.sum(predictions == -1))
print("Last three predictions:", predictions[-3:])

scores = model.decision_function(X[-3:])
print("Anomaly scores:", scores)

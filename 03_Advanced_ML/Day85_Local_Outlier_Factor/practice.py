import numpy as np
from sklearn.neighbors import LocalOutlierFactor

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

model=LocalOutlierFactor(
    n_neighbors=20,
    contamination=3/len(X)
)

predictions=model.fit_predict(X)

print("Total observations:",len(X))
print("Predicted normal:",np.sum(predictions==1))
print("Predicted anomalies:",np.sum(predictions==-1))
print("Last three predictions:", predictions[-3:])

lof_scores=-model.negative_outlier_factor_
print("Last three LOF scores:", lof_scores[-3:])


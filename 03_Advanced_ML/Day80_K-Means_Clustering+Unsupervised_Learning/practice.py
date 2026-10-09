import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X=np.array([
    [20,80],
    [22,85],
    [25,78],
    [23,82],
    [80,20],
    [85,18],
    [78,25],
    [82,22],
    [50,50],
    [52,48],
    [48,53],
    [51,52]
])

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

model=KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X_scaled)

labels=model.labels_

print("Cluster labels:", labels)
print("Centroids:\n",model.cluster_centers_)
print("Inertia:",model.inertia_)
import numpy as np
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import DBSCAN

X,_=make_moons(
    n_samples=300,
    noise=0.06,
    random_state=42
)

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

model=DBSCAN(
    eps=0.25,
    min_samples=5
)
labels=model.fit_predict(X_scaled)

unique_labels=set(labels)
n_clusters=len(unique_labels-{-1})
n_noise=np.sum(labels==-1)

print("Cluster labels:",unique_labels)
print("Number of clusters:",n_clusters)
print("Number of noise points:",n_noise)
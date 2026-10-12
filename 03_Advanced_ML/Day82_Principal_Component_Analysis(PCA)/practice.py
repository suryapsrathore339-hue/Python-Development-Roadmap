import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data=load_wine()
X=data.data
y=data.target

print("Original Shape:",X.shape)

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42,stratify=y
)

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

pca=PCA(n_components=2)
X_train_pca=pca.fit_transform(X_train_scaled)
X_test_pca=pca.transform(X_test_scaled)

print("Reduced training shape:",X_train_pca.shape)
print("Reduced test shape:",X_test_pca.shape)

print("Explained variance ratio:",
      pca.explained_variance_ratio_)

print("Total variance retained:",
      pca.explained_variance_ratio_.sum())

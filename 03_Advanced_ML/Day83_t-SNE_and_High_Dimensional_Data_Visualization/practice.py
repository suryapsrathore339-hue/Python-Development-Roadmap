import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

data=load_digits()
X=data.data
y=data.target 

print("Original Shape:", X.shape)

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

pca=PCA(n_components=30,random_state=42)
X_reduced=pca.fit_transform(X_scaled)

tsne=TSNE(
    n_components=2,
    perplexity=30,
    learning_rate="auto",
    init="pca",
    random_state=42
)

X_embedded=tsne.fit_transform(X_reduced)

print("t-SNE output shape:",X_embedded.shape)

plt.figure(figsize=(10,7))
scatter=plt.scatter(
    X_embedded[:, 0],
    X_embedded[:, 1],
    c=y,
    cmap="tab10",
    s=10
)

plt.colorbar(scatter, label="Digit label")
plt.title("t-SNE Visualization of Handwritten Digits")
plt.xlabel("t-SNE dimension 1")
plt.ylabel("t-SNE dimension 2")
plt.tight_layout()
plt.show()

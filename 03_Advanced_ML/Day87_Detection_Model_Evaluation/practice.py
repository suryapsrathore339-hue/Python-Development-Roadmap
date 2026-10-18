import numpy as np

from sklearn.datasets import make_blobs
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import(
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score
)

X_normal,_=make_blobs(
    n_samples=500,
    centers=[[0,0]],
    cluster_std=1.0,
    random_state=42
)

rng=np.random.RandomState(42)
X_anomalies=rng.uniform(
    low=-7,high=7,size=(25,2)
)

X=np.vstack([X_normal,X_anomalies])

y_true=np.concatenate([
    np.zeros(len(X_normal),dtype=int),
    np.ones(len(X_anomalies),dtype=int)
])

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

models={
    "Isolation Forest":IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    ),
    "LOF":LocalOutlierFactor(
        n_neighbors=20,
        contamination=0.05
    ),
    "One-Class SVM":OneClassSVM(
        kernel="rbf",
        nu=0.05,
        gamma="scale"
    )
}

for name, model in models.items():
    raw_predictions=model.fit_predict(X_scaled)
    y_pred=(raw_predictions==-1).astype(int)

    print("\n",name)
    print("Precision:",round(
        precision_score(y_true,y_pred,zero_division=0),3
    ))
    print("Recall:",round(
        recall_score(y_true,y_pred,zero_division=0),3
    ))
    print("F1-score:",round(
        f1_score(y_true,y_pred,zero_division=0),3
    ))
    print("Confusion matrix:\n",confusion_matrix(y_true,y_pred))

    if name == "Isolation Forest":
        scores = -model.score_samples(X_scaled)
    elif name == "LOF":
        scores = -model.negative_outlier_factor_
    else:
        scores = -model.decision_function(X_scaled).ravel()

    print("ROC-AUC:", round(
        roc_auc_score(y_true, scores), 3
    ))


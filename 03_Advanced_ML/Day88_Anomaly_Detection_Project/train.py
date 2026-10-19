import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import(
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
)

import joblib 

X_normal,_=make_blobs(
    n_samples=500,
    centers=[[0,0]],
    cluster_std=1.0,
    random_state=42,
)

rng=np.random.RandomState(42)
X_anomalies=rng.uniform(low=-7,high=7,size=(25,2))

X=np.vstack([X_normal,X_anomalies])

y=np.concatenate([
    np.zeros(len(X_normal),dtype=int),
    np.ones(len(X_anomalies),dtype=int),
])

print("Dataset shape:",X.shape)
print("Normal observations:",np.sum(y==0))
print("Anomalies:",np.sum(y==1))

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

print("\nTraining samples:",len(X_train))
print("Testing samples:",len(X_test))

pipeline=Pipeline([
    ("scaler",StandardScaler()),
    (
        "model",
        IsolationForest(
            n_estimators=100,
            contamination="auto",
            random_state=42,
        ),
    ),
])

pipeline.fit(X_train)

raw_predictions=pipeline.predict(X_test)

y_pred=(raw_predictions==-1).astype(int)

print("\n-- Evaluation Results ---")
print("Precision:", round(
    precision_score(y_test,y_pred,zero_division=0),3
))
print("Recall:", round(
    recall_score(y_test,y_pred,zero_division=0),3
))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test,y_pred))

anomaly_scores=-pipeline.decision_function(X_test)
print("ROC-AUC:",round(
    roc_auc_score(y_test,anomaly_scores),3
))

joblib.dump(pipeline,"anomaly_detector.joblib")
print("\nPipeline saved to anomaly_detector.joblib")


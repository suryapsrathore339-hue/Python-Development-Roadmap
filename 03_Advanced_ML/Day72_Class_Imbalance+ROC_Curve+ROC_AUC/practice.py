y_true=[0,0,0,0,0,0,0,0,0,0,1,1]
y_prob=[0.10,0.20,0.15,0.30,0.05,0.40,0.25,0.10,0.35,0.20,
        0.80,0.90]

from sklearn.metrics import roc_auc_score
auc=roc_auc_score(y_true,y_prob)
print("ROC-AUC:", auc)

from sklearn.metrics import roc_curve
fpr,tpr,thresholds=roc_curve(y_true,y_prob)

print("FPR:",fpr)
print("TPR:",tpr)
print("Thresholds:",thresholds)

import matplotlib.pyplot as plt

plt.plot(fpr,tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()
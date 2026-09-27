y_true=[1,1,1,1,0,0,0,0]
y_pred=[1,1,0,1,1,0,0,0]

from sklearn.metrics import(
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

cm=confusion_matrix(y_true,y_pred)

print("Confusion Matrix: ")
print(cm)

accuracy=accuracy_score(y_true,y_pred)
precision=precision_score(y_true,y_pred)
recall=recall_score(y_true,y_pred)
f1=f1_score(y_true,y_pred)

print("Accuracy:",accuracy)
print("Precision:",precision)
print("Recall:",recall)
print("F1 Score:",f1)
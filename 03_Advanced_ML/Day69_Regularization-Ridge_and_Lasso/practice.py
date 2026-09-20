import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# Dataset
X=np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)

y=np.array([
    3,5,10,17,26,
    37,50,65,82,101
])

# Train-test split
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Try different alpha values
for alpha in [0.01,1,100]:

    model=Pipeline([
        ("poly", PolynomialFeatures(degree=5)),
        ("scalar", StandardScaler()),
        ("ridge",Ridge(alpha=alpha))
    ])

    # Train
    model.fit(X_train,y_train)

    # Predictions
    y_pred=model.predict(X_test)

    # Metrics
    mae=mean_absolute_error(y_test,y_pred)
    mse=mean_squared_error(y_test,y_pred)
    rmse=mse**0.5
    r2=r2_score(y_test,y_pred)

    print(f"\nAlpha = {alpha}")
    print("MAE :", mae)
    print("RMSE :", rmse)
    print("R2 :", r2)
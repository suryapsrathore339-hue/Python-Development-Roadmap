📘 Day 66/90 — Supervised Learning + Linear Regression
1. Supervised Learning

In supervised learning, we have:

X → Features/Input
y → Target/Output

Example:

Age + Study Hours + Previous Score → Final Score

So:

X = df[["Age", "Study Hours", "Previous Score"]]
y = df["Final Score"]
2. Basic ML Workflow
Dataset
   ↓
X and y
   ↓
Train / Validation / Test
   ↓
Preprocessing
   ↓
Model
   ↓
Training
   ↓
Prediction
   ↓
Evaluation
   ↓
Error Analysis

The key goal is generalization — performing well on unseen data.

3. Train/Test Split

Training data → used to learn parameters.

Test data → used to evaluate performance on unseen examples.

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

⚠️ Don't train and evaluate on the exact same data because the model may memorize the training examples.

4. Baseline Model

A baseline is a simple reference model.

For regression, a basic baseline can predict the mean target value for every example.

Your actual model should be compared against a reasonable baseline.

5. Linear Regression

For one feature:

$$ \hat y = wx+b $$

Where:

w = coefficient/slope
b = intercept
x = input
ŷ = predicted output

For multiple features:

$$ \hat y=w_1x_1+w_2x_2+\dots+w_nx_n+b $$

Or:

$$ \hat y=Xw+b $$

Example:

Salary = w1(Experience)
       + w2(Age)
       + w3(Education)
       + b
6. Loss Function — MSE

Mean Squared Error:

$$ MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2 $$

Why square the error?

Removes negative signs.
Penalizes large errors more strongly.

Example:

Error = 2  → squared = 4
Error = 10 → squared = 100

So MSE is particularly sensitive to large errors.

7. Gradient Descent

The model tries to minimize its loss.

General update:

$$ \theta_{new}=\theta_{old}-\alpha\nabla J(\theta) $$

Where:

θ = model parameters
α = learning rate
∇J = gradient of the loss
Intuition
Gradient
   ↓
Direction of increasing loss

Gradient Descent
   ↓
Move in opposite direction
   ↓
Lower loss

Learning rate:

Too small → learning is very slow.
Too large → may overshoot or fail to converge.
8. Regression Metrics
MAE
$$ MAE=\frac{1}{n}\sum |y-\hat y| $$

Easy interpretation.

If:

MAE = 13

your predictions are off by about 13 target units on average.

MSE
$$ MSE=\frac{1}{n}\sum(y-\hat y)^2 $$
Penalizes large errors.
Units are squared.
RMSE
$$ RMSE=\sqrt{MSE} $$

Advantages:

Same units as the target.
More sensitive to large errors than MAE.
R² Score

Measures how much better the model performs compared with predicting the mean.

$$ R^2=1-\frac{SS_{res}}{SS_{tot}} $$

Important:

R² is NOT prediction accuracy.

For example:

R² = 0.486

means the model explains about 48.6% of the variance relative to the mean baseline on that evaluated dataset.

R² can also be negative.

9. Data Leakage 🚨

Data leakage occurs when information that should not be available during training influences the model.

Example:

Test data
   ↓
Scaling
   ↓
Training

If the scaler learns statistics from the entire dataset before splitting, information from the test set can leak into training.

Correct approach:

Training data → learn preprocessing
Test data → only transform using learned preprocessing

We'll later solve this properly using Scikit-learn Pipelines.

10. Overfitting vs Underfitting
Overfitting
Training performance → Very good
Test performance     → Poor

Model learned the training data too specifically.

Underfitting
Training performance → Poor
Test performance     → Poor

Model is too simple or hasn't learned enough.

11. Model Coefficients ≠ Causation

Your Day 66 example produced:

YearsExperience coefficient = -19.31

Don't conclude:

"More experience causes salary to decrease."

Instead:

The model found a negative association for experience in this dataset while holding the other included features constant.

Why?

Dataset is small.
Data is noisy.
Features can be correlated.
Correlation/association ≠ causation.

This is an important real-world ML lesson.

12. Scikit-learn Basic Pattern
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)
🧠 Day 66 Cheat Sheet
Concept	Remember
X	Features
y	Target
Regression	Predict continuous values
Linear Regression	ŷ = Xw + b
MSE	Squares errors
MAE	Average absolute error
RMSE	√MSE, same target units
R²	Variance explained relative to mean baseline
Baseline	Simple reference model
Overfitting	Train good, test poor
Underfitting	Train poor, test poor
Data leakage	Unwanted information enters training
Coefficient	Learned association, not automatically causation
Gradient descent	Moves parameters toward lower loss

📌 Day 67 Notes: Multiple Linear Regression & Evaluation

1. Multiple Linear Regression

ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b

Uses multiple features to predict the target.

2. Coefficients
A coefficient represents the model's learned relationship with the target while accounting for the other included features.
It does not automatically imply causation.

3. Multicollinearity
When input features are strongly correlated.

Example:

Age ↔ YearsExperience

Can cause:

unstable coefficients
unexpected positive/negative coefficients
sensitivity to small dataset changes

4. Feature Scaling

Standardization:

z = (x - mean) / standard_deviation

Using:

StandardScaler()

Especially important for:

KNN
K-Means
SVM
Logistic Regression
Neural Networks

Usually not necessary for ordinary Linear Regression.

5. Train / Validation / Test

TRAIN       → Learn parameters
VALIDATION  → Choose/tune model
TEST        → Final evaluation

6. Cross-Validation

With 5-fold CV:

Fold 1 → validation
Fold 2 → validation
Fold 3 → validation
Fold 4 → validation
Fold 5 → validation

Every sample gets used for validation once, and the scores are averaged.

cross_val_score(model, X, y, cv=5, scoring="r2")
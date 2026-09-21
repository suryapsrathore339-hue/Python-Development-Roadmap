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

📚 Day 68 Notes — Polynomial Regression + Bias–Variance
1. Why Polynomial Regression?

Linear Regression assumes a roughly linear relationship:

$$ y=w_1x+b $$

But real relationships can be curved.

Polynomial Regression adds powers of the features:

$$ y=w_0+w_1x+w_2x^2+\cdots+w_nx^n $$

Example:

Degree 1 → y = w0 + w1x
Degree 2 → y = w0 + w1x + w2x²
Degree 3 → y = w0 + w1x + w2x² + w3x³

Important: Polynomial Regression is still based on Linear Regression. It first transforms the features, then Linear Regression learns the coefficients.

2. PolynomialFeatures
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

Then:

model = LinearRegression()
model.fit(X_train_poly, y_train)

y_pred = model.predict(X_test_poly)
fit_transform() vs transform()
Training data → fit_transform()
Testing data  → transform()

General rule for learned preprocessing:

Fit only on training data.

3. Model Complexity

Polynomial degree controls model flexibility.

Degree	Complexity
1	Low
2	Moderate
3	Higher
Very high	Very high

Higher degree allows the model to capture more complicated patterns, but also increases the risk of overfitting.

4. Underfitting

The model is too simple to capture the underlying pattern.

Typical behavior:

Training error → High
Validation error → High

Usually associated with:

High Bias

Example: using a straight line for a strongly curved relationship.

5. Overfitting

The model becomes too complex and starts learning noise/details specific to the training data.

Typical behavior:

Training error → Very Low
Validation/Test error → High

Usually associated with:

High Variance

Example: using a very high-degree polynomial for a small dataset.

6. Bias–Variance Tradeoff

As model complexity increases:

Complexity ↑
      ↓
Bias generally ↓
Variance generally ↑

We want a balance.

Conceptually:

Validation Error
      ↑
      | \       /
      |  \_____/
      |    ↑
      |  Best
      +----------------→ Model Complexity

The goal is good generalization, not minimum training error.

7. Why Training Error Alone Is Dangerous

Suppose:

Degree 1 → Training error = 10
Degree 5 → Training error = 2
Degree 15 → Training error = 0.1

It does not automatically mean Degree 15 is best.

Degree 15 may have memorized the training data.

📚 Day 69 Notes — Regularization: Ridge & Lasso
1. What is Regularization?

Regularization is a technique used to reduce overfitting by adding a penalty for large model coefficients.

Normal Linear Regression minimizes:

$$ MSE $$

Regularized regression minimizes:

$$ MSE + \text{Penalty} $$

The goal is:

Fit the data well while keeping the model from becoming unnecessarily complex.

2. Why Regularization?

From Day 68:

Model complexity ↑
        ↓
Overfitting risk ↑

Regularization provides a way to control that complexity.

Complex model
     ↓
Large coefficients
     ↓
Regularization penalty
     ↓
Coefficients shrink
     ↓
Less aggressive model
     ↓
Potentially better generalization
3. Ridge Regression — L2

Ridge uses the squared coefficients as the penalty:

$$ Loss = MSE + \lambda\sum_{j=1}^{n}w_j^2 $$

In scikit-learn:

from sklearn.linear_model import Ridge

model = Ridge(alpha=1.0)
Effect

Ridge generally:

Shrinks coefficients toward zero
Reduces model complexity
Helps control overfitting
Usually does not make coefficients exactly zero
Memory trick

Ridge → Reduce coefficient size

4. Lasso Regression — L1

Lasso uses the absolute value of coefficients:

$$ Loss = MSE + \lambda\sum_{j=1}^{n}|w_j| $$

In scikit-learn:

from sklearn.linear_model import Lasso

model = Lasso(alpha=1.0)

Lasso can force some coefficients to become exactly zero.

Therefore, it can perform feature selection.

Memory trick

Lasso → Leaves some features out

5. Ridge vs Lasso
Property	Ridge	Lasso
Regularization	L2	L1
Penalty	\(w^2\)	(
Shrinks coefficients	✅	✅
Can make coefficient exactly 0	Usually no	✅
Feature selection	Limited	✅
6. What is alpha?

alpha controls the strength of regularization.

Ridge(alpha=0.01)
Ridge(alpha=1)
Ridge(alpha=100)

Conceptually:

alpha ↑
   ↓
Penalty ↑
   ↓
Coefficient constraint ↑
   ↓
Model flexibility ↓

But:

Higher alpha is NOT automatically better.

Too little regularization
Weak penalty
    ↓
Model remains very flexible
    ↓
Overfitting may remain
Too much regularization
Very strong penalty
    ↓
Coefficients heavily shrink
    ↓
Model becomes too constrained
    ↓
Underfitting

Therefore, alpha is a hyperparameter that should be selected using validation or cross-validation.

7. Why Scaling Matters

Suppose we have:

Feature A → 0–1
Feature B → 0–100000

Regularization acts on coefficients, and feature scale affects coefficient magnitude.

Therefore, Ridge/Lasso generally work better with standardized features:

from sklearn.preprocessing import StandardScaler

Typical workflow:

X
↓
StandardScaler
↓
Ridge/Lasso
8. Pipelines

A clean implementation is:

from sklearn.pipeline import Pipeline

model = Pipeline([
    ("scaler", StandardScaler()),
    ("ridge", Ridge(alpha=1.0))
])

Then:

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

The pipeline ensures preprocessing is handled consistently and helps prevent data leakage during cross-validation.

9. Polynomial Regression + Regularization

This connects directly to Day 68.

Day 68:

Polynomial degree ↑
       ↓
Complexity ↑
       ↓
Overfitting risk ↑

Day 69:

Polynomial features
       ↓
Many coefficients
       ↓
Potential overfitting
       ↓
Ridge/Lasso
       ↓
Penalize coefficients
       ↓
Control complexity

Example:

model = Pipeline([
    ("poly", PolynomialFeatures(degree=5)),
    ("scaler", StandardScaler()),
    ("ridge", Ridge(alpha=1.0))
])
10. Your Experiment

You tested:

Alpha	MAE	RMSE	R²
0.01	0.464	0.566	0.9998
1	2.703	2.711	0.9950
100	28.802	28.974	0.4336

The important observation:

alpha = 0.01
↓
Weak regularization
↓
Very flexible model

alpha = 1
↓
Stronger regularization
↓
Still captures the pattern

alpha = 100
↓
Very strong regularization
↓
Model becomes too constrained
↓
Underfitting

⚠️ This experiment had only 10 samples and 2 test samples, so these scores demonstrate the concept rather than establishing a generally optimal alpha.

🧠 Day 69 Mental Model

Remember this:

Overfitting
    ↓
Need to control complexity
    ↓
Regularization
    ↓
       ┌──────────────┐
       │              │
     Ridge          Lasso
      L2              L1
       ↓               ↓
   Shrinks         Can make
 coefficients      coefficients
                   exactly 0
🔑 Must-remember points
Ridge = L2 regularization.
Lasso = L1 regularization.
Ridge shrinks coefficients.
Lasso can make coefficients exactly zero.
alpha controls regularization strength.
Very large alpha can cause underfitting.
Feature scaling is important for regularized models.
alpha should be selected using validation/CV.
Regularization is primarily about better generalization, not simply reducing training error.

📚 Day 70 Notes — Logistic Regression & Classification
1. Regression vs Classification

Regression predicts a continuous numerical value:

Salary → ₹70,000
Temperature → 32.5°C
House price → ₹65 lakh

Classification predicts a category/class:

Spam / Not Spam
Pass / Fail
Disease / No Disease

Binary classification:

$$ y\in\{0,1\} $$
2. Why Not Use Linear Regression?

Linear Regression can produce values outside the range [0,1].

For classification, we often need:

$$ 0\leq P(y=1)\leq1 $$

So Logistic Regression uses the sigmoid function.

$$ \sigma(z)=\frac{1}{1+e^{-z}} $$

It maps any real number to a value between 0 and 1.

Important values:

$$ \sigma(0)=0.5 $$ $$ \sigma(-\infty)\rightarrow0 $$ $$ \sigma(+\infty)\rightarrow1 $$
3. Logistic Regression

Despite its name, Logistic Regression is primarily a classification algorithm.

First:

$$ z=w_1x_1+w_2x_2+\cdots+w_nx_n+b $$

Then:

$$ P(y=1|X)=\frac{1}{1+e^{-z}} $$
Complete flow
Features
   ↓
Linear combination
z = wX + b
   ↓
Sigmoid
   ↓
Probability
   ↓
Threshold
   ↓
Class
4. Probability → Class

With the default threshold of 0.5:

P(class 1) >= 0.5 → class 1
P(class 1) <  0.5 → class 0

Examples:

0.82 → 1
0.73 → 1
0.49 → 0
0.13 → 0

The threshold can be changed depending on the application, which becomes important when we study precision and recall.

5. predict() vs predict_proba()
predict()

Returns the predicted class:

y_pred = model.predict(X_test)

Example:

[1 0 1 1]
predict_proba()

Returns probability for each class:

y_prob = model.predict_proba(X_test)

Example:

[[0.02, 0.98],
 [0.98, 0.02]]

Columns:

Column 0 → P(class 0)
Column 1 → P(class 1)
6. Decision Boundary

The standard classification threshold is:

$$ P(y=1)=0.5 $$

Since:

$$ \sigma(0)=0.5 $$

the decision boundary occurs when:

$$ z=0 $$

Therefore:

$$ wX+b=0 $$

For two features:

$$ w_1x_1+w_2x_2+b=0 $$

This gives a linear decision boundary.

7. Example

Suppose:

$$ z=2x-6 $$

At \(x=3\):

$$ z=2(3)-6=0 $$

Therefore:

$$ P(y=1)=0.5 $$

So \(x=3\) is the decision boundary.

8. Scikit-learn Implementation
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)

For classification:

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
9. Your Day 70 Experiment

You used:

X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)

y = np.array([
    0,0,0,0,0,
    1,1,1,1,1
])

Your model produced:

Predictions: [1 0]

Probabilities:
[[0.01799637 0.98200363]
 [0.98200563 0.01799437]]

So:

Sample 1
$$ P(0)=0.018 $$ $$ P(1)=0.982 $$

→ prediction = 1

Sample 2
$$ P(0)=0.982 $$ $$ P(1)=0.018 $$

→ prediction = 0

Both were correctly classified:

$$ Accuracy=1.0 $$

⚠️ But there were only 2 test samples, so this does not establish that the model has 100% real-world accuracy.
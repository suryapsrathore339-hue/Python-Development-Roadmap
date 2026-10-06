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

📘 Day 71 — Classification Metrics
1. Confusion Matrix

A confusion matrix tells us what kinds of mistakes a classification model makes.

                    Predicted
                  0          1
Actual  0       TN         FP
        1       FN         TP
Four outcomes
Term	Meaning
TP	Actual = 1, Predicted = 1
TN	Actual = 0, Predicted = 0
FP	Actual = 0, Predicted = 1
FN	Actual = 1, Predicted = 0
Easy memory
True → prediction was correct
False → prediction was wrong
Positive/Negative → what the model predicted
2. Accuracy

How many predictions were correct overall?

$$ Accuracy=\frac{TP+TN}{TP+TN+FP+FN} $$

Useful when classes are reasonably balanced.

⚠️ Can be misleading with highly imbalanced data.

3. Precision

When the model predicts positive, how often is it correct?

$$ Precision=\frac{TP}{TP+FP} $$

Precision focuses on False Positives.

Memory

Precision → "When I say YES, am I right?"

High precision → fewer false positives.

4. Recall

Of all the actual positive cases, how many did the model find?

$$ Recall=\frac{TP}{TP+FN} $$

Recall focuses on False Negatives.

Memory

Recall → "Did I find all the YES cases?"

High recall → fewer false negatives.

5. Precision vs Recall
Precision → FP matters
Recall    → FN matters
Example

If a model predicts many positives but many are actually negative:

→ FP increases
→ Precision decreases.

If a model misses many actual positives:

→ FN increases
→ Recall decreases.

6. F1 Score

F1 balances precision and recall.

$$ F1=2\frac{Precision\times Recall} {Precision+Recall} $$

It is the harmonic mean of precision and recall.

Useful when you want a balance between precision and recall, particularly when accuracy alone isn't informative.

7. Scikit-learn
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
Confusion matrix
cm = confusion_matrix(y_true, y_pred)
print(cm)
Individual metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
Complete report
from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred))
8. Your Day 71 Example

You obtained:

[[3 1]
 [1 3]]

Therefore:

TN = 3
FP = 1
FN = 1
TP = 3

And:

Accuracy  = 0.75
Precision = 0.75
Recall    = 0.75
F1 Score  = 0.75

📘 Day 72 — Class Imbalance + ROC Curve + ROC-AUC
1. Class Imbalance

A dataset is imbalanced when one class has many more examples than another.

Example:

Normal transactions = 9,900
Fraud transactions  =   100

Here, fraud is the minority class.

2. Why Accuracy Can Be Misleading

If 99% of transactions are normal, a model that predicts:

Everything → Normal

gets 99% accuracy, but detects 0 fraud cases.

Therefore, with imbalanced datasets, also consider:

Precision
Recall
F1-score
Confusion matrix
ROC-AUC
Sometimes PR-AUC
3. Classification Threshold

A classifier such as Logistic Regression produces a probability:

P(class = 1)

Example:

P(class 1) = 0.73

With threshold 0.5:

0.73 >= 0.5 → class 1

But the threshold can be changed.

Lower threshold
Threshold ↓
     ↓
More positive predictions
     ↓
Recall generally ↑
Higher threshold
Threshold ↑
     ↓
Fewer positive predictions
     ↓
Recall generally ↓
Precision may ↑

The exact precision/recall changes depend on the data.

4. ROC Curve

ROC = Receiver Operating Characteristic

It plots:

$$ TPR \text{ vs } FPR $$

at different classification thresholds.

5. True Positive Rate (TPR)

TPR is another name for Recall.

$$ TPR = \frac{TP}{TP+FN} $$

Therefore:

TPR = Recall

It measures how many actual positives the model detects.

6. False Positive Rate (FPR)
$$ FPR = \frac{FP}{FP+TN} $$

It measures:

Of all actual negative cases, how many were incorrectly classified as positive?

Memory:

TPR → How many positives did I catch?

FPR → How many negatives did I falsely flag?

A desirable ROC operating point generally has:

High TPR
Low FPR
7. ROC-AUC

AUC = Area Under the ROC Curve

ROC-AUC measures how well the model separates/ranks the two classes across thresholds.

Roughly:

AUC ≈ 1.0 → excellent separation
AUC ≈ 0.5 → random-like separation

An important interpretation:

ROC-AUC is related to the probability that a randomly chosen positive example receives a higher model score than a randomly chosen negative example.

8. predict() vs predict_proba()
predict()

Returns hard class predictions:

y_pred = model.predict(X_test)

Example:

[1, 0, 1, 0]
predict_proba()

Returns probabilities:

y_prob = model.predict_proba(X_test)

For binary classification, probability of class 1:

y_prob = model.predict_proba(X_test)[:, 1]

ROC-AUC normally uses these probabilities/scores, rather than hard 0/1 predictions.

9. Scikit-learn
ROC-AUC
from sklearn.metrics import roc_auc_score

y_prob = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, y_prob)

print("ROC-AUC:", auc)
ROC curve
from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
10. Your Day 72 Experiment

You used:

y_true = [0,0,0,0,0,0,0,0,0,0,
          1,1]

y_prob = [0.10,0.20,0.15,0.30,0.05,0.40,0.25,0.10,0.35,0.20,
          0.80,0.90]

You obtained:

ROC-AUC = 1.0

because both positive examples had higher probabilities than every negative example.

Your ROC output:

FPR = [0.0, 0.0, 0.0, 0.4, 0.6, 0.7, 0.9, 1.0]

TPR = [0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

This demonstrates how changing the threshold produces different (FPR, TPR) points.

🧠 Day 72 Cheat Sheet
Class imbalance
→ One class dominates the dataset

Accuracy
→ Can be misleading with imbalance

Threshold ↓
→ More positive predictions
→ Recall generally ↑

TPR
→ Recall
→ TP / (TP + FN)

FPR
→ False positives among actual negatives
→ FP / (FP + TN)

ROC
→ TPR vs FPR across thresholds

ROC-AUC
→ Measures class separation/ranking across thresholds

predict()
→ Hard classes

predict_proba()
→ Probabilities/scores

# Day 73 — KNN Classification + Feature Scaling

## 1. What is KNN?

**KNN = K-Nearest Neighbors**

KNN is a supervised learning algorithm used for classification and regression.

For classification:

> A new data point is assigned the class that is most common among its K nearest training points.

Example:

If K = 3 and the nearest neighbors are:

```text
0, 0, 1
```

Majority = `0`

Therefore, the new point is classified as `0`.

---

## 2. How KNN Works

Suppose we have a new point:

```text
X = (5, 6)
```

KNN:

1. Calculates distance from the new point to training points.
2. Finds the K closest points.
3. Looks at their labels.
4. Takes the majority class.
5. Assigns that class to the new point.

---

## 3. Euclidean Distance

The most common distance metric is Euclidean distance.

For two points:

```text
A = (x₁, x₂)
B = (y₁, y₂)
```

Distance:

```text
d = √[(x₁-y₁)² + (x₂-y₂)²]
```

For n dimensions:

```text
d = √Σ(xᵢ-yᵢ)²
```

### Example

```text
A = (1, 2)
B = (4, 6)
```

```text
d = √[(4-1)² + (6-2)²]
  = √[9 + 16]
  = 5
```

---

# 4. Why Feature Scaling is Critical in KNN

KNN depends on **distance**.

Suppose we have:

```text
Age = 20–60
Salary = 20,000–2,00,000
```

Salary has a much larger numerical scale.

Therefore, salary can dominate the distance calculation even if age is equally important.

### Solution → Feature Scaling

A common method is **Standardization**.

```text
z = (x - μ) / σ
```

Where:

* `μ` = mean
* `σ` = standard deviation

After standardization, features are placed on comparable scales.

---

# 5. StandardScaler

Scikit-learn:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Important rule

```text
Training data → fit_transform()
Test data     → transform()
```

Do NOT do:

```python
scaler.fit_transform(X_test)
```

because the scaler would learn information from the test set.

This can cause **data leakage**.

---

# 6. Choosing K

`K` = number of neighbors considered.

Example:

```python
KNeighborsClassifier(n_neighbors=3)
```

means:

> Look at the 3 closest training points.

### Small K

Example:

```text
K = 1
```

Characteristics:

* Very flexible
* Low bias
* High variance
* Sensitive to noise
* Greater overfitting risk

### Large K

Characteristics:

* Smoother decision boundary
* Higher bias
* Lower variance
* Can underfit

### Memory Trick

```text
Small K → sensitive → overfit
Large K → smooth → underfit
```

K should normally be selected using **validation or cross-validation**, not randomly.

---

# 7. KNN is a Lazy Learner

KNN does not learn a complicated mathematical model during training like Linear Regression.

Instead, it essentially stores the training data.

When a prediction is required:

```text
New point
   ↓
Calculate distances
   ↓
Find K nearest points
   ↓
Majority vote
   ↓
Prediction
```

Therefore, KNN is often called:

* Lazy learner
* Instance-based learner
* Memory-based learner

---

# 8. Complete KNN Workflow

```text
Raw Data
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
KNN Model
   ↓
Training
   ↓
Prediction
   ↓
Evaluation
```

Python:

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)

print("Predictions:", y_pred)
print("Actual:", y_test)
print("Accuracy:", accuracy)
```

---

# 9. Day 73 Dataset

```python
X = np.array([
    [1, 2],
    [2, 3],
    [2, 1],
    [3, 2],
    [8, 8],
    [9, 7],
    [8, 9],
    [10, 8]
])

y = np.array([
    0, 0, 0, 0,
    1, 1, 1, 1
])
```

The first group belongs to class `0` and the second group belongs to class `1`.

Your result:

```text
Predictions: [0 1]
Actual:      [0 1]
Accuracy:    1.0
```

Correct. ✅

---

# 10. KNN Bias-Variance Relationship

| K     | Bias | Variance | Overfitting |
| ----- | ---- | -------- | ----------- |
| Small | Low  | High     | Higher      |
| Large | High | Low      | Lower       |

Think:

```text
K ↓ → Model becomes more sensitive
K ↑ → Model becomes smoother
```

---

# 11. Key Interview Points

### Why scale features for KNN?

Because KNN uses distance, and features with larger numerical ranges can dominate the distance calculation.

### Why fit scaler only on training data?

To prevent information from the test set influencing preprocessing.

### What happens when K = 1?

The closest training point completely determines the prediction, making the model sensitive to noise.

### Is KNN a parametric model?

No. KNN is generally considered **non-parametric**.

### Is KNN lazy?

Yes. Most computation happens during prediction rather than model training.

---

# 12. Day 73 Quick Revision

```text
KNN
 ↓
Find nearest K points
 ↓
Majority vote
 ↓
Prediction
```

Remember these 6 points:

1. **KNN is distance-based.**
2. **Scaling is important.**
3. `fit_transform()` → training data.
4. `transform()` → test data.
5. Small K → low bias, high variance.
6. Large K → high bias, low variance.

### Most important formula

```text
Euclidean Distance = √Σ(xᵢ-yᵢ)²
```

### Most important preprocessing rule

```text
X_train → fit_transform
X_test  → transform
```

##

# Day 74 — Naive Bayes Classification

## 1. What is Naive Bayes?

**Naive Bayes** is a supervised machine learning algorithm primarily used for classification.

It is based on **Bayes' Theorem**.

Common applications:

* Spam detection
* Sentiment analysis
* Text classification
* News/document classification
* Medical classification

---

## 2. Bayes' Theorem

The fundamental formula is:

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

For machine learning:

$$
P(Class|Features)
=
\frac{P(Features|Class)P(Class)}
{P(Features)}
$$

Since \(P(Features)\) is the same for all classes when comparing them:

$$
P(Class|Features)
\propto
P(Features|Class)\times P(Class)
$$

### Memory

```text
Posterior ∝ Likelihood × Prior
```

---

# 3. Three Important Terms

### Prior

Probability of a class before observing the features.

$$
P(Class)
$$

Example:

```text
90% emails → Not Spam
10% emails → Spam
```

Therefore:

```text
P(Spam) = 0.10
P(Not Spam) = 0.90
```

### Likelihood

Probability of observing the features given a particular class.

$$
P(Features|Class)
$$

### Posterior

Probability of a class after observing the features.

$$
P(Class|Features)
$$

---

# 4. Why is it called "Naive"?

Naive Bayes makes a simplifying assumption:

> Features are conditionally independent given the class.

For example, in spam detection:

```text
"free"
"offer"
"winner"
```

Naive Bayes treats these features as conditionally independent once the class is known.

This assumption may not always be realistic, but the algorithm can still perform well in many practical problems.

---

# 5. Types of Naive Bayes

There are three important variants.

## Gaussian Naive Bayes

Used for **continuous numerical features**.

Examples:

```text
Age
Height
Temperature
Salary
```

Scikit-learn:

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
```

---

## Multinomial Naive Bayes

Commonly used for **count-based data**, especially text.

Examples:

```text
word counts
term frequencies
document classification
```

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
```

---

## Bernoulli Naive Bayes

Used when features are **binary**.

Example:

```text
word present → 1
word absent  → 0
```

```python
from sklearn.naive_bayes import BernoulliNB

model = BernoulliNB()
```

### Quick memory

```text
Gaussian    → Continuous
Multinomial → Counts / Text
Bernoulli   → Binary
```

---

# 6. Gaussian Naive Bayes

For Day 74, we used:

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
```

It assumes that continuous features follow a Gaussian (normal) distribution within each class.

Conceptually:

```text
Feature
   ↓
Estimate distri
```
# Day 75 — Decision Trees

## 1. What is a Decision Tree?

A **Decision Tree** is a supervised machine learning algorithm used for:

* Classification
* Regression

It makes predictions by repeatedly asking questions about features.

Think of it as a sequence of **if-else conditions**.

Example:

```text
Age > 30?
   ↓
 ┌───────┐
No      Yes
 ↓        ↓
Class 0  Experience > 5?
             ↓
          Class 1
```

---

# 2. How Does a Decision Tree Work?

The tree starts at the **root node**.

It then finds a feature and threshold that creates useful groups.

For example:

```text
Salary < 50K?
```

This splits the data into:

```text
Left → Salary < 50K
Right → Salary >= 50K
```

The process continues recursively.

```text
Root
 ↓
Split
 ↓
Child Nodes
 ↓
More Splits
 ↓
Leaf Nodes
 ↓
Prediction
```

---

# 3. Important Tree Terminology

### Root Node

The first/top decision in the tree.

### Internal Node

A node where another decision/split occurs.

### Branch

The path created by a decision.

### Leaf Node

The final node where the prediction is made.

Example:

```text
             Root
              |
          Age > 30?
         /         \
      Node         Node
       |             |
   Experience?     Leaf
    /     \
 Leaf     Leaf
```

---

# 4. How Does the Tree Choose a Split?

The goal is to create **purer groups**.

For classification, two important measures are:

* Gini Impurity
* Entropy

---

# 5. Gini Impurity

Formula:

$$
Gini = 1-\sum p_i^2
$$

where \(p_i\) is the proportion of samples belonging to class \(i\).

### Example

Suppose a node contains:

```text
10 samples

Class 0 → 10
Class 1 → 0
```

Then:

$$
Gini = 1-(1^2+0^2)
$$

$$
Gini=0
$$

Therefore:

> **Gini = 0 → perfectly pure node**

---

# 6. Mixed Node

Suppose:

```text
Class 0 → 5
Class 1 → 5
```

Then:

$$
p_0=0.5
$$

$$
p_1=0.5
$$

Therefore:

$$
Gini=1-(0.5^2+0.5^2)
$$

$$
Gini=0.5
$$

So the node is much less pure.

### Memory

```text
Lower Gini → Higher purity
Gini = 0   → Perfectly pure
```

---

# 7. Entropy

Another measure of impurity is **Entropy**.

Formula:

$$
Entropy=-\sum p_i\log_2(p_i)
$$

Interpretation:

```text
Low entropy  → Pure node
High entropy → Mixed node
```

A completely pure node has:

$$
Entropy=0
$$

---

# 8. Gini vs Entropy

Both are used to measure node impurity.

```text
Gini
  ↓
Impurity

Entropy
  ↓
Impurity
```

In practice, you usually don't calculate them manually.

Scikit-learn can choose the criterion:

```python
DecisionTreeClassifier(
    criterion="gini"
)
```

or:

```python
DecisionTreeClassifier(
    criterion="entropy"
)
```

---

# 9. Overfitting in Decision Trees

This is one of the most important concepts.

A tree can keep splitting until it becomes extremely complicated.

Example:

```text
Simple tree
     ↓
Few rules
     ↓
May underfit
```

But:

```text
Very deep tree
     ↓
Many highly specific rules
     ↓
May memorize training data
     ↓
Overfitting
```

Therefore, controlling tree complexity is important.

---

# 10. `max_depth`

`max_depth` controls the maximum depth of the tree.

Example:

```python
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
```

Smaller depth:

```text
↓ complexity
↓ overfitting risk
↑ bias
```

Larger depth:

```text
↑ complexity
↑ overfitting risk
↓ bias
```

---

# 11. Other Important Hyperparameters

### `min_samples_split`

Minimum number of samples required to split an internal node.

Example:

```python
DecisionTreeClassifier(
    min_samples_split=5
)
```

A node needs at least 5 samples before it can be split.

---

### `min_samples_leaf`

Minimum number of samples allowed in a leaf.

Example:

```python
DecisionTreeClassifier(
    min_samples_leaf=3
)
```

This prevents extremely tiny leaves.

---

### `max_leaf_nodes`

Controls the maximum number of leaf nodes.

---

# 12. Does a Decision Tree Need Feature Scaling?

Generally, **no**.

For example:

```text
Age = 20–60
Salary = 20,000–2,00,000
```

KNN can be affected because it calculates distances.

But a Decision Tree asks questions such as:

```text
Age < 30?
Salary < 50000?
```

It doesn't depend on Euclidean distance.

Therefore:

```text
KNN             → Scaling important
Decision Tree   → Scaling generally unnecessary
```

---

# 13. Decision Tree Classification Code

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

Evaluation:

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
```

---

# 14. Day 75 Dataset

```python
X = np.array([
    [1, 20],
    [2, 21],
    [3, 22],
    [4, 23],
    [8, 40],
    [9, 41],
    [10, 42],
    [11, 43]
])

y = np.array([
    0, 0, 0, 0,
    1, 1, 1, 1
])
```

Your output:

```text
Predictions: [0 1]
Actual:      [0 1]
Accuracy:    1.0
```

The implementation was correct. ✅

---

# 15. Decision Tree Advantages

### Easy to interpret

The rules can be visualized and understood.

### Little preprocessing

Generally doesn't require:

* Standardization
* Normalization

### Handles n

# Day 76 — Random Forest 🌲🌲

## 1. What is Ensemble Learning?

**Ensemble Learning** means combining multiple machine learning models to produce a stronger and more reliable model.

Instead of depending on one model:

> Multiple models → combine their predictions → better/stable prediction

Examples:

* Random Forest
* Gradient Boosting
* XGBoost
* AdaBoost

---

## 2. What is Random Forest?

**Random Forest is an ensemble of multiple Decision Trees.**

For classification:

> Multiple Decision Trees → predictions → majority voting → final class

Example:

```text
Tree 1 → Class 1
Tree 2 → Class 0
Tree 3 → Class 1
Tree 4 → Class 1
Tree 5 → Class 0

Final → Class 1
```

Because Class 1 received 3 votes.

---

## 3. Why Multiple Trees?

A single Decision Tree can easily overfit the training data.

Random Forest combines many trees so that:

* Individual tree errors can cancel out
* Predictions become more stable
* Variance is reduced
* Overfitting is generally reduced compared with one unrestricted tree

### Main idea

> **One tree can be unstable; many diverse trees are more robust.**

---

# 4. How does Random Forest create different trees?

Random Forest introduces randomness in two important ways.

### A. Bootstrap Sampling

Each tree is trained using a randomly sampled dataset from the original training data.

Some samples may appear multiple times, while some may not appear in tha

# Day 77 — Gradient Boosting 🚀

## 1. What is Gradient Boosting?

**Gradient Boosting** is an ensemble learning technique that combines multiple weak learners, usually Decision Trees, to create a strong model.

The key idea:

> **Trees are built sequentially, and each new tree tries to correct the errors made by the previous model.**

---

## 2. How Gradient Boosting Works

Suppose our first tree makes some mistakes.

```text
Tree 1
   ↓
Predictions
   ↓
Find errors
   ↓
Tree 2 learns from those errors
   ↓
Find remaining errors
   ↓
Tree 3 corrects more errors
   ↓
Final prediction
```

So unlike Random Forest, the trees are **not independent**.

---

## 3. Why is it called "Boosting"?

Each new weak learner improves the overall model.

```text
Weak Tree 1
     +
Weak Tree 2
     +
Weak Tree 3
     +
Weak Tree 4
     ↓
Strong Model
```

The individual trees don't need to be extremely powerful.

Their combined effect produces a strong predictor.

---

# 4. Why "Gradient"?

Gradient Boosting minimizes a **loss function**.

The gradient indicates the direction in which the loss can be reduced.

Conceptually:

```text
Current Model
     ↓
Calculate error/loss
     ↓
Find direction to reduce loss
     ↓
Train next tree
     ↓
Add tree to model
```

You don't need to implement the calculus behind this yet.

Remember:

> **Gradient → direction for reducing the loss.**

---

# 5. Random Forest vs Gradient Boosting

This is one of the most important comparisons.

| Random Forest                      | Gradient Boosting                   |
| ---------------------------------- | ----------------------------------- |
| Ensemble method                    | Ensemble method                     |
| Uses Bagging                       | Uses Boosting                       |
| Trees built independently          | Trees built sequentially            |
| Uses bootstrap samples             | New trees focus on previous errors  |
| Mainly reduces variance            | Can reduce bias and variance        |
| Majority voting for classification | Additive combination of learners    |
| Usually robust                     | Often very powerful on tabular data |

### Memory trick

>

# Day 78 — AdaBoost 🚀

## 1. What is AdaBoost?

**AdaBoost = Adaptive Boosting.**

It is an **ensemble learning algorithm** that combines multiple weak learners to create a strong model.

The key idea:

> **Each new learner gives more attention to samples that previous learners classified incorrectly.**

---

## 2. What is a Weak Learner?

A weak learner is a simple model that performs only moderately well.

AdaBoost commonly uses:

> **Decision Stumps**

A decision stump is a Decision Tree with only one level.

```python
DecisionTreeClassifier(max_depth=1)
```

Instead of one complicated tree:

```text
Deep Tree
```

AdaBoost uses:

```text
Small Tree
+
Small Tree
+
Small Tree
+
...
↓
Strong Model
```

---

# 3. Why "Adaptive"?

AdaBoost **adapts** after every learner.

Suppose the first learner makes these predictions:

```text
Sample A → Correct
Sample B → Correct
Sample C → Wrong
Sample D → Correct
```

AdaBoost increases the importance of Sample C.

The next learner pays more attention to it.

```text
Learner 1
   ↓
Find mistakes
   ↓
Increase importance of difficult samples
   ↓
Learner 2
   ↓
Find new mistakes
   ↓
Adjust importance again
```

This process continues sequentially.

---

# 4. Sample Weights

Initially, training samples can have roughly equal importance.

Conceptually:

```text
A → 1
B → 1
C → 1
D → 1
```

If C is misclassified:

```text
A → normal
B → normal
C → HIGH importance
D → normal
```

The next learner focuses more on C.

### Important:

> **AdaBoost does not s**




# Anomaly Detection using Isolation Forest

A machine learning project that detects unusual observations using **Isolation Forest**. It demonstrates data generation, preprocessing, model evaluation, model persistence, and inference on new observations using Scikit-learn.

## Project Overview

Anomaly detection identifies data points that deviate from normal patterns. It is useful in applications such as fraud detection, equipment monitoring, network security, and data quality checks.

This project generates synthetic normal observations and anomalies, trains an Isolation Forest model, evaluates its performance on held-out test data, and saves the complete preprocessing-and-model pipeline for future predictions.

## Features

- Synthetic dataset generation using NumPy and Scikit-learn
- Train/test split with stratification
- Feature scaling using `StandardScaler`
- Anomaly detection using `IsolationForest`
- Evaluation using precision, recall, F1-score, confusion matrix, and ROC-AUC
- Model persistence using Joblib
- Prediction on new observations using a saved pipeline

## Project Structure

```text
day88_anomaly_detection_project/
├── train.py
├── predict.py
├── anomaly_detector.joblib
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- NumPy
- Scikit-learn
- Joblib

## Dataset

The project uses a synthetic dataset containing:

- **500 normal observations** generated around `(0, 0)`
- **25 anomalous observations** generated from a uniform distribution between `-7` and `7` in each dimension
- **525 total observations**
- **2 numerical features** per observation

Labels:

- `0` — Normal observation
- `1` — Anomalous observation

The dataset is split into training and testing sets using a 75:25 ratio, with stratification to preserve the label proportions.

## Model Pipeline

The training pipeline consists of two stages:

1. **StandardScaler:** Standardizes the input features using statistics learned from the training data.
2. **Isolation Forest:** Identifies observations that are isolated more easily than typical observations.

The pipeline is saved using Joblib so that preprocessing and prediction can be reused consistently.

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd day88_anomaly_detection_project
```

Replace `<your-repository-url>` with your actual GitHub repository URL.

### 2. Create and activate a virtual environment (optional but recommended)

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Train and evaluate the model

```bash
python train.py
```

This generates the dataset, splits it, trains the pipeline, evaluates predictions on the test set, and saves `anomaly_detector.joblib`.

### Predict anomalies in new observations

After training:

```bash
python predict.py
```

The script loads the saved pipeline and classifies new observations as normal or anomalous.

## Evaluation Results

Example results from the training script:

| Metric | Result |
|---|---:|
| Precision | 0.429 |
| Recall | 1.000 |
| F1-score | 0.600 |
| ROC-AUC | 1.000 |

Confusion matrix:

```text
[[118   8]
 [  0   6]]
```

These results mean:

- 118 normal observations were correctly identified.
- 8 normal observations were incorrectly flagged as anomalies.
- 0 anomalies were missed.
- 6 anomalies were correctly detected.

**Note:** These results come from one synthetic dataset split and are not a guarantee of performance on real-world data. The perfect ROC-AUC reflects ranking performance on this particular test set; it does not mean every threshold-based prediction is correct.

## Limitations

- The dataset is synthetic and does not represent every real-world anomaly pattern.
- Only two numerical features are used.
- The model is trained on the training subset containing both normal and anomalous observations. A stricter novelty-detection workflow may train on normal-only data.
- Hyperparameters and decision thresholds have not been extensively tuned.
- Performance should be validated on representative, held-out real-world data before deployment.

## Future Improvements

- Compare Isolation Forest with LOF and One-Class SVM on held-out data.
- Tune model hyperparameters and decision thresholds.
- Add visualizations of normal observations and detected anomalies.
- Create a FastAPI endpoint for anomaly prediction.
- Add automated tests for preprocessing, loading, and prediction.
- Evaluate the model on a realistic labelled dataset.

## Learning Outcomes

Through this project, I practiced:

- Building a Scikit-learn `Pipeline`
- Avoiding preprocessing leakage by fitting the scaler on training data
- Evaluating anomaly detection with classification metrics
- Saving and loading ML models using Joblib
- Running inference on new data without retraining

## Author

**Surya Rathore**

B.Tech — Smart Manufacturing  
IIITDM Jabalpur

---

*Created as part of my 90-day Python Development, FastAPI, and Machine Learning roadmap.*
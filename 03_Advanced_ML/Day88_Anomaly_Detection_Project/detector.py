from pathlib import Path

import joblib
import numpy as np

MODEL_PATH = Path(__file__).resolve().parent / "anomaly_detector.joblib"


def load_model(path=MODEL_PATH):
    """Load the saved preprocessing and model pipeline."""
    return joblib.load(path)


def predict_observations(model, data):
    """Return 0 for normal observations and 1 for anomalies."""
    X = np.asarray(data, dtype=float)

    if X.ndim != 2:
        raise ValueError("Input must be a 2D array.")

    if X.shape[1] != 2:
        raise ValueError("Expected exactly 2 features per observation.")

    if X.shape[0] == 0:
        raise ValueError("Input must contain at least one observation.")

    if not np.isfinite(X).all():
        raise ValueError("Input contains NaN or infinite values.")

    raw_predictions = model.predict(X)
    return (raw_predictions == -1).astype(int)

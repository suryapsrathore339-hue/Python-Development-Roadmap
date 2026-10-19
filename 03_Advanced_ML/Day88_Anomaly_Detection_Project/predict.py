import numpy as np
import joblib 

pipeline=joblib.load("anomaly_detector.joblib")

new_data=np.array([
    [0.2,-0.3],
    [1.0, 0.5],
    [7.0, 7.0],
    [-8.0, 8.0],
])

raw_predictions=pipeline.predict(new_data)
anomaly_scores=-pipeline.decision_function(new_data)

predictions = (raw_predictions == -1).astype(int)

for point,prediction,score in zip(
    new_data,predictions,anomaly_scores
):
    label="ANOMALY" if prediction==1 else "NORMAL"
    print(
        f"Point: {point},Prediction:{label},"
        f"Anomaly score:{score:.4f}"
    )

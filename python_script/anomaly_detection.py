import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest
from data_validation import validate_data

#function to calculate z-score anomalies
def zscore_anomaly(data, threshold):
    #calculate Z-scores for each metric
    z_scores = np.abs(zscore(data))
    #Flag anomalies where the z-score exceeds the threshold
    return z_scores > threshold

#function to simulate real-time anomaly detection using Z-score and Isolation Forest
def realtime_anomaly_detection_iforest(data_stream, zscore_threshold, cont, state, num):
    #Initialize Isolation Forest
    isolation_forest = IsolationForest(random_state=state, contamination=cont)

    #Store the result of anomaly flags
    anomalies = []

    #Fit the isolation forest model on the entire dataset (batch approach)
    iforest_preds = isolation_forest.fit_predict(data_stream[['metric_1', 'metric_2', 'metric_3']])

    #Process the data stream in real-time
    for i, row in data_stream.iterrows():
        #Extract current data point for each metric
        metric_1, metric_2, metric_3 = row['metric_1'], row['metric_2'], row['metric_3']

        #Z-score based anomaly detection
        current_data = np.array([metric_1, metric_2, metric_3])
        z_anomalies = zscore_anomaly(current_data, zscore_threshold)

        #Isolation Forest anomaly detection
        isolation_forest_anomaly = iforest_preds[i] == -1

        #Combine the results: Z-score anomalies and Isolation Forest
        combined_anomaly = z_anomalies.any() or isolation_forest_anomaly

        #Store the anomaly status for each timestamp
        anomalies.append({
            'timestamp': row['timestamp'],
            'metric_1_anomaly': z_anomalies[0],
            'metric_2_anomaly': z_anomalies[1],
            'metric_3_anomaly': z_anomalies[2],
            'isolation_forest_anomaly': isolation_forest_anomaly,
            'combined_anomaly': combined_anomaly
        })

        #Handle errors and unseen data
        try:
            validate_data([metric_1, metric_2, metric_3], num)
        except ValueError as e:
            print(f"Data validation error at timestamp {row['timestamp']}:{e}")

    return pd.DataFrame(anomalies)
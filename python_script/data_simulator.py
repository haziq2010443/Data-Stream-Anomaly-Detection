import numpy as np
import pandas as pd
import time

def simulate_data_stream(num_points, seasonal_frequency, seasonal_amplitude, noise_level):
    timestamps = []
    metric_1 = []
    metric_2 = []
    metric_3 = []

    for t in range(num_points):
        timestamps.append(t)

        metric_1_value = (0.01 * t) + seasonal_amplitude * np.sin(2 * np.pi * t / seasonal_frequency) + np.random.normal(0, noise_level)
        metric_1.append(metric_1_value)
        
        metric_2_value = (0.005 * t) + seasonal_amplitude * np.sin(2 * np.pi * t / (seasonal_frequency * 1.5)) + np.random.normal(0, noise_level)
        metric_2.append(metric_2_value)
        
        metric_3_value = (-0.008 * t) + seasonal_amplitude * np.sin(2 * np.pi * t / (seasonal_frequency * 2)) + np.random.normal(0, noise_level)
        metric_3.append(metric_3_value)

        time.sleep(0.01)

    data_stream = pd.DataFrame({
        'timestamp': timestamps,
        'metric_1': metric_1,
        'metric_2': metric_2,
        'metric_3': metric_3
    })

    return data_stream
#Importing necessary libraries
import matplotlib.pyplot as plt

#Importing functions
from data_simulator import simulate_data_stream
from anomaly_detection import realtime_anomaly_detection_iforest
from visualization import plot_interactive_anomalies, plot_anomalies

#Global Variables For tuning purposes
NUM = 1000
FREQ = 100
AMP = 10
LVL = 2

THRES = 3
CONTAMINATION = 0.05
STATE = 42

data_stream = simulate_data_stream(NUM, FREQ, AMP, LVL)

#Plot Test the data stream created
plt.figure(figsize=(10,6))
plt.plot(data_stream['timestamp'], data_stream['metric_1'], label=' Metric 1')
plt.plot(data_stream['timestamp'], data_stream['metric_2'], label=' Metric 2')
plt.plot(data_stream['timestamp'], data_stream['metric_3'], label=' Metric 3')
plt.title('Simulated Real-Time Sequence of Floating-Point Numbers')
plt.xlabel('Time')
plt.ylabel('Metric Value')
plt.legend()
plt.show()

#detecting anomaly on data stream
anomaly_results = realtime_anomaly_detection_iforest(data_stream, THRES, CONTAMINATION, STATE, NUM)

#visualize the data stream
#interactive plot
plot_interactive_anomalies(data_stream, anomaly_results)
plot_anomalies(data_stream, anomaly_results)
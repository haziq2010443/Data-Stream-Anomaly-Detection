import plotly.graph_objs as go
import plotly.io as pio
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots

pio.renderers.default = 'browser'

#function to create an interactive plots of data stream and anomalies using Plotly
def plot_interactive_anomalies(data_stream, anomaly):
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                        vertical_spacing=0.1,
                        subplot_titles=("Metric 1", "Metric 2", "Metric 3"))
    
    #Plot each metric in the data stream
    for metric_idx, metric_name in enumerate(['metric_1', 'metric_2', 'metric_3'], start=1):
        fig.add_trace(go.Scatter(x=data_stream['timestamp'],
                                 y=data_stream[metric_name],
                                 mode='lines',
                                 name=f'{metric_name} stream'),
                      row=metric_idx, col=1)
        
        #Highlight the anomalies
        fig.add_trace(go.Scatter(x=anomaly['timestamp'][anomaly['combined_anomaly']],
                                 y=data_stream[metric_name][anomaly['combined_anomaly']],
                                 mode='markers',
                                 marker=dict(color='red', size=8),
                                 name=f'{metric_name} anomalies'),
                      row=metric_idx, col=1)

    #Update layout for interactivity
    fig.update_layout(height=800, width=1000,
                      title_text="Real-Time Data Stream with Anomalies",
                      showlegend=True)

    #Add axis labels
    fig.update_xaxes(title_text="Time", row=3, col=1)
    fig.update_yaxes(title_text="Value")

    fig.show()

# Function to plot data stream with anomalies using Matplotlib
def plot_anomalies(data_stream, anomaly_results):
    plt.figure(figsize=(12, 6))

    # Plot each metric
    plt.plot(data_stream['timestamp'], data_stream['metric_1'], label='Metric 1', color='blue')
    plt.plot(data_stream['timestamp'], data_stream['metric_2'], label='Metric 2', color='orange')
    plt.plot(data_stream['timestamp'], data_stream['metric_3'], label='Metric 3', color='green')

    # Highlight anomalies
    for metric_name in ['metric_1', 'metric_2', 'metric_3']:
        anomalies = anomaly_results['combined_anomaly']
        anomaly_timestamps = data_stream['timestamp'][anomalies]
        anomaly_values = data_stream[metric_name][anomalies]
        plt.scatter(anomaly_timestamps, anomaly_values, color='red', label=f'{metric_name} Anomalies', s=50)

    # Customize the plot
    plt.title('Real-Time Data Stream with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()

    # Show the plot
    plt.show()
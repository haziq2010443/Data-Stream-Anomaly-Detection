# Efficient Data Stream Anomaly Detection

This project focuses on developing Python scripts capable of detecting anomalies in a continuous data stream. This stream, simulating real-time sequences of floating-point numbers, could represent various metrics such as financial transactions or system metrics. The focus will be on identifying unusual patterns, such as exceptionally high values or deviations from the norm.

## Project Overview

In this project, I simulate a real-time sequence of multivariate data (e.g., financial transactions or system metrics) that incorporates regular patterns, seasonal elements, and random noise. The hybrid algorithm is designed to:
- **Z-Score:** Detect anomalies that deviate significantly from the statistical norm.
- **Isolation Forest:** Identify more complex anomalies by isolating data points in a feature space.

The algorithm is designed to handle errors for unseen data and ensure data validation at each step. The real-time detection mechanism can be run both in Jupyter notebooks and as Python scripts via IDEs.

## Features
- **Simulate Real-Time Data Streams:** Generate multivariate data streams with floating-point metrics.
- **Z-Score Anomaly Detection:** Detect point anomalies based on deviations from the mean.
- **Isolation Forest Detection:** Identify complex anomalies using machine learning.
- **Real-Time Processing:** Handle continuous data streams with built-in error handling and data validation.

## Project Structure

The repository contains the following files:
- `notebooks/` - Jupyter notebooks to run the code interactively.
- `scripts/` - Python scripts to run the algorithm in a standalone manner.
- `requirements.txt` - Lists all required libraries to replicate the environment.
- `README.md` - This document.

## Installation and Setup

### Clone the repository:
First, clone the repository to your local machine using:
```bash
git clone https://github.com/haziq2010443/Data-Stream-Anomaly-Detection.git
```
### Environment Setup:
It is recommended to set up a virtual environment to manage dependencies.

1. Create a virtual environment:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
- On macOS/Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Project

### Option 1: Run via Jupyter Notebook
1. Navigate to the `notebooks/` folder.
2. Open the provided Jupyter notebook (`Efficient-Data-Stream-Anomaly-Detection.ipnyb`).
3. Run the cells interactively to simulate the data stream and perform real-time anomaly detection.

### Option 2: Run Python Scripts vis IDE
1. Navigate to the `scripts/` folder.
2. Open your preferred IDE (e.g., **PyCharm**, **VS Code**).
3. Open the script `main.py`.
4. Run the script in the IDE to simulate the data stream and detect anomalies in real time.

## Dependencies
The project requires the following Python libraries (listed in `requirements.txt`):
- `numpy`
- `pandas`
- `scikit-learn`
- `scipy`
- `matplotlib`
- `plotly`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

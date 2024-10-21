import numpy as np

#function to validate data
def validate_data(data, num_points):
    if any(np.isnan(data)):
        raise ValueError("Data contains NaN values")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Data contains invalid types")
    if any(x < -num_points or x > num_points for x in data):
        raise ValueError("Data contains values outside the expected range of 1000")
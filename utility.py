import numpy as np
import datetime


def generate_iot_data():
    # Generate random IoT data
    # make sure you save booleans, datetimes, as strings otherwise they will not be serializable to json format
    # your script will break if you don't do this - check Timestamp, Motion Detected, Status
    # notice multiple ways of string conversion from other data types
    # also notice the specific data types for each data point - some numbers are saved as strings
    iot_data = {
        "Device ID": np.random.randint(1000, 9999),  # Random 4-digit device ID
        "Timestamp": f"{datetime.datetime.now()}",        # Current timestamp
        # Temperature in Celsius
        "Temperature": float(np.random.uniform(-20, 50)),
        # Humidity in percentage
        "Humidity": float(np.random.uniform(0, 100)),
        # Battery level in percentage
        "Battery Level": float(np.random.uniform(0, 100)),
        # Signal strength in dBm
        "Signal Strength": float(np.random.uniform(-100, 0)),
        # Random boolean for motion detection
        "Motion Detected": str(np.random.choice([True, False])),
        # Light level in lux
        "Light Level": float(np.random.uniform(0, 1000)),
        # Atmospheric pressure in hPa
        "Pressure": float(np.random.uniform(900, 1100)),
        # Random status
        "Status": np.random.choice(['active', 'inactive', 'error']),
        # Random event count
        "Event Count": float(np.random.randint(0, 100)),
        # Random error code
        "Error Code": str(np.random.choice([0, 1, 2, 3, 99])),
        "Data Usage": float(np.random.uniform(0, 500))  # Data usage in MB
    }
    return iot_data

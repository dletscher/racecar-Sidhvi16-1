import json
import os

DATA_FILE = "MyData.json"

# Default learned coefficients (change these to your agent’s starting params)
default_data = {
    "steering_gain": 1.0,
    "smoothing_alpha": 0.85,
    "steer_right_threshold": 0.4,
    "steer_left_threshold": -0.4,
    "brake_steer_threshold": 0.6,
    "velocity_accel_threshold": 3.8,
    "front_clearance_accel": 0.7,
    "min_clearance_brake": 0.5
}

def save_data(data):
    """Save learned coefficients to disk."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    """Load learned coefficients from disk, or return defaults if none saved."""
    if not os.path.exists(DATA_FILE):
        return default_data.copy()
    with open(DATA_FILE, "r") as f:
        return json.load(f)

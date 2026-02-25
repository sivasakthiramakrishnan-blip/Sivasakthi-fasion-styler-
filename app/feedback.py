import json
import os

FEEDBACK_FILE = "feedback.json"

def save_feedback(outfit_name, liked):
    data = []
    
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as f:
            data = json.load(f)
    
    data.append({
        "outfit": outfit_name,
        "liked": liked
    })
    
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=2)
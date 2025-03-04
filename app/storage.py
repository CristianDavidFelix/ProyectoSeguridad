import csv
from datetime import datetime

def save_event(event):
    with open("data/attacks.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            event["timestamp"],
            event["src_ip"],
            event["dst_ip"],
            event["src_port"],
            event["dst_port"],
            event["type"]
        ])
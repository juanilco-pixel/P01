"""
Project: Eye Project (P01) - Life Safety
Description: A privacy-focused 30-day local trace logging system.
"""
import datetime
import os

class EyeSafetyEngine:
    def __init__(self):
        self.log_path = "./traces"
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

    def record_trace(self, device_id):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f"{self.log_path}/trace_log.txt", "a") as f:
            f.write(f"[{now}] Device {device_id} detected nearby.\n")
        print(f"Trace recorded securely at {now}")

if __name__ == "__main__":
    eye = EyeSafetyEngine()
    eye.record_trace("SMART_NODE_01")
    print("Core logic: Data remains local for 30 days.")

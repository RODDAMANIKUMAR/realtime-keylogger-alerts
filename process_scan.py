# process_scan.py
import psutil

# Define suspicious keywords in process names
SUSPICIOUS_KEYWORDS = ["keylog", "logger", "hook", "spy", "capture"]

def find_suspicious_processes():
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name'].lower()
            for word in SUSPICIOUS_KEYWORDS:
                if word in pname:
                    suspicious.append(proc)
        except:
            continue
    return suspicious
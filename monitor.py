# monitor.py
import keyboard
import win32gui
import time
from alerts import show_notification, send_email_alert
from process_scan import find_suspicious_processes

# Helper to get the currently focused window
def get_foreground_window_title():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

# Callback for keypress
def on_key_press(e):
    window = get_foreground_window_title()
    if not window.strip():
        print("[ALERT] Keystroke with no active window!")
        show_notification("Suspicious Activity", "Keystroke detected without active window.")
        send_email_alert("Suspicious Keylogging Alert", "Keystroke detected with no window.")
    
    suspicious = find_suspicious_processes()
    if suspicious:
        for proc in suspicious:
            msg = f"Suspicious process: {proc.name()} (PID: {proc.pid})"
            print("[ALERT]", msg)
            show_notification("Suspicious Process", msg)
            send_email_alert("Suspicious Keylogger Process", msg)

# Main function
def run_monitor():
    keyboard.on_press(on_key_press)
    print("[*] Monitoring started. Press keys to test...")
    keyboard.wait()

if __name__ == "__main__":
    run_monitor()

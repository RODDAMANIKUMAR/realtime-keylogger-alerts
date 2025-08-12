print("Keylogger Alert System Started!")

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



# alerts.py
from win10toast import ToastNotifier
import smtplib
from email.message import EmailMessage

# Local popup
def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=5)

# Email alert (configure your email details!)
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "admin_email@example.com"

def send_email_alert(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("[+] Email alert sent.")
    except Exception as e:
        print("[-] Failed to send email:", e)
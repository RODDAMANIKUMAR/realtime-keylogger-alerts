#  Keylogger Alert System

A Python-based system that logs keystrokes, detects suspicious activity, and sends real-time alerts via **desktop notifications** and **email**.

>  **Disclaimer**: This project is intended for educational and ethical use only. Do **not** use this software to monitor others without consent.

##  Project Structure
keylogger_alert_system/
├── alerts.py # Handles desktop and email notifications
├── main.py # (Optional) Script to tie all modules together
├── monitor.py # Future use: can monitor system behavior or active processes
├── process_scan.py # Scans for suspicious system processes (optional feature)
├── test_keylogger.py # Main script: logs keystrokes and detects suspicious input
├── keylogger_result.png # Screenshot showing example output or alerts
└── README.md # Project documentation (this file)

##  Features

-  Real-time keystroke logging using `pynput`
-  Detects suspicious words like:
  - `password`
  - `admin`
  - `nginx`
  - `mypasswordis123`
-  Shows Windows desktop notifications using `win10toast`
-  Sends email alerts via Gmail SMTP

##  Requirements

Make sure Python 3.6+ is installed.

Install required Python packages:

```bash
pip install pynput win10toast

✉  Email Alert Configuration
Open alerts.py and configure your email details:
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use Gmail App Password
TO_EMAIL = "recipient@example.com"

##  How to Run
From your terminal:
bash
Copy
Edit
python test_keylogger.py



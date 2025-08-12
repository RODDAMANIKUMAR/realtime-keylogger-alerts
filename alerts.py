# alerts.py
from win10toast import ToastNotifier
import smtplib
from email.message import EmailMessage

# Local popup
def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=5)

# Email alert (configure your email details!)
EMAIL_ADDRESS = "spykeemani1124@gmail.com"
EMAIL_PASSWORD = "iapl ezzo ivov chkw"
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




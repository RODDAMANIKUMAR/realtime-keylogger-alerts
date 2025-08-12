from pynput import keyboard
from alerts import show_notification, send_email_alert

# Define what words you consider suspicious
SUSPICIOUS_WORDS = ['password', 'admin', 'nginx', 'mypasswordis123']
typed_keys = []

def on_press(key):
    try:
        # Only process printable characters
        if hasattr(key, 'char') and key.char is not None:
            typed_keys.append(key.char)

            # Keep last 30 characters
            if len(typed_keys) > 30:
                typed_keys.pop(0)

            # Convert buffer to string and check for suspicious words
            current_string = ''.join(typed_keys).lower()
            for word in SUSPICIOUS_WORDS:
                if word in current_string:
                    print(f"[!] Suspicious word detected: {word}")

                    # 🔔 Desktop notification
                    show_notification("Keylogger Alert", f"Suspicious word detected: {word}")

                    # 💌 Email alert
                    send_email_alert(
                        subject="🚨 Suspicious Activity Detected",
                        body=f"The user typed the suspicious word: {word}"
                    )

                    typed_keys.clear()
                    break
    except Exception as e:
        print(f"[ERROR] {e}")

# Start listening for keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

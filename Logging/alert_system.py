import os
import random
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sklearn.ensemble import IsolationForest
import numpy as np

# Configuration constants
SENDGRID_API_KEY = "SG.8VNJnn8aTkCb_u4Rq_ZOzQ.k2KrpXN39OC6VCcLxY9jx1ZxnUkjV-brY"  # Replace with your SendGrid API key
RECEIVER_EMAIL = "piyushmodgil9@gmail.com"  # The email to receive alerts
SENDER_EMAIL = "spaceanomalydetect@gmail.com"  # Replace with your sender email
ANOMALY_THRESHOLD = -0.5  # Threshold for anomaly detection
ANOMALY_COUNT_ALERT = 10  # Number of anomalies before sending an alert

class AnomalyDetector:
    def __init__(self, threshold):
        self.threshold = threshold
        self.model = IsolationForest(n_estimators=200, contamination=0.05, random_state=42)
        self.anomaly_count = 0
        self.anomalies = []  # Stores details of anomalies

    def train_model(self):
        normal_data = np.random.randint(low=500, high=1500, size=(1000, 1))
        self.model.fit(normal_data)

    def detect_anomaly(self, value):
        score = self.model.decision_function([[value]])[0]
        if score < self.threshold:
            self.anomaly_count += 1
            self.anomalies.append({"packet_count": value, "score": score})
            return True
        return False

    def reset_anomaly_count(self):
        self.anomaly_count = 0
        self.anomalies = []  # Clear anomaly details after sending email

class EmailNotifier:
    def __init__(self, api_key, sender_email, receiver_email):
        self.api_key = api_key
        self.sender_email = sender_email
        self.receiver_email = receiver_email

    def send_email(self, subject, content):
        try:
            message = Mail(
                from_email=self.sender_email,
                to_emails=self.receiver_email,
                subject=subject,
                html_content=content  # Changed to HTML format for better visualization
            )
            sg = SendGridAPIClient(self.api_key)
            sg.send(message)
            print(f"Email sent: {subject}")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")

def format_anomaly_email(anomalies):
    """
    Formats the list of anomalies into a table-like HTML content for email.
    """
    html_content = "<h3>Anomalies Detected</h3>"
    html_content += "<table border='1' style='border-collapse: collapse; width: 100%;'>"
    html_content += "<tr><th>Packet Count</th><th>Anomaly Score</th></tr>"
    for anomaly in anomalies:
        html_content += f"<tr><td>{anomaly['packet_count']}</td><td>{anomaly['score']:.4f}</td></tr>"
    html_content += "</table>"
    html_content += f"<p>Total anomalies detected: {len(anomalies)}</p>"
    return html_content

def main():
    detector = AnomalyDetector(threshold=ANOMALY_THRESHOLD)
    detector.train_model()
    notifier = EmailNotifier(SENDGRID_API_KEY, SENDER_EMAIL, RECEIVER_EMAIL)

    print("Monitoring started...")

    while True:
        packet_count = random.randint(300, 2000)  # Simulated incoming packet count
        print(f"Incoming packet count: {packet_count}")

        if detector.detect_anomaly(packet_count):
            print(f"Anomaly detected! Packet count: {packet_count}")

        if detector.anomaly_count >= ANOMALY_COUNT_ALERT:
            formatted_email = format_anomaly_email(detector.anomalies)
            notifier.send_email(
                subject="Multiple Anomalies Detected Alert",
                content=formatted_email
            )
            detector.reset_anomaly_count()

        time.sleep(1)  # Adjust monitoring frequency as needed

if __name__ == "__main__":
    main()

import os
import random
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sklearn.ensemble import IsolationForest
import numpy as np

# Configuration constants
SENDGRID_API_KEY = "SG.8VNJnn8aTkCb_u4Rq_ZOzQ.k2KrpXN39OC6VCcLxY9jx1ZxnUkjV-brY"  # Replace with your SendGrid API key
RECEIVER_EMAIL = "piyushmodgil9@gmail.com"  # The email address to receive anomaly alerts
SENDER_EMAIL = "spaceanomalydetect@gmail.com"  # Replace with your sender email
ANOMALY_THRESHOLD = -0.5  # Threshold value for anomaly detection
ANOMALY_COUNT_ALERT = 10  # Number of anomalies before sending an alert email

# Anomaly detection class that uses Isolation Forest for detecting anomalies in packet counts
class AnomalyDetector:
    def __init__(self, threshold):
        self.threshold = threshold
        self.model = IsolationForest(n_estimators=200, contamination=0.05, random_state=42)  # Isolation Forest model setup
        self.anomaly_count = 0  # Counter to track the number of detected anomalies
        self.anomalies = []  # List to store details of detected anomalies

    # Method to train the model with normal data (simulated packet counts)
    def train_model(self):
        normal_data = np.random.randint(low=500, high=1500, size=(1000, 1))  # Simulate normal traffic
        self.model.fit(normal_data)

    # Method to detect anomalies based on a new packet count value
    def detect_anomaly(self, value):
        score = self.model.decision_function([[value]])[0]  # Get the anomaly score for the packet count
        if score < self.threshold:  # If score is below threshold, it's an anomaly
            self.anomaly_count += 1  # Increment anomaly counter
            self.anomalies.append({"packet_count": value, "score": score})  # Store anomaly details
            return True
        return False

    # Method to reset the anomaly count and clear the anomaly list after an email is sent
    def reset_anomaly_count(self):
        self.anomaly_count = 0
        self.anomalies = []  # Clear anomaly details after sending an email

# Email notification class for sending alert emails using SendGrid
class EmailNotifier:
    def __init__(self, api_key, sender_email, receiver_email):
        self.api_key = api_key  # SendGrid API key
        self.sender_email = sender_email  # Sender's email address
        self.receiver_email = receiver_email  # Receiver's email address

    # Method to send an email with a subject and HTML content
    def send_email(self, subject, content):
        try:
            # Create the email message
            message = Mail(
                from_email=self.sender_email,
                to_emails=self.receiver_email,
                subject=subject,
                html_content=content  # HTML content for better email formatting
            )
            sg = SendGridAPIClient(self.api_key)  # SendGrid client initialization
            sg.send(message)  # Send the email
            print(f"Email sent: {subject}")  # Log the email sending status
        except Exception as e:
            print(f"Failed to send email: {str(e)}")  # Handle any exceptions during email sending

# Method to format anomaly details into an HTML table for the email content
def format_anomaly_email(anomalies):
    """
    Formats the list of anomalies into a table-like HTML content for email.
    """
    html_content = "<h3>Anomalies Detected</h3>"  # Header for the email
    html_content += "<table border='1' style='border-collapse: collapse; width: 100%;'>"  # Start the table
    html_content += "<tr><th>Packet Count</th><th>Anomaly Score</th></tr>"  # Table headers
    for anomaly in anomalies:
        html_content += f"<tr><td>{anomaly['packet_count']}</td><td>{anomaly['score']:.4f}</td></tr>"  # Table rows with anomaly data
    html_content += "</table>"
    html_content += f"<p>Total anomalies detected: {len(anomalies)}</p>"  # Total count of detected anomalies
    return html_content

# Main monitoring loop
def main():
    # Initialize the anomaly detector and train the model
    detector = AnomalyDetector(threshold=ANOMALY_THRESHOLD)
    detector.train_model()

    # Initialize the email notifier with the necessary configuration
    notifier = EmailNotifier(SENDGRID_API_KEY, SENDER_EMAIL, RECEIVER_EMAIL)

    print("Monitoring started...")

    # Infinite loop to simulate real-time packet monitoring
    while True:
        # Simulate an incoming packet count (in real-world scenarios, this would be actual data)
        packet_count = random.randint(300, 2000)
        print(f"Incoming packet count: {packet_count}")

        # Check if the packet count is anomalous
        if detector.detect_anomaly(packet_count):
            print(f"Anomaly detected! Packet count: {packet_count}")

        # If the number of anomalies reaches the threshold, send an email alert
        if detector.anomaly_count >= ANOMALY_COUNT_ALERT:
            formatted_email = format_anomaly_email(detector.anomalies)  # Format the anomaly details
            notifier.send_email(
                subject="Multiple Anomalies Detected Alert",  # Subject of the email
                content=formatted_email  # Email content with anomaly details
            )
            detector.reset_anomaly_count()  # Reset anomaly count after sending the alert

        # Pause for 1 second before the next packet count check (adjustable based on monitoring frequency)
        time.sleep(1)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

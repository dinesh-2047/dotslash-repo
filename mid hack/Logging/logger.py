import logging
from datetime import datetime

# Configure logging to write messages to a log file and set the logging level to INFO
logging.basicConfig(
    filename='anomaly_detection.log',  # Log file name where messages will be saved
    level=logging.INFO,  # Set the logging level to INFO to capture informational messages
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format, including timestamp and log level
)

# Function to log anomaly detection events
def log_anomaly_detection(anomaly_description, packet_count):
    """
    Logs the details of an anomaly detection event including the description and packet count.
    """
    message = f"Anomaly Detected: {anomaly_description} | Packet Count: {packet_count}"  # Prepare the log message
    logging.info(message)  # Write the message to the log file
    print(message)  # Also print the message to the console for real-time monitoring

# Function to log when an email alert is sent
def log_email_sent(anomaly_description, receiver_email):
    """
    Logs when an email alert is sent for a detected anomaly.
    """
    message = f"Alert Email Sent: {anomaly_description} to {receiver_email}"  # Prepare the log message
    logging.info(message)  # Write the message to the log file
    print(message)  # Also print the message to the console for real-time monitoring

# Function to log packet information
def log_packet_info(packet_count, packet_details):
    """
    Logs the packet count and details for monitoring purposes.
    """
    message = f"Packet Count: {packet_count} | Details: {packet_details}"  # Prepare the log message
    logging.info(message)  # Write the message to the log file
    print(message)  # Also print the message to the console for real-time monitoring

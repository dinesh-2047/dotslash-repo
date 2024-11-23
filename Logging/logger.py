import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='anomaly_detection.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_anomaly_detection(anomaly_description, packet_count):
    message = f"Anomaly Detected: {anomaly_description} | Packet Count: {packet_count}"
    logging.info(message)
    print(message)

def log_email_sent(anomaly_description, receiver_email):
    message = f"Alert Email Sent: {anomaly_description} to {receiver_email}"
    logging.info(message)
    print(message)

def log_packet_info(packet_count, packet_details):
    message = f"Packet Count: {packet_count} | Details: {packet_details}"
    logging.info(message)
    print(message)

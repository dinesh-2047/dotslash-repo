import numpy as np
from sklearn.ensemble import IsolationForest
import time
import random
import logging
from collections import deque

# Class to handle packet metadata such as protocol, source and destination IPs, and ports
class PacketMetadataGenerator:
    def __init__(self):
        # Define available network protocols and common ports
        self.protocols = ["TCP", "UDP", "HTTP", "HTTPS", "FTP", "SSH", "DNS"]
        self.ports = [80, 443, 53, 22, 21, 8080]

    # Method to generate the metadata of a network packet
    def generate_packet_metadata(self):
        # Randomly select a protocol
        protocol = random.choice(self.protocols)
        # Generate source and destination IP addresses in a common private IP range
        src_ip = f"192.168.{random.randint(0,255)}.{random.randint(0,255)}"
        dest_ip = f"10.0.{random.randint(0,255)}.{random.randint(0,255)}"
        # Select random source port and destination port
        src_port = random.randint(1024, 65535)
        dest_port = random.choice(self.ports)
        # Set packet size to 0 for this implementation
        packet_size = 0
        # Randomly generate latency between 0.1 and 50 ms
        latency = round(random.uniform(0.1, 50.0), 3)

        # Return a dictionary containing the generated metadata
        return {
            "protocol": protocol,
            "src_ip": src_ip,
            "dest_ip": dest_ip,
            "src_port": src_port,
            "dest_port": dest_port,
            "packet_size": packet_size,
            "latency": latency
        }

# Class to detect anomalies in network traffic based on packet count
class AnomalyDetector:
    def __init__(self, threshold, memory_window=100):
        # Set the threshold for anomaly detection
        self.threshold = threshold
        # Initialize the Isolation Forest model with specific configuration
        self.model = IsolationForest(n_estimators=200, contamination=0.05, random_state=42, verbose=1)
        # Store the historical packet data in a deque with a fixed memory window size
        self.packet_history = deque(maxlen=memory_window)
        # Define the threshold for variance to trigger model retraining
        self.packet_variance_threshold = 1000
        # Define the interval for retraining the model
        self.retrain_interval = 50
        # Counter to keep track of the number of packets processed
        self.detection_counter = 0

    # Method to retrain the model adaptively based on packet data variance
    def adaptive_training(self):
        # Retrain the model if the variance of the packet history exceeds the threshold
        if len(self.packet_history) >= self.packet_history.maxlen:
            data_variance = np.var(self.packet_history)
            if data_variance > self.packet_variance_threshold:
                # Fit the model using the current packet history data
                self.model.fit(np.array(self.packet_history).reshape(-1, 1))
                logging.info("Model retrained based on new packet variance.")

    # Method to detect anomalies in packet traffic based on the packet count
    def detect_anomaly(self, packet_count):
        # Append the new packet count to the history
        self.packet_history.append(packet_count)
        # Increment the detection counter to track the number of packets processed
        self.detection_counter += 1
        # Retrain the model periodically based on the defined interval
        if self.detection_counter % self.retrain_interval == 0:
            self.adaptive_training()

        # Generate a set of normal data for training the model
        normal_data = np.random.randint(low=500, high=1500, size=(1000, 1))
        # Fit the model using normal data to ensure consistent detection
        self.model.fit(normal_data)
        # Calculate the anomaly score based on the packet count
        anomaly_score = self.model.decision_function([[packet_count]])[0]
        # If the anomaly score is below the threshold, classify it as an anomaly
        if anomaly_score < self.threshold:
            return self.categorize_anomaly(packet_count)
        return None

    # Method to categorize the detected anomaly based on packet count
    def categorize_anomaly(self, packet_count):
        if packet_count < 500:
            return f"Anomaly: Low Traffic Spike. Count: {packet_count}"
        elif packet_count > 1500:
            return f"Anomaly: High Traffic Spike. Count: {packet_count}"
        return f"Anomaly: Unusual Traffic Pattern. Count: {packet_count}"

# Class for managing and processing network traffic
class TrafficSimulator:
    def __init__(self):
        # Initialize the packet metadata generator to produce metadata for each packet
        self.metadata_generator = PacketMetadataGenerator()

    # Method to simulate the receipt of network traffic packets
    def simulate_packet(self):
        # Randomly select a packet count within a specified range
        packet_count = random.randint(300, 2000)
        # Generate the metadata for the packet
        metadata = self.metadata_generator.generate_packet_metadata()

        # If the packet size is 0, display the packet details and return the packet count
        if metadata["packet_size"] == 0:
            self.display_packet_details(metadata, packet_count)
            return packet_count
        return None

    # Method to display details of the generated packet
    def display_packet_details(self, metadata, packet_count):
        print(f"Packet Details: [Protocol: {metadata['protocol']}] "
              f"[Source IP: {metadata['src_ip']}] "
              f"[Dest IP: {metadata['dest_ip']}] "
              f"[Src Port: {metadata['src_port']}] "
              f"[Dst Port: {metadata['dest_port']}]")
        print(f"Packet Count: {packet_count}, Packet Size: {metadata['packet_size']}B, Latency: {metadata['latency']}ms")

# Class for analyzing packets and detecting anomalies
class PacketAnalyzer:
    def __init__(self, threshold=-0.3):
        # Initialize the anomaly detector with a defined threshold
        self.detector = AnomalyDetector(threshold)

    # Method to analyze the packet and detect any anomalies
    def analyze_packet(self, packet_count):
        if packet_count is not None:
            # Pass the packet count to the anomaly detector
            result = self.detector.detect_anomaly(packet_count)
            # If an anomaly is detected, print the result
            if result:
                print(f"Detection Result: {result}\n")

# Class for managing and reporting detected anomalies
class EnhancedReporting:
    def __init__(self):
        # List to store reported anomalies
        self.reported_anomalies = []

    # Method to report a detected anomaly
    def report_anomaly(self, anomaly):
        self.reported_anomalies.append(anomaly)
        # Print the reported anomaly for immediate review
        print(f"Reporting Anomaly: {anomaly}")

    # Method to summarize all the detected anomalies
    def summarize_anomalies(self):
        # Print the total number of anomalies detected
        print(f"Total Anomalies Detected: {len(self.reported_anomalies)}")
        # Print the details of each anomaly
        for anomaly in self.reported_anomalies:
            print(anomaly)

# Class for real-time packet inspection and analysis
class RealTimePacketInspector:
    def __init__(self):
        # Initialize components for packet simulation, analysis, and reporting
        self.traffic_simulator = TrafficSimulator()
        self.analyzer = PacketAnalyzer()
        self.reporting = EnhancedReporting()

    # Method to continuously monitor and analyze network traffic in real-time
    def run_inspection(self):
        while True:
            # Simulate the receipt of a packet
            packet_count = self.traffic_simulator.simulate_packet()
            if packet_count is not None:
                # Analyze the packet for anomalies
                anomaly_result = self.analyzer.analyze_packet(packet_count)
                if anomaly_result:
                    # Report the detected anomaly
                    self.reporting.report_anomaly(anomaly_result)
            # Add a small delay to mimic real-time processing
            time.sleep(random.uniform(0.3, 1.5))

# Configure logging for better visibility of the system's operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Main entry point for executing the packet inspection system
if __name__ == "__main__":
    # Initialize and start the real-time packet inspector
    inspector = RealTimePacketInspector()
    inspector.run_inspection()


import numpy as np
from sklearn.ensemble import IsolationForest
import time
import random
import logging
from collections import deque
from flask import Flask, jsonify, render_template

# Flask web framework initialization
app = Flask(__name__)

# Class for generating packet metadata such as protocol, IP addresses, and ports
class PacketMetadataGenerator:
    def __init__(self):
        # List of protocols and commonly used ports
        self.protocols = ["TCP", "UDP", "HTTP", "HTTPS", "FTP", "SSH", "DNS"]
        self.ports = [80, 443, 53, 22, 21, 8080]

    def generate_packet_metadata(self):
        # Select a random protocol from the available protocols
        protocol = random.choice(self.protocols)
        # Generate random source and destination IP addresses within specified ranges
        src_ip = f"192.168.{random.randint(0,255)}.{random.randint(0,255)}"
        dest_ip = f"10.0.{random.randint(0,255)}.{random.randint(0,255)}"
        # Select random source port and destination port from predefined range
        src_port = random.randint(1024, 65535)
        dest_port = random.choice(self.ports)
        # Assume packet size is 0 for simplicity in this example
        packet_size = 0
        # Randomly generate latency in the range of 0.1 to 50.0 ms
        latency = round(random.uniform(0.1, 50.0), 3)

        # Return a dictionary with the generated metadata
        return {
            "protocol": protocol,
            "src_ip": src_ip,
            "dest_ip": dest_ip,
            "src_port": src_port,
            "dest_port": dest_port,
            "packet_size": packet_size,
            "latency": latency
        }

# Class to handle anomaly detection using Isolation Forest
class AnomalyDetector:
    def __init__(self, threshold, memory_window=100):
        # Set threshold for anomaly detection
        self.threshold = threshold
        # Initialize the Isolation Forest model, a machine learning algorithm
        self.model = IsolationForest(n_estimators=200, contamination=0.05, random_state=42, verbose=1)
        # Initialize a deque to store packet history, keeping a memory window of fixed size
        self.packet_history = deque(maxlen=memory_window)
        # Variance threshold for packet data to trigger model retraining
        self.packet_variance_threshold = 1000
        # Interval at which the model will be retrained
        self.retrain_interval = 50
        # Counter to track the number of packets processed
        self.detection_counter = 0

    def adaptive_training(self):
        # Train the model again if the data variance exceeds the predefined threshold
        if len(self.packet_history) >= self.packet_history.maxlen:
            data_variance = np.var(self.packet_history)
            if data_variance > self.packet_variance_threshold:
                # Train the model with the latest packet history data
                self.model.fit(np.array(self.packet_history).reshape(-1, 1))
                logging.info("Model retrained based on new packet variance.")

    def detect_anomaly(self, packet_count):
        # Append the new packet count to the history
        self.packet_history.append(packet_count)
        # Increment the detection counter to track the number of packets processed
        self.detection_counter += 1
        # If enough packets have been processed, retrain the model periodically
        if self.detection_counter % self.retrain_interval == 0:
            self.adaptive_training()

        # Generate a set of normal traffic data for training the model
        normal_data = np.random.randint(low=500, high=1500, size=(1000, 1))
        # Fit the model with normal traffic data to maintain model consistency
        self.model.fit(normal_data)
        # Calculate the anomaly score based on the packet count
        anomaly_score = self.model.decision_function([[packet_count]])[0]
        # If the anomaly score is below the threshold, categorize it as an anomaly
        if anomaly_score < self.threshold:
            return self.categorize_anomaly(packet_count)
        return None

    def categorize_anomaly(self, packet_count):
        # Categorize the detected anomaly based on the packet count
        if packet_count < 500:
            return f"Anomaly: Low Traffic Spike. Count: {packet_count}"
        elif packet_count > 1500:
            return f"Anomaly: High Traffic Spike. Count: {packet_count}"
        return f"Anomaly: Unusual Traffic Pattern. Count: {packet_count}"

# Class for simulating packet traffic and generating random packet counts
class TrafficSimulator:
    def __init__(self):
        # Initialize the PacketMetadataGenerator for packet metadata generation
        self.metadata_generator = PacketMetadataGenerator()

    def simulate_packet(self):
        # Generate a random packet count within a specified range
        packet_count = random.randint(300, 2000)
        # Generate packet metadata
        metadata = self.metadata_generator.generate_packet_metadata()
        # If the packet size is 0, return the generated packet count
        if metadata["packet_size"] == 0:
            return packet_count
        return None

# Class for inspecting and processing network traffic in real-time
class RealTimePacketInspector:
    def __init__(self):
        # Initialize the TrafficSimulator to simulate packet traffic
        self.traffic_simulator = TrafficSimulator()
        # Initialize the AnomalyDetector for detecting traffic anomalies
        self.analyzer = AnomalyDetector(threshold=-0.3)
        # Initialize a list to store the processed packet data
        self.packet_data = []

    def run_inspection(self):

        while True:
            packet_count = self.traffic_simulator.simulate_packet()
            # If a valid packet count is generated, process it for anomaly detection
            if packet_count is not None:
                anomaly_result = self.analyzer.detect_anomaly(packet_count)
                # If an anomaly is detected, log the result
                if anomaly_result:
                    print(f"Detection Result: {anomaly_result}")
                # Capture the timestamp and the anomaly result (or "Normal" if no anomaly detected)
                timestamp = time.time()
                self.packet_data.append((timestamp, packet_count, anomaly_result or "Normal"))
                # Introduce a small delay to mimic real-time packet processing
                time.sleep(random.uniform(0.3, 1.5))

    def get_packet_data(self):
        # Return the last 50 packets of data for display
        return self.packet_data[-50:]

# Flask routes to serve the application
@app.route('/')
def index():
    # Render the index page (for displaying the packet data on a web interface)
    return render_template('index.html')

@app.route('/packet_data')
def packet_data():
    # Return the most recent packet data in JSON format
    return jsonify(inspector.get_packet_data())

# Main function to initialize and run the web server with real-time packet inspection
if __name__ == "__main__":
    # Initialize the RealTimePacketInspector to start processing packet data
    inspector = RealTimePacketInspector()

    # Use threading to run the packet inspection in parallel with the Flask web server
    import threading
    inspector_thread = threading.Thread(target=inspector.run_inspection)
    inspector_thread.daemon = True
    inspector_thread.start()

    # Start the Flask web application
    app.run(debug=True, host="0.0.0.0", port=5000)

import numpy as np
from sklearn.ensemble import IsolationForest
import time
import random
import logging
from collections import deque

class PacketMetadataGenerator:
    def __init__(self):
        self.protocols = ["TCP", "UDP", "HTTP", "HTTPS", "FTP", "SSH", "DNS"]
        self.ports = [80, 443, 53, 22, 21, 8080]

    
    def generate_packet_metadata(self):
        protocol = random.choice(self.protocols)
        src_ip = f"192.168.{random.randint(0,255)}.{random.randint(0,255)}"
        dest_ip = f"10.0.{random.randint(0,255)}.{random.randint(0,255)}"
        src_port = random.randint(1024, 65535)
        dest_port = random.choice(self.ports)
        
        packet_size = 0
        latency = round(random.uniform(0.1, 50.0), 3)

        return {
            "protocol": protocol,
            "src_ip": src_ip,
            "dest_ip": dest_ip,
            "src_port": src_port,
            "dest_port": dest_port,
            "packet_size": packet_size,
            "latency": latency
        }

class AnomalyDetector:
    def __init__(self, threshold, memory_window=100):
        self.threshold = threshold
        self.model = IsolationForest(n_estimators=200, contamination=0.05, random_state=42, verbose=1)
        self.packet_history = deque(maxlen=memory_window)
        self.packet_variance_threshold = 1000
        self.retrain_interval = 50
        self.detection_counter = 0

    def adaptive_training(self):
        if len(self.packet_history) >= self.packet_history.maxlen:
            data_variance = np.var(self.packet_history)
            if data_variance > self.packet_variance_threshold:
                self.model.fit(np.array(self.packet_history).reshape(-1, 1))
                logging.info("Model retrained based on new packet variance.")

    def detect_anomaly(self, packet_count):
        self.packet_history.append(packet_count)
        self.detection_counter += 1
        if self.detection_counter % self.retrain_interval == 0:
            self.adaptive_training()

        normal_data = np.random.randint(low=500, high=1500, size=(1000, 1))
        self.model.fit(normal_data)
        anomaly_score = self.model.decision_function([[packet_count]])[0]
        if anomaly_score < self.threshold:
            return self.categorize_anomaly(packet_count)
        return None 

    def categorize_anomaly(self, packet_count):
        if packet_count < 500:
            return f"Anomaly: Low Traffic Spike. Count: {packet_count}"
        elif packet_count > 1500:
            return f"Anomaly: High Traffic Spike. Count: {packet_count}"
        return f"Anomaly: Unusual Traffic Pattern. Count: {packet_count}"

class TrafficSimulator:
    def __init__(self):
        self.metadata_generator = PacketMetadataGenerator()

    def simulate_packet(self):
        packet_count = random.randint(300, 2000)
        metadata = self.metadata_generator.generate_packet_metadata()

        if metadata["packet_size"] == 0:
            self.display_packet_details(metadata, packet_count)
            return packet_count
        return None  

    def display_packet_details(self, metadata, packet_count):
        print(f"Packet Details: [Protocol: {metadata['protocol']}] "
              f"[Source IP: {metadata['src_ip']}] "
              f"[Dest IP: {metadata['dest_ip']}] "
              f"[Src Port: {metadata['src_port']}] "
              f"[Dst Port: {metadata['dest_port']}]")
        print(f"Packet Count: {packet_count}, Packet Size: {metadata['packet_size']}B, Latency: {metadata['latency']}ms")

class PacketAnalyzer:
    def __init__(self, threshold=-0.3):
        self.detector = AnomalyDetector(threshold)

    def analyze_packet(self, packet_count):
        if packet_count is not None:
            result = self.detector.detect_anomaly(packet_count)
            if result:
                print(f"Detection Result: {result}\n")

class EnhancedReporting:
    def __init__(self):
        self.reported_anomalies = []

    def report_anomaly(self, anomaly):
        self.reported_anomalies.append(anomaly)
        print(f"Reporting Anomaly: {anomaly}")

    def summarize_anomalies(self):
        print(f"Total Anomalies Detected: {len(self.reported_anomalies)}")
        for anomaly in self.reported_anomalies:
            print(anomaly)

class RealTimePacketInspector:
    def __init__(self):
        self.traffic_simulator = TrafficSimulator()
        self.analyzer = PacketAnalyzer()
        self.reporting = EnhancedReporting()

    def run_inspection(self):
        while True:
            packet_count = self.traffic_simulator.simulate_packet()
            if packet_count is not None:
                anomaly_result = self.analyzer.analyze_packet(packet_count)
                if anomaly_result:
                    self.reporting.report_anomaly(anomaly_result)
            time.sleep(random.uniform(0.3, 1.5))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    inspector = RealTimePacketInspector()
    inspector.run_inspection()

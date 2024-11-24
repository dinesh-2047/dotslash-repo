import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

class DataVisualizer:
    def __init__(self):
        # Initialize an empty list to store packet data
        self.packet_data = [] 

    def capture_data(self, packet_count, anomaly_score, mitigated_requests):
        # Capture and append packet data with timestamp
        timestamp = len(self.packet_data) + 1  # Simple incremented timestamp based on the current length of data
        self.packet_data.append((timestamp, packet_count, anomaly_score, mitigated_requests))

    def simulate_data(self, anomaly_detector, mitigation_engine):
        # Simulate traffic data for 50 iterations to generate packet count, anomaly score, and mitigation details
        for _ in range(50): 
            packet_count = random.randint(300, 2000)  # Random packet count between 300 and 2000
            anomaly_score = anomaly_detector.detect_anomaly(packet_count)  # Detect anomaly based on packet count
            mitigated_requests = mitigation_engine.mitigated_requests  # Get number of mitigated requests from mitigation engine

            # Print if an anomaly is detected
            if anomaly_score:
                print(f"Anomaly Detected: {anomaly_score}")
            
            # Simulate attack mitigation
            mitigation_engine.mitigate_attack()

            # Capture the data (timestamp, packet count, anomaly score, mitigated requests)
            self.capture_data(packet_count, anomaly_score if anomaly_score else 0, mitigated_requests)

    def visualize_data_3d(self):
        # Prepare data for 3D visualization
        times = np.array([data[0] for data in self.packet_data])  # Extract timestamps
        packet_counts = np.array([data[1] for data in self.packet_data])  # Extract packet counts
        anomaly_scores = np.array([data[2] for data in self.packet_data])  # Extract anomaly scores
        mitigated_requests = np.array([data[3] for data in self.packet_data])  # Extract mitigated requests

        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the data points in 3D space (time vs packet count vs anomaly score)
        ax.plot(times, packet_counts, anomaly_scores, label="Packet Traffic", color='blue')
        
        # Add a scatter plot with colors representing mitigated requests
        sc = ax.scatter(times, packet_counts, anomaly_scores, c=mitigated_requests, cmap='coolwarm')

        # Add color bar for better understanding of mitigated request scale
        cbar = plt.colorbar(sc)
        cbar.set_label('Mitigated Requests')

        # Set axis labels and the title of the plot
        ax.set_xlabel('Time')
        ax.set_ylabel('Packet Count')
        ax.set_zlabel('Anomaly Score')
        ax.set_title('3D Visualization of Traffic Anomalies and Mitigations')

        # Show the plot
        plt.show()

if __name__ == "__main__":
    # Import necessary modules (AnomalyDetector, MitigationEngine) for detection and mitigation
    from anomaly_detector import AnomalyDetector
    from mitigation_engine import MitigationEngine

    # Create instances of AnomalyDetector and MitigationEngine with default parameters
    detector = AnomalyDetector(threshold=-0.3)
    mitigation_engine = MitigationEngine(ip="175.176.187.102", port=80)

    # Create instance of DataVisualizer to handle data simulation and visualization
    visualizer = DataVisualizer()

    # Simulate data for 50 iterations, generating traffic data and mitigating attacks
    visualizer.simulate_data(detector, mitigation_engine)

    # Visualize the captured data in 3D
    visualizer.visualize_data_3d()

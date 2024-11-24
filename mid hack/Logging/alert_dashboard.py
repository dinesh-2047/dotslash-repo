from flask import Flask, jsonify, render_template
from visualize import DataVisualizer
from anomaly_detector import AnomalyDetector
from mitigation_engine import MitigationEngine

# Initialize the Flask web application
app = Flask(__name__)

# Create an instance of the AnomalyDetector with a specified threshold for detecting anomalies
detector = AnomalyDetector(threshold=-0.3)
# Create an instance of the MitigationEngine with the server's IP address and port to handle responses or mitigation actions
mitigation_engine = MitigationEngine(ip="175.176.187.102", port=80)

# Create an instance of the DataVisualizer for handling packet data visualization
visualizer = DataVisualizer()

# Define the route for the home page, which will render the dashboard HTML
@app.route('/')
def index():
    # Render and return the dashboard page for displaying network data and analysis results
    return render_template('dashboard.html')

# Define the route for retrieving graph data to display in the front-end
@app.route('/graph_data')
def graph_data():
    # Extract the packet data stored in the visualizer
    packet_data = visualizer.packet_data  
    # Extract individual components for graphing (timestamps, packet counts, anomaly scores, and mitigated requests)
    times = [data[0] for data in packet_data]
    packet_counts = [data[1] for data in packet_data]
    anomaly_scores = [data[2] for data in packet_data]
    mitigated_requests = [data[3] for data in packet_data]

    # Organize the extracted data into a structure suitable for graphing on the front-end
    graph_data = {
        'times': times,
        'packet_counts': packet_counts,
        'anomaly_scores': anomaly_scores,
        'mitigated_requests': mitigated_requests
    }
    
    # Return the data in JSON format so the front-end can render the graphs
    return jsonify(graph_data)

# Main entry point to run the application
if __name__ == "__main__":
    # Start the data simulation process, using the anomaly detector and mitigation engine
    visualizer.simulate_data(detector, mitigation_engine) 
    # Run the Flask application in debug mode for easier development and testing
    app.run(debug=True)  

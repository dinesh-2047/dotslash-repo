from flask import Flask, render_template, jsonify
from anomaly_detector import AnomalyDetector
from mitigation_engine import MitigationEngine
from visualize import DataVisualizer
import config

# Initialize the Flask application
app = Flask(__name__)

# Initialize the anomaly detection system with a defined threshold for anomaly detection
detector = AnomalyDetector(config.THRESHOLD)
# Initialize the mitigation engine with the server's IP address and port for potential responses
engine = MitigationEngine(config.SERVER_IP, config.SERVER_PORT)
# Initialize the data visualization component for presenting network data
visualizer = DataVisualizer()

# Define the route for the home page of the application
@app.route('/')
def index():
    # Render and return the HTML template for the index page
    return render_template('index.html')

# Define the route to retrieve network packet data for analysis
@app.route('/get_data')
def get_data():
    # Call the method to simulate the collection of packet data
    visualizer.simulate_packet_data()
    # Fetch the latest collected packet data
    packet_data = visualizer.packet_data
    # Return the packet data as a JSON response to the client
    return jsonify(packet_data)

# Main entry point for running the Flask web application
if __name__ == "__main__":
    # Run the Flask app on all available network interfaces, listening on port 5000
    app.run(debug=True, host="0.0.0.0", port=5000)

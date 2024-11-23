from flask import Flask, render_template, jsonify
from anomaly_detector import AnomalyDetector
from mitigation_engine import MitigationEngine
from visualize import DataVisualizer
import config

app = Flask(__name__)

detector = AnomalyDetector(config.THRESHOLD)
engine = MitigationEngine(config.SERVER_IP, config.SERVER_PORT)
visualizer = DataVisualizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    visualizer.simulate_packet_data()
    packet_data = visualizer.packet_data
    return jsonify(packet_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
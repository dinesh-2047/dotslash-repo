from flask import Flask, jsonify, render_template
from visualize import DataVisualizer
from anomaly_detector import AnomalyDetector
from mitigation_engine import MitigationEngine

app = Flask(__name__)

detector = AnomalyDetector(threshold=-0.3)
mitigation_engine = MitigationEngine(ip="175.176.187.102", port=80)

visualizer = DataVisualizer()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/graph_data')
def graph_data():
    packet_data = visualizer.packet_data  
    times = [data[0] for data in packet_data]
    packet_counts = [data[1] for data in packet_data]
    anomaly_scores = [data[2] for data in packet_data]
    mitigated_requests = [data[3] for data in packet_data]

    graph_data = {
        'times': times,
        'packet_counts': packet_counts,
        'anomaly_scores': anomaly_scores,
        'mitigated_requests': mitigated_requests
    }
    
    return jsonify(graph_data)

if __name__ == "__main__":
    visualizer.simulate_data(detector, mitigation_engine) 
    app.run(debug=True)

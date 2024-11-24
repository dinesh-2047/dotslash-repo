# **MOMMYNET**

This project is a **Network Anomaly Detection and Mitigation System** designed to detect anomalies in network traffic, such as DDoS attacks or unusual traffic patterns. It includes a traffic simulator that generates data, an anomaly detector that uses machine learning to identify outliers, and a real-time reporting system. The system also features an **IP-based Attack Mitigation Engine**, which simulates attacks and applies mitigation techniques when the traffic is identified as suspicious.

---

## **Features**
- Simulates incoming network traffic to a target server and monitors packet flow.
- Detects anomalies in the traffic using an **Anomaly Detector**.
- Utilizes threading for efficient traffic handling and attack simulation.
- **Mitigation Engine**: Drops or mitigates incoming connections based on the attack rate.
- **Real-Time Logging**: Tracks and logs detected anomalies, mitigation actions, and traffic statistics.
- **Attack Mitigation**: Automatically applies rate limiting to prevent server overload during potential DDoS attacks.
- **Summary Reporting**: Generates summaries of attack and mitigation statistics after each cycle.
- **Email Notifications**: Automatically sends email alerts when anomalies exceed a defined threshold (if configured).
- **Real-Time Dashboard**: Offers an optional real-time display of attack counts and mitigated requests.

---

## **Requirements**
- Python 3.x
- `scikit-learn` for anomaly detection (if used)
- Basic understanding of network traffic and anomaly detection techniques
- `SendGrid` for email notifications (if email alert feature is configured)

---

## **Usage**
### **1. Clone the Repository**
```bash
git clone https://github.com/dinesh-2047/dotslash-repo.git
cd dotslash-repo
```

### **2. Install Dependencies**
This script requires the following Python libraries:
```bash
pip install scikit-learn numpy
```

### **3. Configure Email** (Optional)
If you wish to enable email notifications, replace the placeholders in the script with your own SendGrid credentials:
- Replace `SENDGRID_API_KEY`, `SENDER_EMAIL`, and `RECEIVER_EMAIL` in the script.

### **4. Run the Script**
Execute the main script to start the anomaly detection and mitigation system:
```bash
python main.py
```

### **5. Provide Input**
If running with the real-time packet simulation:
- **Packet Count**: Define the number of packets to simulate in each cycle.
- **Threshold**: Set the anomaly detection threshold.

---

## **Script Breakdown**

### **1. `MitigationEngine` Class**
This class handles the mitigation of potential attacks:
- **Purpose**: Simulate incoming traffic and apply mitigation techniques like rate limiting when an attack is detected.
- **Key Methods**:
  - `mitigate_attack()`: Analyzes incoming traffic and drops requests if attack thresholds are exceeded (e.g., more than 1000 requests in under 10 seconds).
  - `print_summary()`: Prints a summary of the current attack and mitigation stats, including requests mitigated and time since last mitigation.

### **2. `AnomalyDetector` Class**
This class uses **Isolation Forest** for anomaly detection:
- **Threshold**: A score threshold for anomaly detection (negative values indicate outliers).
- **Key Methods**:
  - `detect_anomaly(value)`: Detects anomalies based on the packet count.
  - `adaptive_training()`: Retrains the model based on new packet data to improve accuracy over time.

### **3. `DataVisualizer` Class**
This class visualizes the network data in real-time:
- **Purpose**: Visualizes traffic, anomaly scores, and mitigated requests using 3D plotting.
- **Key Methods**:
  - `capture_data()`: Captures and stores packet data, including packet count, anomaly score, and mitigated requests.
  - `simulate_data()`: Simulates traffic and anomalies, using the `AnomalyDetector` and `MitigationEngine` for detection and mitigation.
  - `visualize_data_3d()`: Visualizes the packet data in a 3D graph.

### **4. Real-Time Packet Inspector**
- The system simulates network traffic, analyzes it for anomalies, and triggers mitigation and alerts when required.

---

## **Logging**
The system logs key events, including anomaly detection and email notifications, to a log file (`anomaly_detection.log`).

- **log_anomaly_detection()**: Logs anomaly detection events.
- **log_email_sent()**: Logs email notifications sent to the receiver.
- **log_packet_info()**: Logs packet details as they are analyzed.

---

## **Important Notes**
1. **Educational Use Only**: This script is strictly for educational purposes to demonstrate network anomaly detection.
2. **Permissions**: Always obtain explicit permission before running this tool on any live network or server.
3. **Usage Responsibility**: The author is not responsible for misuse or illegal activities associated with this tool.

---

## **Future Enhancements**
- Add support for more advanced anomaly detection algorithms.
- Integrate additional visualization tools for traffic analysis.
- Provide better GUI features to control and monitor the system.
- Implement logging for anomalies and alerts in a centralized database.

---

## **Contributors**

- **Devashish** (Team Leader)(Primary Developer)
- **Dinesh Bhardwaj** (Contributor)
- **Sourabh Choudhary** (Contributor)

---

This README explains the key functionalities of the anomaly detection and mitigation system, covering traffic simulation, anomaly detection, attack mitigation, email alerts, and logging. It provides users with clear instructions for installation, configuration, and usage.
```

### Key Updates:

1. **Features**: Added details about the **Mitigation Engine** and the ability to visualize data in real-time with 3D plots.
2. **Script Breakdown**: Updated with the `MitigationEngine`, `AnomalyDetector`, and `DataVisualizer` classes.
3. **Logging and Email Reporting**: Added emphasis on real-time logging and email notifications for anomaly detection and mitigation.
4. **Real-Time Packet Inspector**: Explained the role of the packet inspector in simulating and analyzing network traffic.

This version reflects the updated functionality based on the recent code provided.
# **MOMMYNET**

This project is a **Network Anomaly Detection and Mitigation System** designed to detect anomalies in network traffic, such as DDoS attacks or unusual traffic patterns. It includes a traffic simulator that generates data, an anomaly detector that uses machine learning to identify outliers, and a real-time reporting system. The system also features an email alert mechanism that triggers when certain anomaly thresholds are reached.

---

## **Features**
- Creates multiple simultaneous TCP connections to a target server.
- Continuously sends data to the target, simulating a DoS attack.
- Utilizes threading for efficient traffic handling.
- Traffic analyzer to monitor network traffic in real-time.
- GUI dashboard for controlling the attack and viewing network data.
- Displays anomaly and mitigated data.
- **Anomaly Detection**: Uses an Isolation Forest model to detect traffic anomalies.
- **Email Notifications**: Automatically sends email alerts when anomalies exceed a defined threshold.
- **Real-Time Logging**: Tracks and logs detected anomalies, sent emails, and packet data.
- **Adaptive Learning**: The anomaly detection model is retrained periodically to improve its accuracy.

---

## **Requirements**
- Python 3.x
- Tkinter library for GUI (if applicable)
- `scikit-learn` for anomaly detection
- `SendGrid` for email notifications
- Basic understanding of network traffic and anomaly detection techniques

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

### **3. Configure Email**
- Replace `SENDGRID_API_KEY`, `SENDER_EMAIL`, and `RECEIVER_EMAIL` in the script with your own SendGrid credentials.

### **4. Run the Script**
Execute the main script to start real-time packet analysis and anomaly detection:
```bash
python main.py
```

### **5. Provide Input (GUI)**  
If running with a GUI (Tkinter):
- **Packet Count**: Number of packets to simulate.
- **Threshold**: Set the anomaly detection threshold.

---

## **Script Breakdown**

### **1. `AnomalyDetector` Class**
This class uses **Isolation Forest** for anomaly detection:
- **Threshold**: A score threshold for anomaly detection (negative values indicate outliers).
- **Adaptive Training**: The model is retrained when the packet variance exceeds a certain threshold.

- **Key Methods**:
  - `detect_anomaly(value)`: Detects anomalies based on packet count.
  - `categorize_anomaly(packet_count)`: Categorizes the type of anomaly (e.g., low or high traffic spikes).
  - `adaptive_training()`: Retrains the model based on new packet history.

### **2. `TrafficSimulator` Class**
This class simulates traffic by generating random packets and passing them to the anomaly detector.

- **simulate_packet()**: Simulates a packet and returns the packet count for anomaly detection.

### **3. `PacketAnalyzer` Class**
The packet analyzer handles the detection of anomalies based on the simulated traffic and uses the **AnomalyDetector** to categorize potential issues.

### **4. `EnhancedReporting` Class**
This class handles email reporting:
- **report_anomaly()**: Sends anomaly details via email when triggered.
- **summarize_anomalies()**: Prints a summary of all detected anomalies.


### **5. Logging**
The system logs key events, including anomaly detection and email notifications, to a log file (`anomaly_detection.log`).

- **log_anomaly_detection()**: Logs anomaly detection events.
- **log_email_sent()**: Logs email notifications sent to the receiver.
- **log_packet_info()**: Logs packet details as they are analyzed.

### **7. Real-Time Packet Inspector**
The real-time packet inspector simulates network traffic, analyzes it for anomalies, and triggers alerts via email when required.

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

This README explains the key functionalities of the anomaly detection system, covering traffic simulation, anomaly detection, email alerts, and logging. It provides users with clear instructions for installation and usage, along with a breakdown of the code components.
```

### Key Updates:

1. **Features**: Added the real-time anomaly detection, email notifications, and adaptive learning aspects.
2. **Script Breakdown**: Updated with details about the `AnomalyDetector`, `TrafficSimulator`, `PacketAnalyzer`, and `EnhancedReporting` classes.
3. **Logging and Email Reporting**: Emphasized logging of anomaly detection events and email notifications.

The overall content remains the same while reflecting the updated functionality based on your provided code.
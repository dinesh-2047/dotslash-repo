
# **MOMMYNET**

This project is a **DDOS ATTACK PREVENTION MECHANISM** tool designed to simulate DoS attacks for educational purposes. It includes a traffic analyzer that listens for incoming traffic and a Tkinter-based dashboard that controls the attack and displays relevant data. The goal is to understand how traffic flows in a network and explore mitigation techniques for potential threats.

---

## **Features**
- Creates multiple simultaneous TCP connections to a target server.
- Continuously sends data to the target, simulating a DoS attack.
- Utilizes threading for efficient traffic handling.
- Traffic analyzer to monitor network traffic in real-time.
- GUI dashboard for controlling the attack and viewing network data.
- Displays anomaly and mitigated data.

---

## **Requirements**
- Python 3.x
- Tkinter library for GUI
- Basic understanding of networking and socket programming

---

## **Usage**
### **1. Clone the Repository**
```bash
git clone https://github.com/dinesh-2047/dotslash-repo.git
cd dotslash-repo
```

### **2. Install Dependencies**
This script uses Python's standard libraries (Tkinter, socket, threading, etc.), so no additional dependencies are required.

### **3. Run the Script**
Execute the script using:
```bash
python main.py
```

### **4. Provide Input**
When prompted in the GUI:
- **Target IP Address**: The server's IP address you want to test.
- **Target Port**: The port number on which the server is listening.

---

## **Script Breakdown**

### **1. `TrafficAnalyzer` Class**
This class listens for UDP traffic on a specified port and tracks the following metrics:
- **Total Packets**: The total number of received packets.
- **Average Packet Size**: The average size of the packets.
- **Connection Rate**: Simulated number of new connections per second.
- **Bandwidth**: Simulated bandwidth usage in bytes per second.

### **2. `make_socket(host, port)`**
This function:
- Creates a TCP socket using the target's host and port.
- Attempts to connect to the server.
- Handles connection errors by retrying or closing the socket.

### **3. `attack(host, port, id)`**
This function:
- Manages multiple sockets using a list.
- Sends a null byte (`b"\0"`) to the target continuously.
- Handles socket errors and reinitializes failed connections.
- Logs each successful data transmission.

### **4. `start_attack()`, `stop_attack()`**
These functions:
- Start and stop the attack on the target server.
- Provide feedback to the user using message boxes.

### **5. GUI (Tkinter) Dashboard**
The GUI is built using the Tkinter library and allows users to:
- Start and stop the attack.
- Cycle identities for anonymity.
- View real-time anomaly and mitigated data.
- Display network traffic statistics.

---

## **Important Notes**
1. **Educational Use Only**: This script is strictly for testing and educational purposes. Unauthorized use is illegal and unethical.
2. **Target Systems**: Always obtain explicit permission before running this tool on any network or server.
3. **Responsibility**: The author is not responsible for any misuse of this script.

---

## **Future Enhancements**
- Add support for different payload types.
- Include logging to track connection statistics.
- Integrate proxy support for anonymized testing.

---

## **Contributors**
- Devashish (Leader - Cyber Sentinels) (Primary Developer)
- Dinesh Bhardwaj (Contributor)
- Sourabh Choudhary (Contributor)

---

This README now includes details about the traffic analyzer class and the corresponding GUI/dashboard that you integrated. It explains the key functionalities, user input requirements, and the overall flow of the tool.

# Network Stress Testing Script

This project is a **network stress testing tool** designed for educational and ethical purposes only. The script demonstrates how to create multiple TCP connections and send data to a target server. The goal is to understand the concepts of sockets, threading, and traffic simulation.

---

## **Features**
- Creates multiple simultaneous TCP connections to a target.
- Sends continuous data to the target server.
- Utilizes threading for high-performance simulations.
- Includes error handling for connection failures.

---

## **Requirements**
- Python 3.x
- A basic understanding of networking and socket programming.

---

## **Usage**
### **1. Clone the Repository**
```bash
git clone <repository_url>
cd <repository_directory>
```

### **2. Install Dependencies**
This script uses only Python’s standard library, so no additional dependencies are required.

### **3. Run the Script**
Execute the script using:
```bash
python script_name.py
```

### **4. Provide Input**
When prompted, enter:
- **Target IP Address**: The server's IP you want to test.
- **Target Port**: The port number on which the server is listening.

---

## **Script Breakdown**

### **1. `make_socket(host, port)`**
This function:
- Creates a TCP socket using the target's host and port.
- Attempts to connect to the server.
- Handles connection errors by retrying or closing the socket.

### **2. `attack(host, port, id)`**
This function:
- Manages multiple sockets using a list.
- Sends a null byte (`b"\0"`) to the target continuously.
- Handles socket errors and reinitializes failed connections.
- Logs each successful data transmission.

---

## **Important Notes**
1. **Educational Use Only**: This script is strictly for testing and educational purposes. Using it on unauthorized systems is illegal and unethical.
2. **Target Systems**: Always obtain explicit permission before running this tool on any network or server.
3. **Responsibility**: The author is not responsible for any misuse of this script.

---

## **Future Enhancements**
- Add support for different payload types.
- Include logging to track connection statistics.
- Integrate proxy support for anonymized testing.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## **Contributors**
- **Your Name** (Primary Developer)  
Feel free to contribute by submitting pull requests or raising issues.

--- 

This README follows a standard format, including all necessary details up to the `attack` function. You can expand it further as you develop additional functionality!
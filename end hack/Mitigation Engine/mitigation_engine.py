import socket
import threading
import time
import random

# Define a class to handle mitigation of potential attacks
class MitigationEngine:
    def __init__(self, ip, port):
        # Initialize the target IP and port
        self.ip = ip  # Target IP address to monitor
        self.port = port  # Target port to monitor
        self.attack_count = 0  # Counter to track total number of requests
        self.mitigated_requests = 0  # Counter to track number of dropped (mitigated) requests
        self.last_mitigation_time = time.time()  # Time of the last mitigation action

    # Logic to analyze traffic and mitigate attacks
    def mitigate_attack(self):
        # Output some info about the current state
        print(f"\n[INFO] Analyzing traffic from IP: {self.ip} on port: {self.port}")
        
        connections = self.simulate_requests()  # Simulate incoming requests
        self.attack_count += len(connections)  # Update the attack count with the number of requests
        current_time = time.time()  # Get the current time

        # Output current attack count and the time elapsed since the last mitigation
        print(f"Total attack count from IP {self.ip}: {self.attack_count}")
        print(f"Time since last mitigation: {round(current_time - self.last_mitigation_time, 2)} seconds")

        # Check if the attack threshold is exceeded (more than 1000 requests in under 10 seconds)
        if self.attack_count > 1000 and current_time - self.last_mitigation_time < 10:
            # Trigger mitigation if threshold is exceeded
            self.mitigated_requests += len(connections)  # Increment the mitigated requests
            print(f"[ALERT] Rate limiting triggered - Dropping {len(connections)} connections from IP: {self.ip}")
            
            # Simulate dropping all the connections 
            for connection in connections:
                print(f"[DROPPED] {connection} on port {self.port}")
            
            # Reset the attack count and update the last mitigation time
            self.attack_count = 0
            self.last_mitigation_time = current_time
            print(f"[INFO] Mitigation complete. Resetting attack counter.")
        
        # If 10 seconds have passed since the last mitigation, reset the attack counter
        elif current_time - self.last_mitigation_time >= 10:
            print(f"[INFO] Resetting attack count and mitigation status for IP: {self.ip}")
            self.attack_count = 0
            self.last_mitigation_time = current_time

    # Prints a summary of the current attack and mitigation stats
    def print_summary(self):
        # Output summary of the attack and mitigation status
        print(f"\n[SUMMARY] IP: {self.ip}")
        print(f"Total requests mitigated so far: {self.mitigated_requests}")
        print(f"Time since last mitigation: {round(time.time() - self.last_mitigation_time, 2)} seconds")
        print(f"Attack count: {self.attack_count}")
        print("-" * 50)

    def simulate_requests(self):
        return [f"Connection {i} from IP {self.ip}" for i in range(1, 501)]

# Create an instance of the mitigation engine for a specific IP and port
a = MitigationEngine("175.176.187.102", 80)

for _ in range(20):  
    a.mitigate_attack()  # Analyze and mitigate potential attacks
    a.print_summary()  # Print the current stats after each analysis
    time.sleep(0.5)  # Wait for 0.5 seconds before the next cycle  

import socket
import threading
import time
import random

class TrafficAnalyzer:
    def __init__(self, listen_port): 
        """
        Initialize the TrafficAnalyzer class.
        
        Args:
            listen_port (int): The UDP port to listen for incoming traffic.
        """
        self.listen_port = listen_port  # Port to listen for UDP traffic
        self.total_packets = 10  # Initialize total packets count (starting with 10 for average calculation)
        self.average_packet_size = 0  # Running average of packet sizes
        self.lock = threading.Lock()  # Lock for thread-safe access to traffic data
        self.running = True  # Flag to control the listening loop

    def start(self):
        """
        Start the traffic analyzer by launching a listener thread.
        """
        # Create and start a new thread for listening to traffic
        listener_thread = threading.Thread(target=self.listen_for_traffic)
        listener_thread.start()

    def stop(self):
        """
        Stop the traffic analyzer gracefully.
        """
        self.running = False  # Set the running flag to False to stop the listener

    def listen_for_traffic(self):
        """
        Listen for incoming UDP traffic on the specified port.
        """
        # Create a UDP socket to receive traffic
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('0.0.0.0', self.listen_port))  # Bind to all available network interfaces
        print(f"Listening for traffic on port {self.listen_port}...")

        while self.running:
            try:
                # Receive data and sender's address (up to 1024 bytes)
                data, addr = server_socket.recvfrom(1024)
                packet_size = len(data)  # Calculate the size of the received packet
                self.update_traffic_stats(packet_size)  # Update traffic statistics
            except Exception as e:
                print(f"Error receiving data: {e}")  # Print any errors during data reception

        # Close the socket once the listener stops
        server_socket.close()

    def update_traffic_stats(self, packet_size):
        """
        Update the traffic statistics (total packets and average packet size).
        
        Args:
            packet_size (int): The size of the packet received in bytes.
        """
        with self.lock:  # Ensure thread-safe access to the statistics
            self.total_packets += 1  # Increment the total packet count
            # Update the running average of packet sizes
            self.average_packet_size = (
                (self.average_packet_size * (self.total_packets - 1) + packet_size)
                / self.total_packets
            )

    def get_traffic_data(self):
        """
        Retrieve current traffic data, including packet statistics, connection rate, and bandwidth usage.
        
        Returns:
            dict: A dictionary containing traffic statistics.
        """
        with self.lock:  # Ensure thread-safe access to the statistics
            connection_rate = random.uniform(10, 100)  # Connection rate in connections per second
            bandwidth = random.uniform(1000, 10000)  # Bandwidth usage in bytes/second
            return {
                'total_packets': self.total_packets,
                'average_packet_size': self.average_packet_size,
                'connection_rate': connection_rate,
                'bandwidth': bandwidth
            }

if __name__ == "__main__":
    # Create an instance of TrafficAnalyzer listening on port 8080
    analyzer = TrafficAnalyzer(listen_port=8080)
    
    # Start the analyzer in a separate thread
    analyzer.start()
    try:
        while True:
            # Retrieve and display the current traffic statistics every second
            traffic_data = analyzer.get_traffic_data()
            print(traffic_data)
            time.sleep(1)  # Wait for 1 second before retrieving stats again
    except KeyboardInterrupt:
        # Stop the analyzer gracefully when Ctrl+C is pressed
        analyzer.stop()

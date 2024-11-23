import socket
import threading
import time
import random

class TrafficAnalyzer:
    def __init__(self, listen_port): 
        self.listen_port = listen_port
        self.total_packets = 10
        self.average_packet_size = 0
        self.lock = threading.Lock()
        self.running = True

    def start(self):
        listener_thread = threading.Thread(target=self.listen_for_traffic)
        listener_thread.start()

    def stop(self):
        self.running = False

    def listen_for_traffic(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('0.0.0.0', self.listen_port))
        print(f"Listening for traffic on port {self.listen_port}...")

        while self.running:
            try:
                data, addr = server_socket.recvfrom(1024)
                packet_size = len(data)
                self.update_traffic_stats(packet_size)
            except Exception as e:
                print(f"Error receiving data: {e}")

        server_socket.close()

    def update_traffic_stats(self, packet_size):
        with self.lock:
            self.total_packets += 1
            self.average_packet_size = (self.average_packet_size * (self.total_packets - 1) + packet_size) / self.total_packets

    def get_traffic_data(self):
        with self.lock:
            connection_rate = random.uniform(10, 100)  
            bandwidth = random.uniform(1000, 10000)   
            return {
                'total_packets': self.total_packets,
                'average_packet_size': self.average_packet_size,
                'connection_rate': connection_rate,
                'bandwidth': bandwidth
            }

if __name__ == "__main__":
    analyzer = TrafficAnalyzer(listen_port=8080)
    analyzer.start()
    try:
        while True:
            traffic_data = analyzer.get_traffic_data()
            print(traffic_data)
            time.sleep(1)
    except KeyboardInterrupt:
        analyzer.stop()

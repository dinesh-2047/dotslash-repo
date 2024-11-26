import numpy as np
from sklearn.ensemble import IsolationForest
import time
import random
import logging
from collections import deque

# Class to handle packet metadata such as protocol, source and destination IPs, and ports
class PacketMetadataGenerator:
    def __init__(self):
        # Define available network protocols and common ports
        self.protocols = ["TCP", "UDP", "HTTP", "HTTPS", "FTP", "SSH", "DNS"]
        self.ports = [80, 443, 53, 22, 21, 8080]

   
   invalid datetime A combination of a date and a time. Attributes: ()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    # Initialize and start the real-time packet inspector
    inspector = RealTimePacketInspector()
    inspector.run_inspection()

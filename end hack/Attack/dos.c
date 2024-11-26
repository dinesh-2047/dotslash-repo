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

   
    getc(stdin); // Wait for user input to keep the program running
    return 0; // Exit the program
}

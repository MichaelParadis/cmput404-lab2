#!/usr/bin/env python3
import socket

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)    
    print(addr_info)

if __name__ == "__main__":
    main()

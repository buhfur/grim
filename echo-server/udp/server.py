#!/usr/bin/env python3 
import socket
import sys
import argparse 
# Simple udp echo server 
host = 'localhost'

data_payload = 2048

backlog = 5  # No. of maximum allowed connections to server 

def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Enable reuse of address / port 
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

    # Bind socket to port 
    sock.bind((host,port)) 
    # NOTE: only difference between TCP and UDP is no listen function being used. 

    print(f"Bound Server to\nHost: {host}\nPort: {port}\n")

    try:

        while True:
            print(f"Waiting to receive message from client\n")
            data , addr  = client.recvfrom(data_payload) # Receives data_payload bytes from client 
            print(f'Received {len(data)} from {address}\n')
            if data:
                sent_data = sock.sendto(data,addr)
                print(f"Sent {sent_data} bytes back to {addr}\n")

            # End connection to client 
    except KeyboardInterrupt:
        sock.close() # Close the socket if Ctrl+C is pressed 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Server example")
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)


    


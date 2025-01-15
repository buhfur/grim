import socket
import sys
import argparse 
# Simple tcp echo server 
host = 'localhost'

data_payload = 2048

backlog = 5  # No. of maximum allowed connections to server 

def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enable reuse of address / port 
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

    # Bind socket to port 
    sock.bind((host,port)) 
    sock.listen(backlog)  # Listen up to backlog connections 
    while True:
        print(f"Waiting to receive message from client")
        client, addr = sock.accept() # Accepts connection from client 
        data = client.recv(data_payload) # Receives data_payload bytes from client 
        if data:
            print(f"Data: {data}")
            client.send(data)
            print(f"Sent {data} bytes back to {addr}")

        # End connection to client 
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Server example")
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)


    


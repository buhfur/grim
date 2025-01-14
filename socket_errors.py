#!/usr/bin/env python3 
import socket 
import sys
import argparse
# Handling socket errors 

def main():
    parser = argparse.ArgumentParser(description='Socket error examples')
    parser.add_argument('-H','--host', type=str,action="store", dest="host")
    parser.add_argument('-p','--port', type=int,action="store", dest="port")
    parser.add_argument('-f','--file', type=argparse.FileType('r'),action="store", dest="file")
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # Attempt creating socket 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error Creating Socket: {e}\n")
        sys.exit(1)
    # Attempt to connect to host/port 
    try:
        s.connect((host,port))
    except socket.gaierror as e:
        print(f"Address related Error Connecting to {host}: {e}\n")
        sys.exit(1)

    except socket.error as e:
        print(f"Connection Error: {e}")

    # Attempt to send data
    try:
        msg = "GET {filename} HTTP/1.0\r\n\r\n" # basic HTTP GET request 
        s.sendall(msg.encode('utf-8'))

    except socket.error as e:
        print(f"Error sending data: {e}\n")
        sys.exit(1)
    while True:
        # Wait to receive data from remote host 
        try:
            buf = s.recv(2048)
        
        except socket.error as e:
            print(f"Error receiving data : {e}\n")
            sys.exit(1)
        if not len(buf): # Checks if buffer for received data has been filled 
            break
        sys.stdout.write(buf.decode('utf-8'))



    

if __name__ == '__main__':
    main()

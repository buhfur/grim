#!/usr/bin/env python3 
import socket 
import argparse 
import sys
# UDP echo client
host = 'localhost'
data_payload = 2048
def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host,port)
    print(f"Connecting to: {host} on port : {port}\n")
    message = "Test msg , this is a test."
    try: 
        message = "Test msg , this will be echoed"
        print(f"Sending: {message} to server.\n")
        sock.sendto(message.encode('utf-8'), server_address) # Send message encoded in utf-8 
        # Look for response 
        data, server = sock.recvfrom(data_payload) 
        print(f"Received : {data}\n")

    except socket.error as e:
        print(f"Socket error: {str(e)}\n")

    except Exception as e:
        print(f"Other exception encountered: {e}\n")
    finally:
        print(f"Closing connection to {host}")
        sock.close()





if __name__ == '__main__':
    args = argparse.ArgumentParser(description='Echo socket client')
    args.add_argument('--port',action='store',type=int,required=True)
    given_args = args.parse_args()
    port = given_args.port

    echo_client(port)

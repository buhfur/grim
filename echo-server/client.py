import socket 
import argparse 
import sys
#!/usr/bin/env python3 

host = 'localhost'

def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host,port)
    print(f"Connecting to: {host} on port : {port}\n")
    sock.connect(server_address) # Attempt connection to server
    # Send data
    try: 
        message = "Test msg , this is a test."
        print(f"Sending: {message} to server.\n")
        sock.sendall(message.encode('utf-8')) # Send message encoded in utf-8 
        # Look for response 
        amount_recv = 0
        amount_exp = len(message) # Length of message should be same lenght as the message should only be echoed back to the client 
        while amount_recv < amount_exp: 
            data = sock.recv(16) # Receive 16-bytes at a time 
            amount_recv += len(data)
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

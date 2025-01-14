#!/usr/bin/env python3 
import socket 
import sys 
# Reusing socket addressses 

# Run on specific port and return it after closing  
# Usually after closing , the port used will still register as in use , resulting in the "Address already in use" error 
# You can avoid this by using SO_REUSEADDR socket option 

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get old state of SO_REUSEADDR option 
    old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print(f"Old socket state : {old_state}\n")

    # Enable SO_REUSEADDR option 
    sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print(f"New socket state: {new_state}")
    
    local_port = 8282
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    print(f"Listening on port : {local_port}\n")
    while True:
        try:
            conn ,addr = srv.accept()
            print(f'Connected by: {addr[0]}:{addr[1]}\n')
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print(f"{msg}\n")


if __name__ == '__main__':
    reuse_socket_addr()

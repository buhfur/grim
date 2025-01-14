#!/usr/bin/env python3 

import socket 

def test_socket_mode():
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    
    s.setblocking(1) # Set to 0 for non-blocking 
    s.settimeout(0.5)
    s.bind(("0.0.0.0",0))
    socket_address = s.getsockname()
    print(f"Server launched on : {str(socket_address)}")
    while True:
        s.listen(1)

if __name__ == '__main__':
    test_socket_mode()

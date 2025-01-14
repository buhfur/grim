#!/usr/bin/env python3 

import socket 

# Changing socket timeout 

def test_socket_timeout() -> float:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create TCP socket 
    s.settimeout(100) # Set timeout for socket , default is None, used for the blocking-socket operations 
    return s.gettimeout() # Returns non-negative float


if __name__ == '__main__':
    print(f"Socket timeout: {test_socket_timeout()}")


#!/usr/bin/env python3 

# Modify socket send / recv buffer sizes 

import socket 

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buf_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF) # Get size of sockets send buffer 
    print(f"Buffer size [Before]: {bufsize}")
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_SNDBUF,
            SEND_BUF_SIZE)
    sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_RCVBUF,
            RECV_BUF_SIZE)
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print(f"Buffer size [After]: {bufsize}")

if __name__ == '__main__':
    modify_buf_size()

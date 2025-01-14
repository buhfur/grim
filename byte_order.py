#!/usr/bin/env python3 

import socket 

# Convert data to and from host and network byte order in both 32 bit and 16 bit 

def convert_byte_order():
    data = 1234
    # 32 bit
    long_order = f"Original : {data}\nLong Host Byte Order: {socket.ntohl(data)}\nLong Network Byte order: {socket.htonl(data)}\n"
    # 16 bit 
    short_order = f"Original : {data}\nShort Host Byte Order: {socket.ntohs(data)}\nShort Network Byte order: {socket.htons(data)}\n"
     
    return (long_order, short_order)


if __name__ == '__main__':
    long, short = convert_byte_order()
    print(long)
    print(short)

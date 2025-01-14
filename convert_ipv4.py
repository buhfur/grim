#!/usr/bin/env python3 
import socket
from binascii import hexlify
# Function that converts IPv4 addresses into 32-bit strings  
def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.3.104']: 
        pack_ip_addr = socket.inet_aton(ip_addr) # Converts IP to 32-bit byte string
        pack_ip_to_hex = hexlify(pack_ip_addr) # Convert binary to hexadecimal 
        print(f"pack_ip_addr : {pack_ip_addr}")
        unpacked_ip_addr = socket.inet_ntoa(pack_ip_addr)

        print(f"IP Address: {ip_addr}\nPacked IP Address: {hexlify(pack_ip_addr)}\nUnpacked IP: {unpacked_ip_addr}\n")

def find_serv_by_port():
    services = {} 
    for x in range(1,1024):
        try:
            services[x] = socket.getservbyport(x)
        except OSError:
            continue
    return services
if __name__ == '__main__':
    #convert_ip4_address()
    services = find_serv_by_port()
    for x in services.keys():
        print(f"Port number : {x}\nPort Service Name: {services[x]}\n")





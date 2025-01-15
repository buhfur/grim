#!/usr/bin/env python3 
import socket 
import ntplib
from time import ctime 


# Print current time from time server 
def print_time():
    ntp_client = ntplib.NTPClient() # Create instance of NTPClient 
    response = ntp_client.request('pool.ntp.org') # make request to NTP server 
    print(ctime(response.tx_time))

if __name__ == '__main__':
    print_time()


import socket 

if __name__ == '__main__':
    domain = 'www.google.com'
    print(socket.gethostbyname(domain)) # Get IP of remote host 
    print(socket.gethostbyname(socket.gethostname())) # Get IP of local host, no interface specified

    # Convert IPv4 address into 32 bit binary string 
    

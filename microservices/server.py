import socket

def server():
    '''this microservice will listen for network requests and respond'''
    # AF_INET works over IP4 SOCK_STREAM is for sending normal-sized packets of data
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # a tuple to configure the port
    port_t = ('localhost', 9876) # or 127.0.0.1
    server.bind(port_t)
    # we can ask our server to listen out for any requsts
    server.listen()
    print(f'Server is running on {port_t[0]} port {port_t[1]}')
    # we usually have a run loop
    while True:
        '''this will loop endlessly'''
        # accept any requests that may happen
        (client, addr) = server.accept() # unpack the information from the client
        print(f'Server received a request from {addr}')
        # read just the first few bytes from the client
        buf = client.recv(1024) # only take the first 1024 bytes
        print(f'Server received {buf}') # buf will be in bytes


if __name__ == '__main__':
    server()
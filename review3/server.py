# we can build a socket server
import socket # this provides all we need for socket programming
from datetime import datetime
import requests
import json

def getData(cat='albums', id=''):
    if id=='':
        apiUrl = f'https://jsonplaceholder.typicode.com/{cat}'
    else:
        apiUrl = f'https://jsonplaceholder.typicode.com/{cat}/{id}'
    response = requests.get(apiUrl)
    response_l = response.json() # or html, text etc
    response_j = json.dumps(response_l)
    # response_j = response.json() # or html, text etc
    # we could do some pre-procesing, e.g. filter, clean, authenticate...
    return response_j

def writeTofile(buf):
    with open('server_log', 'ab') as fout:
        fout.write(buf)

def server():
    '''this microservice will listen for request, respond to request
       and be available over an http port '''
    # here are some good defaults for a microservice
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # we need some port settings
    port_t = ('localhost', 9876) # or a fixed IP address
    server.bind(port_t)
    # set our server to listen
    server.listen()
    print(f'Server is running on {port_t[0]} port {port_t[1]}')
    # we need a run loop
    while True:
        # unpack any request we may recieve
        (client, addr) = server.accept()
        print(f'request received from {addr}')
        # read the first 1024 bytes of the buffer
        # buf = client.recv(4)
        # we could write logic to examine the buffer for 'fingerprints' telling us the nature of the data
        # if we want to take more of the client data...
        # buf2= client.recv(4)
        # we usually assign a loop to do this
        # rec = [] # an empty list
        # while True:
        #     b = client.recv(4)
        #     if len(b)>0: # be a bit more careful here
        #         rec.append(b)
        #     else:
        #         break
        # for _ in rec:
        #     print(_)
        # see https://coderivers.org/blog/python-socket-recv/#buffer-sizing
        bufSize = 4 # 1024
        buf = b''
        while True:
            data = client.recv(bufSize) 
            print(f'Next {bufSize} bytes: {data}')
            if not data:
                break
            buf += data

        # persist the request in a byte file
        writeTofile(buf)

        # we can choose to send a response
        print(f'Server received {buf}')
        received = buf.decode()
        if '/' in received:
            (cat, id) = received.split('/')
            r = getData(cat, id)
            message = f'{r}'.encode()
           
        elif received=='date':
            message = datetime.now()
            client.send( f'{message}'.encode() ) # we would format the date
        elif received=='time':
            message = datetime.now().strftime("%H:%M:%S").encode()
        else:
            message = received.upper().encode()
        # client.send( message )
        client.close()
        # if the client sends b'quit' then we will close the server
        if buf == b'quit':
            print('server is closing')
            server.close()
            break
        

if __name__ == '__main__':
    server()
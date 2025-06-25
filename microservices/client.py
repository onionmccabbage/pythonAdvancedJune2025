import socket
import sys

def client():
    '''This network client will send a request to a server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # match the server
    port_t = ('localhost', 9876)
    # make a connection to the server
    client.connect(port_t)
    # send some byte-encoded data to the server
    if len(sys.argv) > 1: # there will always be the file name
        msg = (' '.join(sys.argv[1:])).encode() # combine all the additional arguments into a space-separated string
    else:
        msg = 'Hello'.encode() # or b'Hello'
    client.send(msg)
    client.close() # always a good idea to tidy up


if __name__ == '__main__':
    client()

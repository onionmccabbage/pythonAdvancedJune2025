import socket
# see https://www.tutorialspoint.com/determine-the-type-of-an-image-in-python
import imghdr

def findImageKind():
    with open('phone.png', 'rb') as finb:
        b = finb.read()
        print(b)
    imgKind = imghdr.what('', b) # imghdr.what('filename' [,bytestring]) # one or the other
    print(imgKind)

def client():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")

if __name__ == '__main__':
    # findImageKind()
    client()
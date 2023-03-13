# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send 'GET_KEY' to download a string.
# The string is compressed with a common algorithm found in many
# websites. Decompress the string and print it to get the flag.

import socket
import string
import gzip

def getEncryptedMessages(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'GET_KEY')
        data = s.recv(2048)
        return data
      
message = getEncryptedMessages('localhost',10000)
print(message)
message = gzip.decompress(message)
print(message)

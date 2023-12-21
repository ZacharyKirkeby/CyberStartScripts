# Connect over TCP to the following server: 'localhost', 10000
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline

import socket
import string

host = 'localhost'
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'GET')
data = s.recv(2048).decode()
encryptedMessages = data.split('\n')
miniDictionary = [' OF ',' AND ',' OR ',' BE ',' THE ',' MY ',' HER ',' I ',' FOR ',' IF ',' ARE ',' AN ',' THEY ',' BUT ',' SO ', ' YOU ',' TO ']
print(data)  

def tryAll(phrasesList):
    for i in range(0,4):
        for k in range(27):
            message = caesarCipher(phrasesList[i],k)
            for words in miniDictionary:
              	if words in message: 
                  encryptedMessages[i] = message
  

                  
                  
def caesarCipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            result += shift_char
        else:
            result += char
    return result


tryAll(encryptedMessages)
encryptedMessages.pop(0)
encryptedMessages.pop(3)
responseString = encryptedMessages[0] + '\n' + encryptedMessages[1] + '\n' + encryptedMessages[2]
s.sendall(responseString.encode())
data = s.recv(2048).decode()
print(data)

    
    
    

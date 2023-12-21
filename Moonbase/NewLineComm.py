import socket
import string


def get_encrypted_messages(host, port):
    """connect to the server and retrieve encrypted messages"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'GET')
        data = s.recv(2048).decode()
        return data

def send_decrypted_messages(host, port, messages):
    """connect to the server and send decrypted messages"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(messages.encode())
        data = s.recv(2048).decode()
        return data

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            result += shift_char
        else:
            result += char
    return result
  
  
  
host = 'localhost'
port = 10000
encrypted_messages = get_encrypted_messages(host, port).split('\n')

miniDictionary = [' OF ',' AND ',' OR ',' BE ',' THE ',' MY ',' HER ',' I ',' FOR ',' IF ',' ARE ',' AN ',' THEY ',' BUT ',' SO ', ' YOU ',' TO ']

def tryAll(phrasesList):
    for i in range(0,4):
        for k in range(27):
            message = caesar_cipher(phrasesList[i],k)
            for words in miniDictionary:
              	if words in message: 
                  encrypted_messages[i] = message
                 
  
tryAll(encrypted_messages)
encrypted_messages.pop(0)
encrypted_messages.pop(3)
#print(encrypted_messages)
responseString = encrypted_messages[0] + '\n' + encrypted_messages[1] + '\n' + encrypted_messages[2]
print(responseString)
response = send_decrypted_messages(host, port, responseString)
print(response)
  
  

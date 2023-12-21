# Connect to the  server at 'localhost', 10000 send any data,
# the server will respond with the required word codes
# You will find a passage of text in the file backdoor.txt. Write a script
# which will use that text to build a message using the received word codes.
# Each word code is sent on a new line and contains
# paragraph_number, line_number, word_number from backdoor.txt
# Send the expected words back to the server to retrieve the flag.
# The server expects all the words in a single transmission.
# The words should have punctuation stripped from them.
# And the words should be separated by newline characters (\n)

import socket
import string

host = 'localhost'
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'GET')
data = s.recv(2048).decode()
codes = data.split('\n')
print(data)
message = ''
backDoor = open('backdoor.txt','r')
paragraphs = backDoor.read().split('\n'+'\n')
i = 0
for nums in range(6):
  pos = codes[i].split(',')
  num = int(pos[0])
  paragraph = paragraphs[int(num)-1]
  num = int(pos[1])
  sentance = paragraph.split('\n')
  words = sentance[int(num)-1].split(' ')
  num = int(pos[2])
  message = message+words[int(num)-1]+' '
  i+=1
  
message = message.translate(str.maketrans('', '', string.punctuation))
print(message)

s.sendall(message.encode())
data = s.recv(2048).decode()
print(data)




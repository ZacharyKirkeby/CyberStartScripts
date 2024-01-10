import urllib.request, urllib.error, urllib.parse

link = "http://www.chiquitooenterprise.com/password"
cipher = urllib.request.urlopen(link).read().decode('utf-8')
revString = cipher[::-1]


answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = urllib.request.urlopen(answer)
response = response.read()
print(response.decode('utf-8'))

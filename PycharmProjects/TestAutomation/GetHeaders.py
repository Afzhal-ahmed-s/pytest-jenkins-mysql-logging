import requests

headerdata = {'T1' : "First_Header", 'T2' : "Second_Header"}

# sending customized header
response = requests.get('https://httpbin.org/get', headers= headerdata)

print(response.text)

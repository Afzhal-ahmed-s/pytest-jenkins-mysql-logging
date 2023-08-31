import  requests

param = {"name": "Dua Lipa", "email": "dl@mail.com", "gender": "female"}

# sending parameters
response = requests.get('https://httpbin.org/get', params = param)
print(response.text)

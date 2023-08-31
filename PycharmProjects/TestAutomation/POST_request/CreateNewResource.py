import json
import  jsonpath
import requests

url = "https://reqres.in/api/users"

# reading input json file

file = open("/home/afzhal-ahmed-s/PycharmProjects/createUser.json", 'r')
json_input = file.read() # jsonInput is string data type here
request_json = json.loads(json_input)

print(request_json)

response = requests.post(url, request_json)
print(response.headers)
print(response.content)
print(response.headers.get("Content-Length"))

# parse response in JSON format
responseJson = json.loads(response.text)

# pick id using JSON path
id = jsonpath.jsonpath(responseJson, 'id')
print(id[0])

#assertion
assert response.status_code == 201


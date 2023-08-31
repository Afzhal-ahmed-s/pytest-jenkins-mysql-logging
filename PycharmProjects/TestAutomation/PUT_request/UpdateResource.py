import json
import  requests
import jsonpath

url = "https://reqres.in/api/users/2"

file = open("/home/afzhal-ahmed-s/PycharmProjects/updateUser.json", 'r')
jsonInput = file.read() # jsonInput is string data type here
requestJson = json.loads(jsonInput)

# making PUT request
response = requests.put(url, requestJson)
print(response.content)

#parse response
responseJson = json.loads(response.text)

updated = jsonpath.jsonpath(responseJson, 'updatedAt')
print(updated[0])

assert response.status_code == 200

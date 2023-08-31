import json
import requests
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)

print("Response body: ", response.content)
print("Header: ", response.headers)

print(response.headers.get("Connection"))

print(response.cookies)

print(response.encoding)

print(response.elapsed)

print(response.status_code)

assert response.status_code == 200

jsonResponse = json.loads(response.text)
print(jsonResponse)

# always returns a list
pages = jsonpath.jsonpath(jsonResponse, 'total_pages')
email = jsonpath.jsonpath(jsonResponse, 'data[0].email')
firstName = jsonpath.jsonpath(jsonResponse, 'data[0].first_name')

print(pages[0])
print(email)
print(firstName)
print(jsonpath.jsonpath(jsonResponse, 'data'))

for i in range(0, 3):
    print(jsonpath.jsonpath(jsonResponse, 'data['+str(i)+'].first_name'))


assert pages[0] == 2


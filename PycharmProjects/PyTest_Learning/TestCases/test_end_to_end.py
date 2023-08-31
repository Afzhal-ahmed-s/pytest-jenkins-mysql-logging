import  requests
import json
import jsonpath

def test_Add_new_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/home/afzhal-ahmed-s/PycharmProjects/S14RequestJson.json", 'r')
    json_requests = json.loads(file.read())
    response = requests.post(API_URL, json_requests)
    id = jsonpath.jsonpath(response, 'id')
    print(response.text)
    print(id[0])
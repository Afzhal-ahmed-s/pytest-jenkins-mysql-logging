import requests
import json
import jsonpath

def test_add_student_data():
    API_URL= "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/home/afzhal-ahmed-s/PycharmProjects/S14RequestJson.json", 'r')
    json_requests = json.loads(file.read())
    response = requests.post(API_URL, json_requests)
    print(response.text)

def test_update_student_data():
    API_URL= "http://thetestingworldapi.com/api/studentsDetails/3034"
    file = open("/home/afzhal-ahmed-s/PycharmProjects/S14PUT_request.json", 'r')
    json_requests = json.loads(file.read())
    response = requests.put(API_URL, json_requests)
    print(response.text)

def test_get_student_data():
    API_URL= "http://thetestingworldapi.com/api/studentsDetails/3034"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print("response: ", response.text)
    print("id: ", id)
    assert id[0] == 3034


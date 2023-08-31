import json
import jsonpath
import requests
import pytest

url = "https://reqres.in/api/users"
a = 100

@pytest.fixture()
def start_exe():
    global file
    file = open("/home/afzhal-ahmed-s/PycharmProjects/createUser.json", 'r')

@pytest.mark.skipif(a > 100, reason="I'm experimenting.")
def test_create_new_user(start_exe):
    json_input = file.read()  # jsonInput is string data type here
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    print(response.content)
    responseJson = json.loads(response.text)
    # assertion
    assert response.status_code == 201


def test_create_other_user(start_exe):
    json_input = file.read()  # jsonInput is string data type here
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

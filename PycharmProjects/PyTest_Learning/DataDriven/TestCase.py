import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_multiple_students():

    # API
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/home/afzhal-ahmed-s/PycharmProjects/AddNewStudent.json")
    json_request = json.loads(file.read())

    obj = Library.Common("/home/afzhal-ahmed-s/Downloads/Noduco_Udemy_C-PPA.xlsx", 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row + 1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(API_URL, updated_json_request)
        print(response)

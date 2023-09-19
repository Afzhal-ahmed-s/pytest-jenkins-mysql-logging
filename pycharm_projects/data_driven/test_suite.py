import requests
import json
import jsonpath
import openpyxl
from data_driven import Library

demo_data = [
    {"name": "afzhal", "age": 24}, {"name": "ameer", "age": 24},
    {"name": "akram", "age": 24}, {"name": "vishal", "age": 24},
    {"name": "nitin goyal", "age": None}, {"name": "nitin chawla", "age": None}
]


def test_excel_to_json_payload_then_api_request():
    API_URL = "https://08f3b843-f00e-4b65-a9e0-2ea4eac2eee5.mock.pstmn.io/data_driven/demo"

    file = open("/home/afzhal-ahmed-s/PycharmProjects/excel1_demo.json")
    json_request = json.loads(file.read())

    obj = Library.Common("/home/afzhal-ahmed-s/Downloads/Noduco_Udemy_C-PPA.xlsx", 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row + 1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        print("source: 'test_suite.py', received->", updated_json_request)

        response = requests.post(API_URL, updated_json_request)
        print(response.text)


def test_list_of_json_to_excel_data_insertion():
    file = open("/home/afzhal-ahmed-s/PycharmProjects/excel1_demo.json")
    json_request = json.loads(file.read())

    obj = Library.Common("/home/afzhal-ahmed-s/Downloads/Noduco_Udemy_C-PPA.xlsx", 'Sheet2')
    column_title = list(demo_data[0].keys())
    number_of_columns = len(column_title)
    number_of_rows = len(demo_data)

    print("number of columns: ", number_of_columns)
    print("number of rows: ", number_of_rows)

    # column title insertion
    for i in range(1, 2):
        obj.set_column_data(1, number_of_columns, column_title)

    # row wise data insertion
    for i in range(1, number_of_rows):
        obj.set_column_data(i+1, number_of_columns, list(demo_data[i].values()))


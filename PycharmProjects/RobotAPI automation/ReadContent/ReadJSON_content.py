import json

def read_request_content():
    file = open("/home/afzhal-ahmed-s/PycharmProjects/V160Request.json", 'r')
    jsonFile = file.read()
    json_content = json.loads(jsonFile)
    return json_content

x = read_request_content()
print(x)

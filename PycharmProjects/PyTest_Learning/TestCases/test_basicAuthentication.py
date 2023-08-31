import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get("https://api.github.com/user", auth= HTTPBasicAuth("writetoafzhalahmeds@gmail.com", "githubafz1"))
    print(response.text)
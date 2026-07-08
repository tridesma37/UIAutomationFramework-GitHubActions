import copy
from api_requests.auth_request import AuthRequest
from utils.data_reader import read_json
from utils.helper import random_email

def test_register():
    user = read_json("test_data/user.json")
    user = copy.deepcopy(user)
    user["email"] = random_email()
    response = AuthRequest.register(user)
    assert response.status_code in [200, 201]
    body = response.json()
    assert body["success"] == True

def test_login():
    user = read_json("test_data/user.json")
    response = AuthRequest.login(user)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

def test_me(token):
    response = AuthRequest.me(token)
    assert response.status_code == 200
    body = response.json()
    assert body["success"] == True

def test_negative_register():
    user = {
        "nama": "",
        "email": "abc",
        "password": "123"
    }
    response = AuthRequest.register(user)
    assert response.status_code in [400, 422]
    body = response.json()
    assert body["success"] == False
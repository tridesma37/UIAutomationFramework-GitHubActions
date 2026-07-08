import pytest

from api_requests.auth_request import AuthRequest
from utils.data_reader import read_json


@pytest.fixture(scope="session")
def token():

    user = read_json("test_data/user.json")

    response = AuthRequest.login(user)

    token = response.json()["data"]["token"]

    return token
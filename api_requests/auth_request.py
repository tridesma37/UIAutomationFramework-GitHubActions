import requests
from utils.config import BASE_URL


class AuthRequest:

    @staticmethod
    def register(data):
        return requests.post(
            f"{BASE_URL}/api/auth/register",
            json=data
        )

    @staticmethod
    def login(data):
        return requests.post(
            f"{BASE_URL}/api/auth/login",
            json=data
        )

    @staticmethod
    def me(token):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        return requests.get(
            f"{BASE_URL}/api/auth/me",
            headers=headers
        )

    @staticmethod
    def logout(token):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        return requests.post(
            f"{BASE_URL}/api/auth/logout",
            headers=headers
        )
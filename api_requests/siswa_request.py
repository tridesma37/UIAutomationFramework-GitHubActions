import requests
from utils.config import BASE_URL


class SiswaRequest:

    @staticmethod
    def get_all(token):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        return requests.get(
            f"{BASE_URL}/api/siswa",
            headers=headers
        )

    @staticmethod
    def create(token, data):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        return requests.post(
            f"{BASE_URL}/api/siswa",
            headers=headers,
            json=data
        )

    @staticmethod
    def get_by_id(token, siswa_id):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        return requests.get(
            f"{BASE_URL}/api/siswa/{siswa_id}",
            headers=headers
        )

    @staticmethod
    def delete(token, siswa_id):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        return requests.delete(
            f"{BASE_URL}/api/siswa/{siswa_id}",
            headers=headers
        )
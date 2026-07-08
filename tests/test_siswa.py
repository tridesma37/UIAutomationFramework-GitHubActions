from api_requests.siswa_request import SiswaRequest
from utils.data_reader import read_json

student_id = ""
import random
def test_create_student(token):
    global student_id
    siswa = read_json("test_data/siswa.json")
    angka = random.randint(10000, 99999)
    siswa["nis"] = str(angka)
    siswa["email"] = f"siswa{angka}@gmail.com"
    siswa["telepon"] = f"08123{angka}"
    response = SiswaRequest.create(token, siswa)
    print("STATUS :", response.status_code)
    print("BODY   :", response.text)
    assert response.status_code in [200, 201]
    body = response.json()
    assert body["success"] is True
    student_id = body["data"]["id"]

def test_get_all_student(token):
    response = SiswaRequest.get_all(token)
    assert response.status_code == 200
    body = response.json()
    assert body["success"] == True
    assert len(body["data"]) > 0

def test_get_student(token):
    response = SiswaRequest.get_by_id(token, student_id)
    assert response.status_code == 200
    body = response.json()
    assert body["success"] == True

def test_delete_student(token):
    print("Student ID :", student_id)
    response = SiswaRequest.delete(token, student_id)
    print("DELETE STATUS :", response.status_code)
    print("DELETE BODY   :", response.text)
    assert response.status_code == 200
    print(response.text)
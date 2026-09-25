import requests

BASE_URL = "https://automationintesting.online/api"


def test_login_valid_credentials():
    url = f"{BASE_URL}/auth/login"
    payload = {"username": "admin", "password": "password"}
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert "token" in response.json()


def test_login_invalid_credentials():
    url = f"{BASE_URL}/auth/login"
    payload = {"username": "admin", "password": "wrongpass"}
    response = requests.post(url, json=payload)

    assert response.status_code == 401
import requests

BASE_URL = "https://automationintesting.online/api"


def test_create_booking():
    url = f"{BASE_URL}/booking/"
    payload = {
        "roomid": 1,
        "firstname": "Frantisek",
        "lastname": "Tester",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-05"
        }
    }
    response = requests.post(url, json=payload)

    # Verify status code
    assert response.status_code == 200

    # Verify response body
    data = response.json()
    assert data["booking"]["firstname"] == "Frantisek"
    assert data["booking"]["lastname"] == "Tester"
    assert data["booking"]["roomid"] == 1
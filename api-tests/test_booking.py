import requests
import random
from datetime import datetime, timedelta

BASE_URL = "https://automationintesting.online/api"


def test_create_booking():
    # Generate unique dates to avoid 409 Conflict
    checkin = (datetime.now() + timedelta(days=random.randint(30, 365))).strftime("%Y-%m-%d")
    checkout = (datetime.now() + timedelta(days=random.randint(366, 400))).strftime("%Y-%m-%d")

    url = f"{BASE_URL}/booking/"
    payload = {
        "roomid": 1,
        "firstname": "Frantisek",
        "lastname": "Tester",
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        }
    }
    response = requests.post(url, json=payload)

    # 201 Created is the correct response for a new booking
    assert response.status_code == 201

    # Verify response body — the API returns data directly, not nested under "booking"
    data = response.json()
    assert data["firstname"] == "Frantisek"
    assert data["lastname"] == "Tester"
    assert data["roomid"] == 1
    assert data["bookingdates"]["checkin"] == checkin
    assert data["bookingdates"]["checkout"] == checkout
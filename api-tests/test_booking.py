import requests
import random
from datetime import datetime, timedelta

BASE_URL = "https://automationintesting.online/api"


def test_create_booking():
    # Generate unique dates far in the future to avoid conflicts
    # Use a random offset between 2 and 3 years from today
    checkin_date = datetime.now() + timedelta(days=random.randint(730, 1095))
    checkout_date = checkin_date + timedelta(days=random.randint(1, 5))

    checkin = checkin_date.strftime("%Y-%m-%d")
    checkout = checkout_date.strftime("%Y-%m-%d")

    # Use a random room (1-3) to spread bookings across rooms
    roomid = random.randint(1, 3)

    url = f"{BASE_URL}/booking/"
    payload = {
        "roomid": roomid,
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
    # If 409 (conflict), skip the test instead of failing — it's a data collision, not a bug
    if response.status_code == 409:
        import pytest
        pytest.skip(f"Room {roomid} already booked for {checkin} - {checkout}. Skipping.")

    assert response.status_code == 201, f"Expected 201, got {response.status_code}: {response.text}"

    # Verify response body — the API returns data directly, not nested under "booking"
    data = response.json()
    assert data["firstname"] == "Frantisek"
    assert data["lastname"] == "Tester"
    assert data["roomid"] == roomid
    assert data["bookingdates"]["checkin"] == checkin
    assert data["bookingdates"]["checkout"] == checkout
import pytest
import requests


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking():
    put_URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Vandana",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=put_URL, headers=headers, json=json_payload)
    print(type(put_URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the response body and verify the JSON, Booking id is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


# Advantage of this is
@pytest.fixture()
def read_csv_file_data():
    pass

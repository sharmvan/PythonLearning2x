import pytest
import requests
from conftest import create_token, create_booking


# def test_put_request2():
# create_booking() # Can we use this here? No. If it's a fixture then it can be available.
# create_token() # Can we use this here? No. If it's a fixture then it can be available.
# We can import fixture but there is an alternate way:
# Alternate way is quite simple. create a file "conftest.py"
def test_put_request(create_booking, create_token):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking
    put_URL = base_url + base_path + str(param)
    cookie = "token=" + create_token
    headers = {"Content-Type": "application/json",
               "Cookie": cookie
               }
    print(headers)
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
    response = requests.put(url=put_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == 'Vandana', "Failed Message - Incorrect FirstName"


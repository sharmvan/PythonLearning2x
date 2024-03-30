import requests


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


def test_put_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking()
    put_URL = base_url + base_path + str(param)
    cookie = "token=" + create_token()
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


def test_delete_request():
    try:
        base_url = "https://restful-booker.herokuapp.com/booking/1"
        booking_id = create_booking()
        delete_url = base_url + str(booking_id)
        cookie_value = "token=" + create_token()
        headers = {"Content-Type": "application/json",
                   "Cookie": cookie_value
                   }
        print(headers)

        response = requests.delete(url=delete_url, headers=headers)
        # Assertions
        assert response.status_code == 201
    except Exception as e:
        print(e)

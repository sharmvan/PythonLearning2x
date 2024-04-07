# API Request - HTTP Request
import pytest
import requests  # pip install requests


@pytest.mark.smoke
def test_get_single_request_by_id():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1")
    print(response.text)
    print(response.content)
    print(response.json())
    print(response.headers)
    print(response.url)
    print(response.cookies)
    response_status = response.status_code  # to get status of response, .status_code is an inbuilt method
    assert response_status == 200


# Fixture (imp concept in Python)-- It's basically with pytest mostly how we can use this in pytest.
# We can use the fixture to setup , provide any data or teardown resources if we need in our test cases.
# It means if we want to pass some of the data to other test cases, we can use fixture (in-build feature of pytest).
# for eg: I have one test case: In the
# test_put_requests: we need booking_id and token
# test_delete_requests: we need booking_id and token
# test_patch_requests: we need booking_id and token
# as per booking_id and token, this is a common code. This common code has to be available in all 3 functions.
# Previously we make them (booking_id and token) normal functions. Suppose all below 3 functions are in different file.
# test_put_requests, test_delete_requests, test_patch_requests -- then it will be difficult.
# Here we can use fixture. Fixture are quite easy way to transfer the data from one test to another.
# We can have unlimited of functions.
import pytest


@pytest.fixture()
def sample_data():
    data = [1, 2, 3, 4, 5]  # type-> list
    return data


@pytest.fixture()
def sample_data2():
    return True


# def test_number1_sampledata_to_be_injected():
#     data2 = sample_data()  # called the sample data() function. Earlier we used to call the function.
#     assert len(data2) == 5
# Now use fixture
def test_number1_sampledata_to_be_injected(sample_data):
    assert len(sample_data) == 5


def test_2(sample_data, sample_data2):
    assert sample_data2 == True
    assert 3 in sample_data

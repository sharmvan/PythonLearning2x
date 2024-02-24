# Real example of key value pair is:
# below we will see in json API responses:
# Advantage of dictionary is: It's very similar to jason.
api_response = {
    "first_name": 'Vandana',
    "age": 96,
    "last_name": 'Sharma',
    "email_address": 'www.yahoo.in',
    "password": "google@23232",
    "contact_no": 12345678
}
print(len(api_response))
print(api_response)
print(type(api_response))

# How can I get the password?
pass_w1 = api_response["password"]
pass_w2 = api_response.get('password')
print(pass_w1)
print(pass_w2)

# How to iterate over dictionary? by using "for" loop.
for k, v in api_response.items():
    print(k, "-->", v)

# Dictionary is mutable in nature. Can we change the value of "password"?
api_response["password"] = 'yah00@23232'
print(api_response)

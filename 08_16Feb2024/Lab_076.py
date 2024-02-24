# Where we can use tuple? Suppose when any freshers will come in the project, they won't be able to change it.
# below is the Real based scenario
api_url = ('www.testingacademy.com', 'www.google.com', 'www.flipkart.com')
print(api_url)
print(api_url[1])
print(type(api_url))
api_url[1]= "www.yahoo.in" # TypeError: 'tuple' object does not support item assignment
print(api_url)

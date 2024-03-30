from faker import Faker

# create a faker instance
fake = Faker()

# Generate a fake name
print(fake.name())
# output might be something like "John Doe"

# Generate a fake address
print(fake.address())
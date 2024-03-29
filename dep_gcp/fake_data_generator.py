import pandas as pd
from faker import Faker

fake = Faker()

num_rows = 100

test_data = {
    'Name': [fake.name() for _ in range(num_rows)],
    'Address': [fake.address() for _ in range(num_rows)],
    'Email': [fake.email() for _ in range(num_rows)],
    'Phone Number': [fake.phone_number() for _ in range(num_rows)],
    'Date of Birth': [fake.date_of_birth() for _ in range(num_rows)]
}

df = pd.DataFrame(test_data)

df.to_excel('fake_data.xlsx', index=False, header=True)

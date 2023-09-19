import random
import requests

# Sample data
names = ["Ali", "Fatima", "Ahsan", "Sana", "Imran", "Hina", "Bilal", "Zara", "Mehmood", "Fariha"]
cities = ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Faisalabad", "Multan", "Gujranwala", "Sialkot", "Quetta", "Peshawar"]
blood_types = ["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"]

# Generate 50 sample objects
sample_objects = []
# Define the URL of the endpoint
url = "http://127.0.0.1:8000/donor/create"
for _ in range(50):
    sample_object = {
        "name": random.choice(names),
        "email": "user@example.com",
        "phone_number": "92" + str(random.randint(3000000000, 9999999999)),
        "blood_type": random.choice(blood_types),
        "last_donation_date": "2023-09-10",
        "is_active": random.choice([True, False]),
        "address": "Sample Address",
        "city": random.choice(cities)
    }
        # Send a POST request with the data
    response = requests.post(url, json=sample_object)

    # Check the response from the server
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")

# Now, sample_objects contains 50 objects with random names and Pakistani cities

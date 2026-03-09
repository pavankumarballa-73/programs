#TASK-1:

import json

user_profile = {
    "name": "Alex",
    "age": 25,
    "email": "alex@example.com",
    "is_active": True,
    "skills": ["Python", "Java", "SQL"]
}

json_data = json.dumps(user_profile, indent=4)
print(json_data)

TASK-2:

import json

api_response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'

data = json.loads(api_response)

username = data["data"]["username"]
score = data["data"]["score"]

print(username)
print(score)
print(f"User {username} scored {score} points")

TASK-3:

import json

data = {
    "name": "Priya",
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "zip": "560001"
    }
}

# Extract city and zip
city = data["address"]["city"]
zip_code = data["address"]["zip"]

print(city)
print(zip_code)

# Add new key
data["address"]["country"] = "India"

# Print updated JSON
print(json.dumps(data, indent=4))

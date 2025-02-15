import json

with open("data.json", "r") as f:
    users = json.load(f)
    users.reverse()
    for user in users:
        print(f"{user['ime']} ove godine puni {2025-user['godine']} godina.")
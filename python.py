with open("data.txt", "w") as f:
    f.write("Andrijana, 2001\n")
    f.write("Ana, 2004\n")
    f.write("Milos, 2003\n")
    f.write("Branislava, 1977\n")

with open("data.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    ime, godine = line.strip().split(", ")
    print(f"{ime} ove godine puni {2025-int(godine)} godina.")

import json

users = []
for line in lines:
    ime, godine = line.strip().split(", ")
    users.append({"ime": ime, "godine": int(godine)})
    
with open("data.json", "w") as f:
    json.dump(users, f, indent=4)
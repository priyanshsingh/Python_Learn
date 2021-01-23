user = {"Name": "Priyansh", "Number": "9897684957", "purchases": [1, 2, 3, 4]}

print(user["Name"])
print(user["Number"])
print(user["purchases"])

user["Name"] = "Varun"
print(user)

for item in user.items:
    print(item)

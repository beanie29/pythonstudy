student = {
    "name": "Mark",
    "id": 1234,
    "feedback": None
}
try:
    print(student["last_name"])
except KeyError:
    print("Error finding last_name")

print("This code executes!")
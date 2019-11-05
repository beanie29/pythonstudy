pets = []

pet = {
    'name': 'donald',
    'type': 'dog',
    'owner': 'deidre',
    'legs': 'four',
}
pets.append(pet)

pet = {
    'name': 'stephen',
    'type': 'spider',
    'owner': 'sylvia',
    'legs': 'eight',
}
pets.append(pet)

pet = {
    'name': 'andrew',
    'type': 'aardvark',
    'owner': 'anthony',
    'legs': 'four',
}
pets.append(pet)

for pet in pets:
    print(f"Here's what I know about {pet['name'].title()}")
    for key, value in pet.items():
        print(f"\t{key.title()}, {value.title()}")

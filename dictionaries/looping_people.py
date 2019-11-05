people = []

person = {'first': 'andrew', 'last': 'jenkins', 'location': 'france', 'age': 48}
people.append(person)

person = {'first': 'andrew', 'last': 'bricknell', 'location': 'ireland', 'age': 47}
people.append(person)

person = {'first': 'matthew', 'last': 'davies', 'location': 'australia', 'age': 49}
people.append(person)

for person in people:
    name = f"{person['first']} {person['last']}"
    age = person['age']
    location = person['location']

    print(f"{name.title()} of {location.title()} is {age} years old")

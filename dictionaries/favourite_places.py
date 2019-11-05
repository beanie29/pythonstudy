favourite_places = {
    'yoko': ['tokyo', 'new york', 'hawaii'],
    'martin': ['tokyo', 'shiki'],
    'hana': ['tokyo'],
}

for person, places in favourite_places.items():
    print(f"{person.title()} likes the following places:")
    for place in places:
        print(f"\t{place.title()}")

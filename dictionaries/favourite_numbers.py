favorite_numbers = {
    'mandy': [42, 17],
    'micah': [23, 32],
    'gus': [7, 17],
    'hank': [1000_000, 10_000],
    'maggie': [0, 1],
    }

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")

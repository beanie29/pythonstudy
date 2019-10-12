filename = './foods.txt'
favourite_foods = [
    'pizza',
    'cheeseburgers',
    'carrot',
    'apples'
]
with open(filename, 'w') as f:
    for food in favourite_foods:
        f.write(food + '\n')


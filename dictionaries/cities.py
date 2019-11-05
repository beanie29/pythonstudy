cities = {
    'tokyo': {
        'country': 'japan',
        'population': '10 million',
        'fact': 'it has a live volcano'
    },
    'birmingham': {
        'country': 'england',
        'population': '2 million',
        'fact': 'they speak Brum'
    },
    'paris': {
        'country': 'france',
        'population': '5 million',
        'fact': 'you can see the Eiffel Tower'
    },
}

for city, city_info in cities.items():
    print(f"I know the following about {city.title()}:")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact.title()}")

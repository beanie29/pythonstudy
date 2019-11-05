favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    if len(languages) == 1:
        verb = 'is'
    else:
        verb = 'are'
    print(f"\n{name.title()}'s favourite languages {verb}")
    for language in languages:
        print(f"\t{language.title()}")

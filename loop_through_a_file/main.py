import fileinput

letters_count = {}

with fileinput.input() as in_file:
    for line in in_file:
        for letter in line.strip():
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count = 1
                
print(letters_count)
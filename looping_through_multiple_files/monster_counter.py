import fileinput
import pprint

results = {}
words_to_look_for = ('monster', 'monsters')

with fileinput.input(openhook=fileinput.hook_encoded("utf-8")) as f:
    for line in f:
        for word in line.split(' '):
            word = word.lower().strip('"')
            if word in results:
                results[word] +=1
            else:
                if word in words_to_look_for:
                    results[word] = 1   
print("Results: ")
pprint.pprint(results)
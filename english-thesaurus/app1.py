import json
from difflib import get_close_matches

data = json.load(open("python/english-thesaurus/data.json"))

word = input('Enter a word: ').lower()

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yN = input('Did you mean %s instead?[Y or N]: ' % get_close_matches(word, data.keys())[0]).upper()
        if yN == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yN == "N":
            return ("The word doesn't exist. Please double check it!")
        else:
            return ("We didn't understand your entry. Please try again!")
    else:
        return ("The word doesn't exist. Please double check it!")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
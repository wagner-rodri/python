import json

data = json.load(open("python/english-thesaurus/data.json"))

word = input('Enter a word: ')

def translate(word):
    if word in data:
        return data[word]
    else:
        return("The word doesn't exist, Please double check it!")

print(translate(word))
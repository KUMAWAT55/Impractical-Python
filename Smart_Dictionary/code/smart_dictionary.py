'''Interactive Python Dictionary with suggestions on wrong input'''
import json
from difflib import get_close_matches

def translate(data):
    '''Function traversing in json data to find meaning of word .'''
    word = input("Enter a word :").lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) < 1:
        return "Not Found"
    else:
        confirm = input("Are you trying something Like this : ''{}'' \nType Y/N to confirm ?\n".format(get_close_matches(word, data.keys(), cutoff=0.8)[0]))
        if confirm.lower() == 'y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        return "Ok !!"
def main():
    '''main function'''
    data = json.load(open("/home/rk/Desktop/Impractical-Python/Smart_Dictionary/files/data.json"))
    dec = translate(data)
    if isinstance(dec, list):
        for i in dec:
            print(i)
    else:
        print(dec)
if __name__ == '__main__':
    main()

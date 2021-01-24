import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translator(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(f"did you mean {get_close_matches(w, data.keys())[0]} instead? Y/N ").upper()
        if yn =="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please check and try again"
        else: 
            return "The program did not understand your input."

    else:
        return "The word does not exist. Please check"


word = input("enter a word: ")

output = translator(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
import json

data = json.load(open("data.json"))

while(True):
    search = input("What word would you like to look up?\n")

    try:
        definition = data[search.lower()]
        aString = ""
        aString =definition[0]
        print(aString)
        print("hold ctrl+c to exit\n")
    except:
        print("Word not found.")
        print("hold ctrl+c to exit\n")
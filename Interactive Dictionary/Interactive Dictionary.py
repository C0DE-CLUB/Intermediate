import json #JSON stands for JavaScript Object Notation
from difflib import get_close_matches
data = json.load(open(r'D:\windowPython\data.json')) #Here I am adding the change of directory to fit my computer 
#json.load takes the JSON string and converts it into a python dictionary

def translate(r): #We have defined translate to a namespace of r
    r = r.lower()
    if r in data:
        return data[r]
    elif r.title() in data:
        return data[r.title()]
    elif r.upper() in data: #verefing uppercase words in the json file like USA
        return data[r.upper()]
    elif len(get_close_matches(r, data.keys())) > 0:
        cz = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(r, data.keys())[0])
        if cz == "Y": # Lines 8 - 17 are statements trying to match with the word in a given search engine
            return data[get_close_matches(r, data.keys())[0]]
        elif cz == "N":
            return "The word doesn't exist. Please double check it." # Lines 18-23 are for ambiguous words the program can't understand
        else:
            return "We didn't understand your entry." 
    else:
        return "The word doesn't exist. Please double check it."
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output) # When executed the program wil print out the definition you searched for

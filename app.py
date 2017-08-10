# / dictlookup - looks up a specified word in a json dictionary.
# \
# / version: 1.0
# \ date: 2017.08.10
# / initial: 2017.08.10
# \ TODO:
# / - ensure the array formatting is removed and newlines between each definition.

import json
from difflib import get_close_matches


# sequencematcher/get_close_matches is used to test whether the string
# is close to a properly-spelled word.

# create array
data = json.load(open("data.json"))

# we access a word by addressing its key.
# data["rain"] will return the def.

def define(w):
    # | SequenceMatcher/get_close_matches:
    # |     create close matching structure (to allow for match possibilities)
    # |     can be done using get_close_matches(word, data.keys())
    # |     pass 0 at end to grab only the first word from get_close_matches.
    # |     We need to ensure that it does something even when there are no matches.

        # -scenario 1: empty list
        # -scenario 2: list of matches
        #   - if so, return the first item in the list ONLY.
        #     then pass a message to the user.

    w = w.lower() # automatically convert to lowercase for matching
    if w in data:
        return data[w] # if there is an actual match, then use it.
    # otherwise, use get_close_matches.
    # take the length of what get_close_matches returns,
    # and if it's greater than nothing, then pass the first item as a string.
    elif len(get_close_matches(w, data.keys())) >0:
        # in this case, you have a match suggested.

        # prior method:
        # return "Did you mean %s instead?" % get_close_matches(w,data.keys())[0]
            # use 0 as the first item. Show the user the matching word.

            # now we need to ask the user to respond, and do something or not.
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(w,data.keys())[0])
            yn = yn.lower()
            if yn =="y":
                correctedWord=str(get_close_matches(w,data.keys())[0])
                print(correctedWord)
                return data[get_close_matches(w, data.keys())[0]]
            elif yn=="n":
                print("the word doesn't exist. Please check it.")
            else:
                print("You don't like my suggestion?")
                # end check for similar word
    else:
        return "The word doesn't exist in this dictionary. Please check the\
         spelling and try again."


word = input("please enter a word: ")

# print(define(word)) - this was the previous way


# need to create an output var which cleans up the text entries.
output = define(word)

# for item in output: #iterate through each output
#     print(item) # print each item (doesn't work right now)
#     # need to discriminate a list from a string.

if type(output) == list:
    print("The word "+ word + " is defined as: ")
    for item in output:
        print(item) # print each item if there are is than one
else: # if it's not a list it has to be a string
    print("The word "+ word +" is defined as: ")
    print(output) #if a string, just print it.

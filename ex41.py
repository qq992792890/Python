import random
from urllib.request import urlopen
import sys
WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class names %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "*** = ***(@@@)":
        "From *** get the *** fumction, call ti with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."

}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))
## urlopen(WORD_URL).readlines() attention!! readline() will make wrong actions
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    #print("class_names: ",class_names)
    other_names = random.sample(WORDS,snippet.count("***"))
    #print("other_names: ",other_names)
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS,param_count)))

    for sentence in snippet,phrase:
        result = sentence[:]
        #i made a mistake that i write the : as 1

        for word in class_names:
            result = result.replace("%%%",word,1)
        for word in other_names:
            result = result.replace("***",word,1)
        for word in param_names:
            result = result.replace("@@@",word,1)
        results.append(result)
    return results

try:
    while True:
        snippets = list(PHRASES.keys()) 
        #print(snippets)
        random.shuffle(snippets)
        for snippet in snippets:
            phrase = PHRASES[snippet]
            #print("snippet: ",phrase)
            question,answer = convert(snippet,phrase)
            if PHRASES_FIRST:
                question,answer = answer,question
            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
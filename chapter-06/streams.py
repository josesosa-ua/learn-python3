import pprint

words = {}

with open("dictionary.txt", "r") as file:
    for line in file:
        entry = line.strip().split(" ")
        if len(entry) == 2:
            words[entry[0]] = entry[1]

pprint.pprint(words)
words["US"] = "EU"

with open("dictionary-updated.txt", "w") as file:
    for word in words:
        file.write(f"{word} {words[word]}\n")

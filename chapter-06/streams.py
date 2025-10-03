import  pprint as pp

words = {}
with open('dictionary.txt', 'r') as file:
    for line in file:
        line = line.strip()
        assignments = line.split(" ")
        if len(assignments) == 2:
            words[assignments[0]] = assignments[1]

while True:
    word = input('Enter a word: ')
    if word in words:
        print(f'The definition of "{word}" is: {words[word]}')
    elif word == 'exit':
        break
    else:
        print(f'No definition found for "{word}"')

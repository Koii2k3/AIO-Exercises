def count_chars(string):
    return {word: string.count(word) for word in list(string)}


string = 'Happiness'
print(count_chars(string))

string = 'smiles'
print(count_chars(string))

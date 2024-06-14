FILE_PATH = './P1_data.txt'


def count_word(path):
    with open(path) as f:
        string = f.read()
    string = string.lower().split()
    return {word: string.count(word) for word in string}


print(count_word(FILE_PATH))

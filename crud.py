#c - create
#r - read
#u - update
#d - delete

def add_word(dictionary: dict, word:str, definition: str, tags = None):
    if tags is None:
        tags = []
    if not word in dictionary:
        dictionary[word] = [definition, tags]

def find_word(dictionary: dict, word: str):
    if word in dictionary:
        print(f"{word}: {dictionary[word]}")
    else:
        print(f"{word} not found")

def view_dict(dictionary: dict):
    for x, y in dictionary.items():
        print(f"{x} : {y}")

def update_dict(dictionary: dict, key: str, defintion:str, tags = None):
    if key not in dictionary:
        print("Word not found")
        return
    if tags is None:
        tags = dictionary[key][1]
    dictionary[key] = [defintion, tags]

def delete_word(dictionary: dict, word: str):
    if word in dictionary:
        del dictionary[word]


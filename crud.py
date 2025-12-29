# data structure
# dictionary = {
#     "word" : {
#         "defintion" : "whatever the definition is",
#         "is_verb" : False,
#         "etymology" : "proto-word",
#         "" : ""
#     }
# }
# This is what we want the structure to look like

def add_word(dictionary: dict, word:str, definition: str, tags = None):
    if tags is None:
        tags = []
    if not word in dictionary:
        dictionary[word] = {"definition" : definition, "tags": tags}

def find_word(dictionary: dict, word: str):
    if word in dictionary:
        print(f"{word}: {dictionary[word]}")
    else:
        print(f"{word} not found")

def partial_search(dictionary: dict, query: str):
    return [word for word in dictionary if query.lower() in word.lower()]

def view_dict(dictionary: dict):
    for x, y in dictionary.items():
        print(f"{x} : {y}")

def update_dict(dictionary: dict, key: str, definition:str, tags = None):
    if key not in dictionary:
        print("Word not found")
        return
    if tags is None:
        tags = dictionary[key]["tags"]
    dictionary[key] = {"definition" : definition, "tags" : tags}

def delete_word(dictionary: dict, word: str):
    if word in dictionary:
        del dictionary[word]


import crud
import storage

def while_empty(x):
    while not x:
        print("Please enter a valid value")
        x = input()
    return x

print("Please enter the name of the dictionary file (must end in '.json'). If you haven't yet created a file, please just press enter.")
file_name = input()

if not file_name:  # if enter is pressed without any input, new file created
    print("Please enter what you'd like to name your dictionary file. Make sure it ends in .json")
    file_name = input()

    while not file_name.endswith(".json"):
        print("Please enter a file name ending in '.json'")
        file_name = input()
    storage.create_dict(file_name)

temp_dict = storage.load_dict(file_name)
running = True
labels = []

while running:
    print("Press and enter 'Q' to quit the programme.")
    print("To create a word in your dictionary, enter 'C'.")
    print("To read your entire dictionary, enter 'R'.")
    print("To find a word from your dictionary, enter 'F'.")
    print("To perform a partial search, enter 'P'.")
    print("To update a word from your dictionary, enter 'U'.")
    print("To delete a word from your dictionary, enter 'D'.")
    command = input().upper()
    match command:
        case "Q":
            storage.save_dict(file_name, temp_dict)
            running = False

        case "C":
            print("Enter the word you'd like to add")
            word = input()
            word = while_empty(word)

            print("Now, enter the definition of the word")
            definition = input()
            definition = while_empty(definition)
            
            while True:
                print("If you'd like to add a label, please enter it. Else, press enter. " \
                "Or press enter once you've entered all your labels")
                label = input()
                if not label:
                    break
                labels.append(label)
                    
            crud.add_word(temp_dict, word, definition, labels)
            labels = []

        case "R":
            crud.view_dict(temp_dict)

        case "F":
            print("Please enter the word you'd like to find")
            word = input()
            word = while_empty(word)
            crud.find_word(temp_dict, word)
        
        case "P":
            print("Please enter what you'd like to search for")
            query = input()
            query = while_empty(query)
            results = crud.partial_search(temp_dict, query)
            if results:
                for result in results:
                    print(result)
            else:
                print("No results.")
            
        case "U":
            print("Please enter the word whose values you'd like to update")
            word = input()
            word = while_empty(word)

            print("Please enter what you'd like the definition to be")
            definition = input()
            definition = while_empty(definition)

            while True:
                print("If you'd like to add a label, please enter it. Else, press enter. " \
                "Or press enter once you've entered all your labels")
                label = input()
                if not label:
                    break
                labels.append(label)
                
            crud.update_dict(temp_dict, word, definition, labels)
            labels = []

        case "D":
            print("Please enter the word you'd like to delete.")
            word = input()
            word = while_empty(word)

            crud.delete_word(temp_dict, word)
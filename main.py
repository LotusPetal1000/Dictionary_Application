import crud
import storage

def while_empty(x):
    while not x:
        print("Please enter a valid value")
        x = input()
    return x


running = True
temp_dict = {}
labels = []

while running:
    print("Press and enter 'Q' to quit the programme.")
    print("To create a word in your dictionary, enter 'C'.")
    print("To read your entire dictionary, enter 'R'.")
    print("To find a word from your dictionary, ener 'F'.")
    print("To update a word from your dictionary, enter 'U'.")
    print("To delete a word from your dictionary, enter 'D'.")
    command = input().upper()
    match command:
        case "Q":
            running = False

        case "C":
            print("Enter the name of the dictionary file. If you don't have a dictionary file yet, enter the name you'd like to give it")
            file_name = input()
            file_name = while_empty(file_name)

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
                    
            add_labels = True
            temp_dict = storage.load_dict(file_name)
            crud.add_word(temp_dict, word, definition, labels)
            storage.save_dict(file_name, temp_dict)
            labels = []

        case "R":
            print("Please enter the dictionary file. If you don't have a dictionary yet, press enter, then enter in 'C'.")
            file_name = input()
            if file_name:
                print(storage.load_dict(file_name))

        case "F":
            print("Please enter the name of the dictionary file. If you don't have a dictionary yet, press enter, then enter in 'C'.")
            file_name = input()

            if file_name:
                print("Please enter the word you'd like to find")
                word = input()
                word = while_empty(word)
                
                temp_dict = storage.load_dict(file_name)
                crud.find_word(temp_dict, word)
            
        case "U":
            print("Please enter the name of the dictionary file you'd like to update")
            file_name = input()
            file_name = while_empty(file_name)

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
                
            add_labels = True
            temp_dict = storage.load_dict(file_name)
            crud.update_dict(temp_dict, word, definition, labels)
            storage.save_dict(file_name, temp_dict)
            labels = []

        case "D":
            print("Please enter the name of the dictionary file you'd like to delete")
            file_name = input()
            file_name = while_empty(file_name)

            print("Please enter the word you'd like to delete.")
            word = input()
            word = while_empty(word)

            temp_dict = storage.load_dict(file_name)
            crud.delete_word(temp_dict, word)
            storage.save_dict(file_name, temp_dict)
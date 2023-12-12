import glob
from Settings import Settings
from DataSet import DataSet
from colorClass import colorDataClass

# variables
filename = "dataset/english_words_479k.txt"
accepted_dataset = "accepted_words.txt"
rejected_dataset = "rejected_words.txt"
accepted_dataset_obj = DataSet(accepted_dataset)
rejected_dataset_obj = DataSet(rejected_dataset)
settings = "settings.txt"
settings_obj = Settings(settings)
important_files = [accepted_dataset, rejected_dataset, settings]
words = 0

# load function
def load(name):
    for file in glob.glob("*"):
        if file == name:
            print(f"{colorDataClass.CBLUE}found {name}, start loading the file{colorDataClass.CBLUE}")
            if file == settings:
                # settings_obj = Settings(name)
                if not settings_obj.load():
                    return (False, "ERR:LOAD_FILE")
            elif file == accepted_dataset:
                # accepted_dataset_obj = DataSet(name)
                if not accepted_dataset_obj.load():
                   return (False, "ERR:LOAD_FILE")
            elif file == rejected_dataset:
                # rejected_dataset_obj = DataSet(name)
                if not rejected_dataset_obj.load():
                    return (False, "ERR:LOAD_FILE")
    return (True, "ACC")

def create(name):
    if name == settings:
        # settings_obj = Settings(name)
        username = input(f"{colorDataClass.CGREEN}please write your name : {colorDataClass.CGREEN}")
        if not settings_obj.create(username):
            return (False, "ERR:CREATE_FILE")
    elif name == accepted_dataset:
        # accepted_dataset_obj = DataSet(name)
        if not accepted_dataset_obj.create():
            return (False, "ERR:CREATE_FILE")
    elif name == rejected_dataset:
        # rejected_dataset_obj = DataSet(name)
        if not rejected_dataset_obj.create():
            return (False, "ERR:CREATE_FILE")

# log_message
print(f"{colorDataClass.CBLUE}Welcome in the processing mode foe the dataset ...{colorDataClass.CBLUE}")
print(f"{colorDataClass.CBLACK}___________________________________________________{colorDataClass.CBLACK}")
print()
print()

# start loading the important files
print(f"{colorDataClass.CBLUE}start loading files ...{colorDataClass.CBLUE}")
print(f"{colorDataClass.CBLACK}___________________________________________________{colorDataClass.CBLACK}")
print()

for file in important_files:
    try:
        open(file, "r")
        result = load(file)
        if not result[0]:
            print(f"{colorDataClass.CRED}{result[1]}{colorDataClass.CRED}")
            exit()
    except FileNotFoundError:
        create(file)

print(f"{colorDataClass.CBLUE}the important file loaded successfully{colorDataClass.CBLUE}")
print(f"{colorDataClass.CBLACK}___________________________________________________{colorDataClass.CBLACK}")
print()

# start the main application
print(f"{colorDataClass.CBLUE}starting the main application{colorDataClass.CBLUE}")
print(f"{colorDataClass.CBLACK}___________________________________________________{colorDataClass.CBLACK}")
print()

#   - open the data
english_dataset = open(filename, "r+")

#   - process the data
def process(word):
    result = input(f"{colorDataClass.CGREEN}{word}{colorDataClass.CGREEN}")
#   - add data to the succeeded dataset
    if result == 'Y' or result == 'y':
        accepted_dataset_obj.addline(line=word)
        settings_obj.update()
#   - add data to the rejected dataset
    elif result == "N" or result == "n":
        rejected_dataset_obj.addline(line=word)
        settings_obj.update()
    elif result == 'exit':
        settings_obj.save()
        exit()
    else:
        print(f"{colorDataClass.CVIOLET}unrecognized order, plese write Y if the word is correct, or N if not.{colorDataClass.CVIOLET}")
        process(word)

# Alphaptic or Non
# 
# 

# reading the file
with english_dataset as file:
    if settings_obj.finished_words == settings_obj.words:
        print(f"{colorDataClass.CVIOLET}You have finished your quote, thanks for your effort ^^.{colorDataClass.CVIOLET}")
        exit()
    for line in file.readlines()[settings_obj.word_index:]:
        words = words + 1
        process(line)
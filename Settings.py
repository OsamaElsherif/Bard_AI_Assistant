import json
from dataclasses import dataclass, asdict
from colorClass import colorDataClass

@dataclass
class SettingsDataclass:
    name: str
    word_index: int
    words: int
    finished_words: int

# settings class
class Settings(SettingsDataclass):
    def __init__(self, settings_file) -> None:
        self.settings_file = settings_file
        self.word_index = 0
        self.finished_words = 0
        self.words = 79849

    def load(self) -> bool | Exception:
        try:
            self.settings = json.loads(open("settings.txt", "r+").read())
            self.name = self.settings['name']
            self.word_index = self.settings['word_index']
            self.words = self.settings['words']
            self.finished_words = self.settings['finished_words']
            print(f"{colorDataClass.CBLUE}settings file loadded successfully{colorDataClass.CBLUE}")
            print()
            print()
            print(f"{colorDataClass.CBLACK}___________________________________________________{colorDataClass.CBLACK}")
            print(f"{colorDataClass.CGREEN}Welcome, {self.name} {colorDataClass.CGREEN}")
            print(f"{colorDataClass.CGREEN}Your Quote is {self.words} {colorDataClass.CGREEN}")
            print(f"{colorDataClass.CGREEN}Your're at {self.word_index} {colorDataClass.CGREEN}")
            print(f"{colorDataClass.CGREEN}Your've finished {self.finished_words} {colorDataClass.CGREEN}")
            print(f"{colorDataClass.CBLACK}___________________________________________________{colorDataClass.CBLACK}")
            print()
        except Exception as e:
            print(f"{colorDataClass.CRED}ERR:LOAD:{e}{colorDataClass.CRED}")
            return False
        return True
    
    def set_name(self, name):
        self.name = name
        return f"{colorDataClass.CBLUE}the name set to {colorDataClass.CURL}{name}{colorDataClass.CURL} {colorDataClass.CBLUE}"
    
    def set_words(self, numberOfWords = 79849):
        self.numberOfWords = numberOfWords
        return f"{colorDataClass.CBLUE}the number of your part in words is {numberOfWords}{colorDataClass.CBLUE}"
    
    def update(self) -> bool:
        self.word_index += 1
        self.finished_words += 1
        return True


    def get_name(self):
        return self.settings['name']

    def get_words(self):
        return self.settings['finished_words']

    def get_word_index(self):
        return self.settings['word_index']

    def create(self, name) -> bool | Exception:
        try:
            self.settings_file_obj = open(self.settings_file, "w+")
            self.set_name(name)
            self.save()
            print(f"{colorDataClass.CYELLOW}settings file created successfully{colorDataClass.CYELLOW}")
        except Exception as e:
            print(f"{colorDataClass.CRED}ERR:CREATE:{e}{colorDataClass.CRED}")
            return False
        return True

    def save(self):
        self.settings_file_obj = open(self.settings_file, "w+")
        self.settings_file_obj.write(json.dumps(asdict(self)))
        self.settings_file_obj.close()
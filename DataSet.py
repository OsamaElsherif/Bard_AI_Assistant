from colorClass import colorDataClass

# dataset class
class DataSet:
    def __init__(self, filename) -> None:
        self.filename = filename

    def load(self) -> bool:
        try:
            self.file = open(self.filename, "a")
            print(f"{colorDataClass.CYELLOW}{self.filename} loaded successfully{colorDataClass.CYELLOW}")
        except Exception as e:
            print(e)
            return False
        return True

    def create(self) -> bool:
        try:
            self.file = open(self.filename, "w+")
            print(f"{colorDataClass.CYELLOW}{self.filename} created successfully{colorDataClass.CYELLOW}")
        except Exception as e:
            print(e)
            return False
        return True

    def addline(self, line) -> bool:
        r = self.file.write(f"{line}")
        return r

    def close(self) -> None:
        self.file.close()

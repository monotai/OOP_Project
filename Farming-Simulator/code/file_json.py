import json

class FileJson:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.load()

    def load(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def update(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)
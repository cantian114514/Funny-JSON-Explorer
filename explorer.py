import json
from builder import JsonBuilder

class FunnyJsonExplorer:
    def __init__(self, filepath, factory):
        self.filepath = filepath
        self.factory = factory
        self.root = None

    def _load(self):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
        builder = JsonBuilder(self.factory)
        self.root = builder.build(data)

    def show(self):
        self._load()
        if self.root:
            i = 0
            for child in self.root.children:
                if i < len(self.root.children) - 1:
                    child.draw(False, 0, "├─ ")
                else:
                    child.draw(True, 0, "├─ ")
                i += 1
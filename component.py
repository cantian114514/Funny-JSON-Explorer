from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, icon_family=None):
        self.icon_family = icon_family

    @abstractmethod
    def draw(self, level, prefix=""):
        pass

class Leaf(Component):
    def __init__(self, name, value=None, icon_family=None):
        super().__init__(icon_family)
        self.name = name
        self.value = value

    def draw(self, flag, level, prefix=""):
        icon = self.icon_family.leaf_icon if self.icon_family else ""
        if self.value:
            print(f"{prefix}{icon}{self.name}: {self.value}")
        else:
            print(f"{prefix}{icon}{self.name}")

class Container(Component):
    def __init__(self, name, level=0, icon_family=None):
        super().__init__(icon_family)
        self.name = name
        self.level = level
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def draw(self, flag, level=0, prefix=""):
        icon = self.icon_family.container_icon if self.icon_family else ""
        if flag == True:
            prefix = "└─ "

        print(f"{prefix}{icon}{self.name}")

        if self.children:
            last_child = self.children[-1]

            for child in self.children[:-1]:
                if flag == False:
                    prefix_next = "| " + "  " * (level) + "   ├─ "
                else:
                    prefix_next = "  " * (level) + "   ├─ "
                child.draw(flag, level + 1, prefix_next)

            if flag == True:
                prefix_next = "  " * level + "   └─ "
            else:
                prefix_next = "| " + "  " * (level) + "   └─ "
            last_child.draw(flag, level + 1, prefix_next)

class RectangleContainer(Container):
    def draw(self, flag, level=0, prefix=""):
        icon = self.icon_family.container_icon if self.icon_family else ""
        if level == 0 and flag == False:
            print(f"┌─ {icon}{self.name} {'─' * (41 - len(self.name))}┐")
        else:
            print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┤")

        if self.children:
            last_child = self.children[-1]

            for child in self.children[:-1]:
                prefix_next = "|   " + "|" * (level) + " ├─ "
                child.draw(False, level + 1, prefix_next)

            if flag == True:
                prefix_next = "└─" + "─" * level + "───┴─ "
            else:
                prefix_next = "|   " + "| " * (level) + "├─ "
            last_child.draw(False, level + 1, prefix_next)

class RectangleLeaf(Leaf):
    def draw(self, flag, level, prefix=""):
        icon = self.icon_family.leaf_icon if self.icon_family else ""
        if self.value:
            print(f"{prefix}{icon}{self.name}: {self.value} {'─' * (44 - len(self.name) - len(str(self.value)) - len(prefix) - 2)}┤")
        else:
            if prefix[0] == "└":
                print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┘")
            else:
                print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┤")
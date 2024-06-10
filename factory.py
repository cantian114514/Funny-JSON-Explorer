from abc import ABC, abstractmethod
from component import Container, Leaf, RectangleContainer, RectangleLeaf

class StyleFactory(ABC):
    def __init__(self, icon_family=None):
        self.icon_family = icon_family

    @abstractmethod
    def create_container(self, name, level=0):
        pass

    @abstractmethod
    def create_leaf(self, name, value=None):
        pass

class TreeStyleFactory(StyleFactory):
    def create_container(self, name, level=0):
        return Container(name, level, self.icon_family)

    def create_leaf(self, name, value=None):
        return Leaf(name, value, self.icon_family)

class RectangleStyleFactory(StyleFactory):
    def create_container(self, name, level=0):
        return RectangleContainer(name, level, self.icon_family)

    def create_leaf(self, name, value=None):
        return RectangleLeaf(name, value, self.icon_family)
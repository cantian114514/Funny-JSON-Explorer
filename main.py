from explorer import FunnyJsonExplorer
from iconFamily import poker_face_icon_family
from factory import TreeStyleFactory, RectangleStyleFactory

if __name__ == "__main__":
    filepath = 'example.json'

    # 使用树形风格
    print("Tree Style:")
    tree_factory = TreeStyleFactory(icon_family=poker_face_icon_family)
    explorer = FunnyJsonExplorer(filepath, tree_factory)
    explorer.show()

    # 使用矩形风格
    print("\nRectangle Style:")
    rectangle_factory = RectangleStyleFactory(icon_family=poker_face_icon_family)
    explorer = FunnyJsonExplorer(filepath, rectangle_factory)
    explorer.show()
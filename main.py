import argparse
from explorer import FunnyJsonExplorer
from iconFamily import IconFamily, poker_face_icon_family
from factory import TreeStyleFactory, RectangleStyleFactory

# if __name__ == "__main__":
#     filepath = 'example.json'

#     # 使用树形风格
#     print("Tree Style:")
#     tree_factory = TreeStyleFactory(icon_family=poker_face_icon_family)
#     explorer = FunnyJsonExplorer(filepath, tree_factory)
#     explorer.show()

#     # 使用矩形风格
#     print("\nRectangle Style:")
#     rectangle_factory = RectangleStyleFactory(icon_family=poker_face_icon_family)
#     explorer = FunnyJsonExplorer(filepath, rectangle_factory)
#     explorer.show()

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument('-f', '--file', type=str, required=True, help="JSON file path")
    parser.add_argument('-s', '--style', type=str, choices=['tree', 'rectangle'], required=True, help="Style: 'tree' or 'rectangle'")
    parser.add_argument('-i', '--icon', type=str, choices=['default', 'poker'], default='default', help="Icon family: 'default' or 'poker'")

    args = parser.parse_args()

    # 选择图标族
    if args.icon == 'poker':
        icon_family = IconFamily(container_icon="♢", leaf_icon="♤")
    else:
        icon_family = IconFamily(container_icon="", leaf_icon="")

    # 选择风格工厂
    if args.style == 'tree':
        factory = TreeStyleFactory(icon_family=icon_family)
    elif args.style == 'rectangle':
        factory = RectangleStyleFactory(icon_family=icon_family)

    # 创建 FunnyJsonExplorer 并展示
    explorer = FunnyJsonExplorer(args.file, factory)
    explorer.show()

if __name__ == "__main__":
    main()
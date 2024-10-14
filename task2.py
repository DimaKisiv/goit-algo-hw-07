import avlnode
import sys

def min_value(node, min = sys.maxsize):
    if (node.key < min):
         min = node.key
    if (node.left):
        left_min = min_value(node.left, min)
        if (left_min < min):
            min = left_min
    if (node.right):
        right_min = min_value(node.right, min)
        if (right_min < min):
            min = right_min
    return min


root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = avlnode.insert(root, key)

print(f"Мінімальне знчення в дереві = {min_value(root)}")

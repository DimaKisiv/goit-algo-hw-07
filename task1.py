import avlnode
import sys

def max_value(node, max = -sys.maxsize):
    if (node.key > max):
         max = node.key
    if (node.left):
        left_max = max_value(node.left, max)
        if (left_max > max):
            max = left_max
    if (node.right):
        right_max = max_value(node.right, max)
        if (right_max > max):
            max = right_max
    return max


root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = avlnode.insert(root, key)

print(f"Максимальне знчення в дереві = {max_value(root)}")

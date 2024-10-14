import avlnode

def sum_node(node):
    total_sum = node.key
    if (node.left):
        total_sum += sum_node(node.left)
    if (node.right):
        total_sum += sum_node(node.right)
    return total_sum

root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = avlnode.insert(root, key)

print(f"Сума всіх значень в дереві = {sum_node(root)}")

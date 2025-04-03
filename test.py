import random
from main import BinarySearchTree

random.seed(77)

# values = random.sample(range(1, 100), 42)

# bst = BinarySearchTree()

# for value in values:
#     bst.insert(value)

# bst.inorder_traversal()

# print()

# items = [1, 27, 51, 92, 102]

# for item in items:
#     r = bst.search(item)
#     if r is None:
#         print(f"Item {item} não encontrado")
#     else:
#         print(f"Item {r.root.data} encontrado")


def example_tree(size=42):
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    return tree

def extended_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    return tree

bst = extended_tree()
bst.inorder_traversal()



print("\n--------------------------------")

valor = 66
bst.remove(valor)
print("Após a remoção do valor", valor)
bst.inorder_traversal()
print()
print()
print("Level order traversal:")
bst.level_order_traversal()

print("\n--------------------------------\n")

minimo = bst.min()
print("O menor valor da árvore é", minimo.data)

maximo = bst.max()
print("O maior valor da árvore é", maximo.data)

print("\n--------------------------------")





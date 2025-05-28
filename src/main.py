from models.binary_tree import BinaryTree
from models.binary_search_tree import BinarySearchTree
from models.avl_tree import AVLTree
from utils.printer import print_boxed, print_divider

def menu():
    print_boxed("Menu Principal")
    print("1. Árvore Binária")
    print("2. Árvore Binária de Busca")
    print("3. Árvore AVL")
    print("4. Sair")
    return input("Escolha uma opção: ")

def handle_binary_tree():
    tree = BinaryTree()
    while True:
        print_boxed("Árvore Binária")
        print("1. Inserir valor")
        print("2. Imprimir árvore")
        print("3. Voltar")
        op = input("Escolha uma opção: ")
        
        if op == "1":
            value = int(input("Digite o valor: "))
            if tree.root is None:
                tree = BinaryTree(value)
            else:
                print("Árvore binária simples não suporta inserção!")
        elif op == "2":
            tree.print_tree()
        elif op == "3":
            break

def handle_binary_search_tree():
    tree = BinarySearchTree()
    while True:
        print_boxed("Árvore Binária de Busca")
        print("1. Inserir valor")
        print("2. Buscar valor")
        print("3. Remover valor")
        print("4. Imprimir árvore")
        print("5. Voltar")
        op = input("Escolha uma opção: ")
        
        if op == "1":
            value = int(input("Digite o valor: "))
            tree.insert(value)
        elif op == "2":
            value = int(input("Digite o valor: "))
            result = tree.search(value)
            if result:
                print("Valor encontrado!")
            else:
                print("Valor não encontrado!")
        elif op == "3":
            value = int(input("Digite o valor: "))
            tree.remove(value)
        elif op == "4":
            tree.print_tree()
        elif op == "5":
            break

def handle_avl_tree():
    tree = AVLTree()
    while True:
        print_boxed("Árvore AVL")
        print("1. Inserir valor")
        print("2. Buscar valor")
        print("3. Remover valor")
        print("4. Imprimir árvore")
        print("5. Voltar")
        op = input("Escolha uma opção: ")
        
        if op == "1":
            value = int(input("Digite o valor: "))
            tree.insert(value)
        elif op == "2":
            value = int(input("Digite o valor: "))
            result = tree.search(value)
            if result:
                print("Valor encontrado!")
            else:
                print("Valor não encontrado!")
        elif op == "3":
            value = int(input("Digite o valor: "))
            tree.remove(value)
        elif op == "4":
            tree.print_tree()
        elif op == "5":
            break

def main():
    while True:
        op = menu()
        if op == "1":
            handle_binary_tree()
        elif op == "2":
            handle_binary_search_tree()
        elif op == "3":
            handle_avl_tree()
        elif op == "4":
            print("Saindo...")
            break
        print_divider()

if __name__ == "__main__":
    main() 
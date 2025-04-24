#!/usr/bin/env python3
# test_avl_full.py

from main import AVLTree

def run_tests():
    print("=== Iniciando Testes da Árvore AVL ===")
    avl = AVLTree()

    # 1) Inserções iniciais
    valores = [15, 10, 20, 8, 12, 17, 25, 6, 11, 13]
    print("\n1. Inserindo valores:", valores)
    for v in valores:
        avl.insert(v)

    print("\n2. Travessias após inserções:")
    print("   In‑order:   ", end=""); avl.inorder_traversal();   print()
    print("   Pre‑order:  ", end=""); avl.preorder_traversal();  print()
    print("   Post‑order: ", end=""); avl.postorder_traversal(); print()
    print("   Level‑order:", end=" "); avl.level_order_traversal()

    print("\n3. Estrutura da Árvore:")
    avl.print_tree()

    # 2) Teste de duplicatas
    dup = [10, 20, 15]
    print("\n4. Tentando inserir duplicatas (10, 20, 15):")
    for v in dup:
        avl.insert(v)
    print("   Level‑order (sem mudança):", end=" "); avl.level_order_traversal()

    # 3) Remoções sequenciais
    to_remove = [
        6,   # nó folha
        8,   # nó com 1 filho (após remoção de 6)
        20,  # nó com 2 filhos
        15,  # raiz com 2 filhos
        13,  # módulo de balanceamento extra
    ]
    print("\n5. Removendo valores em sequência:", to_remove)
    for v in to_remove:
        avl.remove(v)
        print("   Level‑order:", end=" "); avl.level_order_traversal()
        print("   Estrutura:")
        avl.print_tree()

    print("\n=== Testes Concluídos ===")

if __name__ == "__main__":
    run_tests()

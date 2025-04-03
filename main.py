from queue import Queue

class Node:
    def __init__(self, data, parent=None):
        self.data = data

        # Um nó pode ter um filho à esquerda e um filho à direita
        self.left = None
        self.right = None

        self.parent = parent
        self.height = 1

    # Converter o nó para string
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None): # Inicializa a árvore com um nó raiz
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percorre a árvore em pós-ordem
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end=" ")

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=" ")
        if node.right:
            self.inorder_traversal(node.right)

    # Altura da arvore
    def height(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return 0;
        
        hleft = self.height(node.left)
        hright = self.height(node.right)

        return max(hleft, hright) + 1

    # Percorrer por nível tilizando fila
    def level_order_traversal(self, node=None):
        if node is None:
            node = self.root
        
        queue = Queue() 
        queue.put(node) # Coloca o nó raiz na fila

        # O método get() remove e retorna o item mais à esquerda da fila
        # O método put() insere um item à direita da fila 

        while not queue.empty(): # Enquanto a fila não estiver vazia
            current = queue.get() # Pega o primeiro nó da fila
            if current is None:
                continue
            print(current, end=" ") # Imprime o nó

            if current.left: # Se o nó tem um filho à esquerda
                queue.put(current.left)
            if current.right: # Se o nó tem um filho à direita
                queue.put(current.right) # Coloca o filho à direita na fila

        print()

class BinarySearchTree(BinaryTree):
    # Inserção sem balanceamento
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    # def insert(self, value):
    #     parent = None
    #     current = self.root
    #     while current:
    #         parent = current
    #         if value < current.data:
    #             current = current.left
    #         else:
    #             current = current.right
    #     if parent is None:
    #         self.root = Node(value)
    #     elif value < parent.data:
    #         parent.left = Node(value)
    #     else:
    #         parent.right = Node(value)


    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return None
        if node.data == value:
            return BinaryTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node
    
    def max(self, node=None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node
    
    def remove(self, value, node=None):
        if node is None:
            node = self.root
        
        if node is None: # Se o nó não existe
            return None

        if value < node.data: # Se o valor a ser removido é menor que o nó atual
            node.left = self.remove(value, node.left) # Remove o valor da esquerda
        elif value > node.data: # Se o valor a ser removido é maior que o nó atual
            node.right = self.remove(value, node.right) # Remove o valor da direita
        else:
            if node.left is None: # Se o nó só tem filho à direita
                return node.right # Retorna o filho à direita
            elif node.right is None: # Se o nó só tem filho à esquerda
                return node.left # Retorna o filho à esquerda
            
            else:
                # Se o nó tem dois filhos
                substitute = self.min(node.right) # Encontra o sucessor do nó
                node.data = substitute.data # Substitui o valor do nó pelo valor do sucessor
                node.right = self.remove(substitute.data, node.right) # Remove o sucessor
        return node


class AVLTree(BinarySearchTree):

    def calcHeight(self, node):
        if not node:
            return 0
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.left) - self.calcHeight(node.right)

    def updateHeight(self, node):
        node.height = 1 + max(self.calcHeight(node.left), self.calcHeight(node.right))

    def rotateRight(self, node):
        # Rotaciona para a direita

        print("Rotacionando para a direita", node.data)

        left_child = node.left # 15 
        temp = left_child.right # None  

        left_child.right = node # direita do 15 e coloquei o 20
        node.left = temp 

        self.updateHeight(node) 
        self.updateHeight(left_child)

        return left_child

    def rotateLeft(self, node):
        # Rotaciona para a esquerda

        print("Rotacionando para a esquerda", node.data)

        right_child = node.right # 15 
        temp = right_child.left

        right_child.left = node
        node.right = temp

        self.updateHeight(node)
        self.updateHeight(right_child)

        return right_child

    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _insert(self, value, node):

        if not node:
            return Node(value)

        if value < node.data:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)

        self.updateHeight(node)

        node.height = 1 + max(self.calcHeight(node.left), self.calcHeight(node.right))

        return self.settleViolation(value, node)

    def settleViolation(self, value, node):
        balance = self.calcBalance(node)

        # Primeiro caso -> left left heavy situation ou seja o nó está desbalanceado à esquerda
        if balance > 1 and value < node.left.data:
            # É um caso de esquerda esquerda
            return self.rotateRight(node) # Rotaciona para a direita

        # Segundo caso -> Se o balance é mnor que -1 ou seja o nó está desbalanceado à direita
        if balance < -1 and value > node.right.data:
            # É um caso de direita direita
            return self.rotateLeft(node) # Rotaciona para a esquerda
            
        # Terceiro caso -> left right heavy situation ou seja o nó está desbalanceado à esquerda e o filho à direita
        if balance > 1 and value > node.left.data:
            node.left = self.rotateLeft(node.left) # Rotaciona para a esquerda o filho à esquerda
            return self.rotateRight(node) # Rotaciona para a direita o nó

        # Quarto caso -> right left heavy situation ou seja o nó está desbalanceado à direita e o filho à esquerda
        if balance < -1 and value < node.right.data:
            node.right = self.rotateRight(node.right) # Rotaciona para a direita o filho à direita
            return self.rotateLeft(node) # Rotaciona para a esquerda o nó

        return node

    def remove(self, value, node=None):
        print("Removendo", value)

        if node is None:
            node = self.root

        node = self._remove(value, node)

        self.root = node

        return node

    def _remove(self, value, node):
        if not node:
            return node

        if value < node.data:
            node.left = self._remove(value, node.left)
        elif value > node.data:
            node.right = self._remove(value, node.right)
        else:
           
            if not node.left and not node.right: # Se o nó não tem filhos \ é um nó folha
                del node
                return None
            
            if not node.left: # Se o nó só tem filho à direita
                # Removendo o nó com um filho à direita
                tempNode = node.right
                del node
                return tempNode
            elif not node.right: # Se o nó só tem filho à esquerda
                # Removendo o nó com um filho à esquerda
                tempNode = node.left
                del node
                return tempNode

            # Se o nó tem dois filhos
            tempNode = self.min(node.right) # pegamos o sucessor do nó que é o menor nó da subárvore direita ou o maior nó da subárvore esquerda
            node.data = tempNode.data
            node.right = self._remove(tempNode.data, node.right)

        if node is None:
            return node
        
        self.updateHeight(node)

        balance = self.calcBalance(node)

        # Caso 1 -> left left heavy situation
        if balance > 1 and self.calcBalance(node.left) >= 0:
            return self.rotateRight(node)
        
        # Caso 2 -> left right heavy situation
        if balance > 1 and self.calcBalance(node.left) < 0: 
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        
        # Caso 3 -> right right heavy situation
        if balance < -1 and self.calcBalance(node.right) <= 0:
            return self.rotateLeft(node)
        
        # Caso 4 -> right left heavy situation  
        if balance < -1 and self.calcBalance(node.right) > 0:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        
        return node




avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)

avl.level_order_traversal() 

avl.remove(5)
avl.remove(4)

print("Raiz final:", avl.root)  # Deve exibir 15
if avl.root:
    print("Filho esquerdo da raiz:", avl.root.left)
    print("Filho direito da raiz:", avl.root.right)
    
print("Percurso level-order:")
avl.level_order_traversal()


# Tela com as visualizações da árvore: pós ordem, em ordem, nível

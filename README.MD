# Projeto de Árvores

Este projeto implementa diferentes tipos de árvores em Python:
- Árvore Binária
- Árvore Binária de Busca
- Árvore AVL

## Estrutura do Projeto

```
trees/
├── src/
│   ├── models/
│   │   ├── node.py
│   │   ├── binary_tree.py
│   │   ├── binary_search_tree.py
│   │   └── avl_tree.py
│   ├── utils/
│   │   └── printer.py
│   └── main.py
├── tests/
│   ├── test_binary_tree.py
│   ├── test_binary_search_tree.py
│   └── test_avl_tree.py
└── README.md
```

## Como Executar

1. Certifique-se de ter o Python 3.x instalado
2. Execute o arquivo principal:
   ```bash
   python src/main.py
   ```

## Como Executar os Testes

Para executar todos os testes, certifique-se de estar no diretório raiz do projeto e execute:
```bash
python -m unittest discover tests
```

Para executar um teste específico:
```bash
python -m unittest tests/test_binary_tree.py
python -m unittest tests/test_binary_search_tree.py
python -m unittest tests/test_avl_tree.py
```

Se você encontrar o erro `ModuleNotFoundError: No module named 'src'`, execute os testes a partir do diretório raiz do projeto, como mostrado acima.

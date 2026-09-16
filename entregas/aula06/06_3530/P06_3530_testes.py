import P06_3530_pilha_encadeada as PE
import P06_3530_fila_encadeada as FE
if __name__ ==  '__main__':
    print("""Testes da Pilha""")

    Pilha = PE.PilhaEncadeada()

    for i in range(5):
        Pilha.push(i)
    print("""Foi feita uma pilha adicionando os números de 0 a 4, nessa ordem.
    Representação da pilha:""")
    print(Pilha.repr())
    print()
    print("""A seguir os elementos serão retirados um por um:""")
    for i in range(len(Pilha)):
        print(Pilha.pop())

    print('\nTentando acessar os métodos topo() e pop() na pilha vazia:\n')
    try:
        print(Pilha.topo())
    except IndexError as e:
        print(e)
    try:
        print(Pilha.pop())
    except IndexError as e:
        print(e)

    print("""\nAs seguintes coisas serão feitas em sequência:
    -Adição da string 'quarenta e dois'
    -Adição do inteiro 42
    -Adição da lista [4, 2]
    -Retirada da lista
    -Adição de None
    -Adição da tupla (2, 4)
    -Verificação do topo
    -Retirada da tupla
    -Adição da lista [4, 2]
    -Adição de True
    -Adição de None
    -Retirada de None
    -Adição de None
    -Adição da lista [4, 2]
    -Print da pilha
    """)
    Pilha.push('quarenta e dois')
    Pilha.push(42)
    Pilha.push([4, 2])
    Pilha.pop()
    Pilha.push(None)
    Pilha.push((2, 4))
    Pilha.topo()
    Pilha.pop()
    Pilha.push([4, 2])
    Pilha.push(True)
    Pilha.push(None)
    Pilha.pop()
    Pilha.push(None)
    Pilha.push([4, 2])
    print(Pilha.repr())

    print()

    print("""Testes da Fila""")

    Fila = FE.FilaEncadeada()
    
    for i in range(5):
        Fila.enfileirar(i)
    print("""Foi feita uma fila adicionando os números de 0 a 4, nessa ordem.
    Representação da fila:""")
    print(Fila.repr())
    print()
    print("""A seguir os elementos serão retirados um por um:""")
    for i in range(len(Fila)):
        print(Fila.desenfileirar())

    print('\nTentando acessar os métodos frente() e desenfileirar() na fila vazia:\n')
    try:
        print(Fila.frente())
    except IndexError as e:
        print(e)
    try:
        print(Fila.desenfileirar())
    except IndexError as e:
        print(e)

    print("""\nAs seguintes coisas serão feitas em sequência:
    -Adição da string 'quarenta e dois'
    -Adição do inteiro 42
    -Adição da lista [4, 2]
    -Retirada da string
    -Adição de None
    -Adição da tupla (2, 4)
    -Verificação do topo
    -Retirada do inteiro
    -Adição da lista [4, 2]
    -Adição de True
    -Adição de None
    -Retirada da lista
    -Adição de None
    -Adição da lista [4, 2]
    -Print da fila
    """)
    Fila.enfileirar('quarenta e dois')
    Fila.enfileirar(42)
    Fila.enfileirar([4, 2])
    Fila.desenfileirar()
    Fila.enfileirar(None)
    Fila.enfileirar((2, 4))
    Fila.frente()
    Fila.desenfileirar()
    Fila.enfileirar([4, 2])
    Fila.enfileirar(True)
    Fila.enfileirar(None)
    Fila.desenfileirar()
    Fila.enfileirar(None)
    Fila.enfileirar([4, 2])
    print(Fila.repr())

    print()
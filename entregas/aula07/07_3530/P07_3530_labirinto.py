# python 3

"""
maze_builder.py
---------------
Geração procedural de labirintos perfeitos usando busca em profundidade (DFS)
com retrocesso (backtracking).

Um labirinto "perfeito" possui exactamente um caminho entre quaisquer dois
pontos — equivalente a uma árvore geradora aleatória sobre a grade m x n.

Representação interna
~~~~~~~~~~~~~~~~~~~~~
A grade lógica de m linhas X n colunas é expandida para uma matriz de
(2m+1) X (2n+1) células, onde:
  - células de coordenadas ímpares (2i+1, 2j+1) representam salas (rooms);
  - células entre duas salas adjacentes representam paredes derrubáveis;
  - as bordas externas são sempre paredes.

O queijo (cheese) é colocado aleatoriamente em qualquer sala.
"""

class Pilha:
    class Item:
        def __init__(self, x, y, dire, prox=None):
            self.Valor = (x, y)
            self.Prox = prox
            self.Dir = dire

    def __init__ (self):
        self.Head=None
        self.Lenght=0

    def add(self, item:Item):
        if self.Lenght == 0:
            self.Head = item
            self.Lenght+=1
            return()
        item.Prox = self.Head
        self.Head=item
        self.Lenght+=1
        return()

    def is_empty(self):
        if self.Lenght == 0:
            return(True)
        return(False)

    def pop(self):
        #Presumindo que a pilha não está vazia
        self.Lenght-=1
        self.Head = self.Head.Prox


import random


def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto perfeito de m X n células usando DFS com backtracking.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):
        pilha = Pilha()
        random.shuffle(directions)
        lista = [0, 1, 2, 3]
        atual = pilha.Item(x, y, lista)
        pilha.add (atual)
        while True:
            x, y = atual.Valor
            maze[2 * x + 1][2 * y + 1] = room
            
            if len(atual.Dir) !=0:
                dx, dy = directions[atual.Dir.pop(0)]
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                    maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                    random.shuffle(directions)
                    lista = [0, 1, 2, 3]
                    atual = pilha.Item(nx, ny, lista)
                    pilha.add(atual)

            else:
                Pilha.pop(pilha)
                if Pilha.is_empty(pilha):
                    break
                atual = pilha.Head


    # Inicia a DFS no canto superior-esquerdo da grade lógica
    dfs(0, 0)

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))

# Example usage:
if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    random.seed(10110)

    room = ' '
    wall = 'W'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)


def busca(maze, start:tuple, direction=None):

    def generate(maze):
        copy = []

        for i in range(len(maze)):
            copy.append([])
            for j in range(len(maze[i])):
                copy[i].append(maze[i][j])
        return(copy)
    
    if direction is None:
        maze = generate(maze)

    if maze[start[0]][start[1]] == cheese:
        return('O queijo está no ponto inicial.')
    if maze[start[0]][start[1]] == wall:
        return("As coordenadas iniciais são de uma parede, selecione uma casa válida.")

    simbolos={
        (1, 0):'v',
        (0, 1):'>',
        (0, -1):'<',
        (-1, 0):'^'
    }
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    if direction is not None:
        directions.remove((-direction[0], -direction[1]))
    for dx, dy in directions:
        nx, ny = start[0] + dx, start[1] + dy
        if maze[nx][ny] == cheese:
            maze[start[0]][start[1]] = simbolos[(dx,dy)]
            return True
        if maze[nx][ny] == room:
                if busca(maze, (nx,ny), (dx,dy)):
                    maze[start[0]][start[1]] = simbolos[(dx,dy)]
                    if start != (1,1):
                        return True
                    return(maze)
                    
if __name__ == '__main__':
    print('Labirinto gerado:\n')
    print_maze(maze)
    resolvido = busca(maze, (1,1))
    print('\nLabirinto resolvido:\n')
    print_maze(resolvido)
from P06_3530_pilha_encadeada import *

class FilaEncadeada:

    def __init__ (self):
        """
        A fila é feita com duas pilhas, uma de entrada (A) e uma de saída (B)
        """
        self.Pilha_A = PilhaEncadeada()
        self.Pilha_B = PilhaEncadeada()

    def enfileirar(self, valor):
        """
        Insere-se um novo objeto no topo da pilha A. Se já havia um antes,
        o novo objeto passa a guardar também a localização do que estava
        no topo antes.
        Complexidade: O(1)
        """
        self.Pilha_A.push(valor)


    def desenfileirar(self):
        """
        Se a fila estiver vazia, retorna IndexError. 
        Se houver um único elemnto na pilha A e nenhum na pilha B,
        o topo da pilha A é retirado com as funções de pilha e seu valor é
        retornado.
        Se houver mais elementos em A, e B estiver vazia, um a um os objetos
        são removidos de A e acrescentados em B, ambas as ações por
        métodos de pilha, e então o objeto no topo de B é removido e seu 
        valor é retornado.
        Se já houver elementos em B, o objeto no topo é removido por métodos de
        pilha e então retornado.
        Complexidade: O(n) (O(1) amortizado, com explicação em '06_3530_respostas.md')
        """
        if len(self) == 0:
            """Retorna a soma dos valores dos objetos que guarda.
            Complexidade: O(1)"""
            raise IndexError("IndexError: A fila está vazia")
        
        if len(self.Pilha_A) == 1 and len(self.Pilha_B) == 0:
            return(self.Pilha_A.pop())
        
        if len(self.Pilha_A) not in [0,1] and len(self.Pilha_B) == 0:
            for __ in range (len(self.Pilha_A)):
                self.Pilha_B.push(self.Pilha_A.pop())
            return(self.Pilha_B.pop())
        
    
        return(self.Pilha_B.pop())



    def frente (self):
        """
        Se a fila estiver vazia, retorna IndexError. 
        Se houver um único elemnto na pilha A e nenhum na pilha B,
        o topo da pilha A tem seu valor retornado.
        Se houver mais elementos em A, e B estiver vazia, um a um os objetos
        são removidos de A e acrescentados em B, ambas as ações por
        métodos de pilha, e então o valor do objeto no topo de B é 
        retornado.
        Se já houver elementos em B, o objeto no topo tem seu valor retornado.
        Complexidade: O(n) (O(1) amortizado, com explicação em '06_3530_respostas.md')
        """

        if len(self) == 0:
            raise IndexError("IndexError: A fila está vazia")
        
        if len(self.Pilha_A) == 1 and len(self.Pilha_B) == 0:
            return(self.Pilha_A.Head.Valor)
        
        if len(self.Pilha_A) not in [0,1] and len(self.Pilha_B) == 0:
            for __ in range (len(self.Pilha_A)):
                self.Pilha_B.push(self.Pilha_A.pop())
            return(self.Pilha_B.Head.Valor)
        
        return(self.Pilha_B.Head.Valor)

    def esta_vazia(self):
        """Se ambas as pilhas estiverem vazias, retorna True.
        Do contrário, retorna False.
        Complexidade: O(1)
        """
        return (len(self) == 0)

    def repr (self):
        """Cria uma string com a representação da pilha.
        O valor do objeto no topo é inserido no início da string,
        e as setas têm o significado de "o valor do próximo objeto é"
        Para isso, duas string são criadas:
        Se houver elementos na pilha B, eles são percorridos um a um e,
        para cada, a string recebe ela mesma mais '<x> -->', onde x
        é o valor do objeto atual (se for o último objeto e A estiver
        vazia, a seta é omitida).
        Em seguida, se houver elementos na pilha A, eles são percorrido um a um,
        e segunda string recebe '--> <x>' mais ela mesma, onde x é o valor do
        objeto atual, criando assim uma 'string invertida'.
        no fim, ambas as strings são concatenadas, e o resultado é retornado.
        Complexidade: O(n)
        """
        if self.esta_vazia():
            raise IndexError("IndexError: A fila está vazia.")
        string = ''
        substring = ''
        atual = self.Pilha_B.Head
        for _ in range (len(self.Pilha_B)):
            if atual.Next is not None:
                string += f'{atual.Valor} --> '
                atual = atual.Next

            else:
                if len(self.Pilha_A) == 0:
                    string += f'{atual.Valor}'
                else:
                    string += f'{atual.Valor} --> '
        
        atual = self.Pilha_A.Head
        if len(self.Pilha_A) != 0:
            for _ in range (len(self.Pilha_A)):
                if atual.Next is not None:
                    substring = f' --> {atual.Valor}' + substring
                    atual = atual.Next
                else:
                    string += f'{atual.Valor}'

        string += substring

        return(string)

    def __len__(self):
        """Retorna a soma do tamanho das duas pilhas..
        Complexidade: O(1)"""
        return(len(self.Pilha_A) + len(self.Pilha_B))

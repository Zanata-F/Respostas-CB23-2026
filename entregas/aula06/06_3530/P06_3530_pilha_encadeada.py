class PilhaEncadeada:
    class _No:
        def __init__(self, valor, next=None):
            self.Valor = valor
            self.Next = next

    def __init__(self):
        self.Head = None
        self.Lenght = 0

    def push(self, item):
        """O objeto que guarda o tamnho da pilha recebe ele mesmo mais 1.
        Então, insere-se um novo objeto no topo da pilha. Se já havia um antes,
        o novo objeto passa a guardar também a localização do que estava
        no topo antes.
        Complexidade: O(1)
        """
        self.Lenght += 1
        if self.Head is None:
            self.Head= self._No(item)
        else:
            novo_item = self._No(item, self.Head)
            self.Head = novo_item

    def pop (self):
        """O objeto que guarda o tamanho da pilha recebe ele mesmo menos 1.
        Então, retira-se o objeto que estiver no topo, colocando o objeto para o qual
        ele aponta em seu lugar. O valor do objeto removido é então retornado.
        Se não houver objetos, retorna IndexError.
        Complexidade: O(1)"""
        if self.Lenght == 0:
            raise IndexError("IndexError: A pilha está vazia")
        else:
            retirado = self.Head
            self.Head = retirado.Next
            self.Lenght -=1
            return(retirado.Valor)
        
    def topo(self):
        """Retorna o valor do objeto no topo.
        Se não houver objetos, retorna IndexError.
        Complexidade: O(1)"""
        if self.Lenght == 0:
            raise IndexError("IndexError: A pilha está vazia")
        else:
            return(self.Head.Valor)

    def esta_vazia(self):
        """Se o objeto que guarda o tamanho da pilha for igual à zero, retorna True.
        Do contrário, retorna False.
        Complexidade: O(1)
        """
        if self.Lenght == 0:
            return(True)
        return(False)

    def __len__ (self):
        """Retorna o valor do objeto que está guardando o tamanho da pilha.
        Complexidade: O(1)"""
        return(self.Lenght)

    def __iter__ (self):
        atual = self.Head
        for _ in range (self.Lenght):
            yield(atual)
            atual = atual.Next

    def repr(self):
        """Cria uma string com a representação da pilha.
        O valor do objeto no topo é inserido no início da string,
        e as setas têm o significado de "o valor do próximo objeto é"
        Para isso, a partir de uma string vazia inicial, cada elemento da pilha
        é percorrido e, a cada um, a string recebe ela mesma mais '--> <x>', 
        onde x é o valor do objeto.
        Complexidade: O(n)
        """
        string = ''
        for item in self:
            if string == '':
                string = (item.Valor)
            else:
                string = (f"{string} --> {item.Valor}")
        return(string)
    


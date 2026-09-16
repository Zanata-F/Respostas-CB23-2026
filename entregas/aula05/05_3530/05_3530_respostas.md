Questão 1:

    Classes base:
        Pessoa
        
            Subclasses de Pessoa:
                Funcionário
                    (herda nome, idade)

                    Funções de Funcionário

                        Garçom
                        Chefe de cozinha
                        Gerente
        
        Restaurante
            Subclasses de Restaurante:

                Funcionário

                Pizzaria
                    (herda Iguaria(comida), nome, endereço e telefone)

                
        Iguaria(comida)
            Subclasses de Iguaria(comida)
                Pizza
                Bolo
                (herdam nome e preço)

Questão 2:
    Eu adicionaria a classe Iguaria como uma classe separada de restaurante, e adicionaria na classe restaurante um dicionário que associasse o nome da comida ao item da classe iguaria.

Questão 3:
    Argumento 1: dois argumentos, um da classe pessoa (quem fez o pedido) e outro da classe iguaria (o que foi pedido)
    Argumento 2: um argumento da classe Iguaria (o pedido que está sendo preparado)
    Argumento 3: um argumento da classe funcionário (quem está sendo demitido)
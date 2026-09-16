O algoritmo de busca em profundidade foi utilizado devido a ser mais simples de implementar em Python
a partir de uma função recursiva.
A implementação de um algoritmo de busca em largura exigiria uma fila que constantemente criaria a necessidade de
rastrear os pais dos nós e os nós já visitados.

Adicionalmente, como o algoritmo é feito de modo que exista sempre um único caminho possível, ambos os algoritmos
devolveriam o mesmo caminho.

Por fim, o algoritmo de busca em largura tem complexidade de espaço O(w), onde w é a largura da árvore que
representa o labirinto, e o algoritmo de busca em profundidade tem complexidade O(d), onde d é a profundidade da árvore. Dado que cada bifurcação representa a criação de ao menos duas folhas, a tendência é ter w>d. Além disso, como a posição do queijo é aleatória, a complexidade de tempo em ambos os algoritmos em ambos os casos é O(C), onde C é o número de casas do labirinto. Isto é, nenhum dos algoritmos representa uma mudança muito grande na eficiência de tempo, mas o algoritmo de busca em profundidade exige espaço menor na memória, sendo o mais recomendado para labirintos muito grandes e. Para labirintos menores, por não haver uma distinção muito grande, o método mais recomendado é uma questão de preferência pessoal.


class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)


class ArvoreBinaria:
    def __init__(self, raiz):
        self._raiz = raiz
        self._aux = 0
        self._aux1 = 0
        self._aux2 = 0

    def insere(self, raiz, nodo):
        """Insere um nodo em uma árvore binária de pesquisa."""
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            self._raiz = nodo

        # Nodo deve ser inserido na subárvore direita.
        elif raiz.chave < nodo.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                self.insere(raiz.direita, nodo)

        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                self.insere(raiz.esquerda, nodo)

    def em_ordem(self, nodo=None):
        if (self._aux == 0):
            nodo = self._raiz
            self._aux += 1

        if not nodo:
            return

        # Visita filho da esquerda.
        self.em_ordem(nodo.esquerda)

        # Visita nodo corrente.
        print(nodo.chave),

        # Visita filho da direita.
        self.em_ordem(nodo.direita)

    def pre_ordem(self, nodo=None):
        if (self._aux1 == 0):
            nodo = self._raiz
            self._aux1 += 1

        if not nodo:
            return

        # Visita nodo corrente.
        print(nodo.chave)

        # Visita filho da esquerda.
        self.pre_ordem(nodo.esquerda)

        # Visita filho da direita.
        self.pre_ordem(nodo.direita)

    def pos_ordem(self, nodo=None):
        if (self._aux2 == 0):
            nodo = self._raiz
            self._aux2 += 1

        if not nodo:
            return

        # Visita filho da esquerda.
        self.pos_ordem(nodo.esquerda)

        # Visita filho da direita.
        self.pos_ordem(nodo.direita)

        # Visita nodo corrente.
        print(nodo.chave)


if __name__ == '__main__':
    arvore_binaria_pesquisa = ArvoreBinaria(NodoArvore(40))
    arvore_binaria_pesquisa.insere(None, NodoArvore(20))
    arvore_binaria_pesquisa.insere(None, NodoArvore(60))
    arvore_binaria_pesquisa.insere(None, NodoArvore(50))
    arvore_binaria_pesquisa.insere(None, NodoArvore(70))
    arvore_binaria_pesquisa.insere(None, NodoArvore(10))
    arvore_binaria_pesquisa.insere(None, NodoArvore(30))

    # raiz = NodoArvore(40)
    #
    # raiz.esquerda = NodoArvore(20)
    # raiz.direita = NodoArvore(60)
    #
    # raiz.direita.esquerda = NodoArvore(50)
    # raiz.direita.direita = NodoArvore(70)
    # raiz.esquerda.esquerda = NodoArvore(10)
    # raiz.esquerda.direita = NodoArvore(30)

    arvore_binaria_pesquisa.em_ordem()
    print("======================")
    arvore_binaria_pesquisa.pre_ordem()
    print("======================")
    arvore_binaria_pesquisa.pos_ordem()
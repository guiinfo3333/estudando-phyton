

from abc import ABC, abstractmethod


class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Método de inserção de informação na árvore"""
        pass

    @abstractmethod
    def empty(self):
        """Método que retorna True, caso a árvore esteja vazia, False caso contrário"""
        pass

    @abstractmethod
    def root(self):
        """Método que retorna o nó raiz da árvore. Se a árvore estiver vazia, None deve ser retornado"""
        pass


class Node:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def empty(self):
        return not self._data

    def __str__(self):
        return self._data.__str__()


class BinaryTree(TreeADT):

    def __init__(self, data=None):
        self._root = Node(data)
        self._aux = 0
        self._aux1 = 0
        self._aux2 = 0
        self._aux3 = 0
        self._lista_em_ordem = []
        self._lista_pre_ordem = []
        self._lista_pos_ordem = []

    def insert(self, raiz, value):

        if not isinstance(value._data, int):
            raise NameError("Permitido apenas números inteiros")
            return

        if self._aux == 0:
            raiz = self._root
            self._aux += 1

        # Nodo deve ser inserido na raiz.
        if raiz._data is None:
            self._root = value

        elif raiz._data < value._data:
            if raiz._right is None:
                raiz._right = value
            else:
                self.insert(raiz._right, value)

        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if raiz._left is None:
                raiz._left = value
            else:
                self.insert(raiz._left, value)
        self._aux = 0

    def empty(self):
        pass

    def root(self):
        pass

    def em_ordem(self, raiz):
        if self._aux1 == 0:
            raiz = self._root
            self._aux1 += 1

        if not raiz:
            return

        # Visita filho da esquerda.
        self.em_ordem(raiz._left)

        # Visita nodo corrente.
        print(raiz._data)
        # print(raiz._data),

        # Visita filho da direita.
        self.em_ordem(raiz._right)

    def pre_ordem(self, raiz):
        if self._aux2 == 0:
            raiz = self._root
            self._aux2 += 1

        if not raiz:
            return

        self._lista_pre_ordem.append(raiz._data)
        print(raiz._data)

        # Visita filho da esquerda.
        self.pre_ordem(raiz._left)

        # Visita filho da direita.
        self.pre_ordem(raiz._right)

    def pos_ordem(self, raiz):
        if self._aux3 == 0:
            raiz = self._root
            self._aux3 += 1

        if not raiz:
            return
        # Visita filho da esquerda.
        self.pos_ordem(raiz._left)

        # Visita filho da direita.
        self.pos_ordem(raiz._right)

        print(raiz._data)
        # Visita nodo corrente.
        self._lista_pos_ordem.append(raiz._data)


    def traversal(self, in_order=True, pre_order=False, post_order=False):
        if in_order:
            self.em_ordem(None)
            self._lista_pre_ordem = []
            self._lista_pos_ordem = []

        if pre_order:
            self.pre_ordem(None)
            self._lista_em_ordem = []
            self._lista_pos_ordem = []

        if post_order:
            self.pos_ordem(None)
            self._lista_em_ordem = []
            self._lista_pre_ordem = []

        print("**************Lista em ordem ****************")
        print(self._lista_em_ordem)
        print("**************Lista em pre-ordem ****************")
        print(self._lista_pre_ordem)
        print("**************Lista em pos-ordem ****************")
        print(self._lista_pos_ordem)


class Programa():

    def menu(self):
        print("Escolha uma das opções abaixo:")
        print("1 - Fala ai mermão, deseja inserir na árvore binária ?")
        print("2 - Deseja exibir a árvore binária em ordem ?")
        print("3 - Deseja exibir a árvore binária em pré-ordem ?")
        print("4 - Deseja exibir a árvore binária em pós-orden ?")
        opcao_menu = input()
        return int(opcao_menu)

if __name__ == '__main__':
    arvore_binaria = BinaryTree(None)
    arvore_binaria.insert(None, Node(20))
    arvore_binaria.insert(None, Node(60))
    arvore_binaria.insert(None, Node(50))
    arvore_binaria.insert(None, Node(70))
    arvore_binaria.insert(None, Node(10))
    arvore_binaria.insert(None, Node(30))
    arvore_binaria.insert(None, Node(110))
    arvore_binaria.insert(None, Node(55))
    arvore_binaria.insert(None, Node(2))
    arvore_binaria.insert(None, Node(1))

    arvore_binaria.pos_ordem(None)
    # arvore_binaria.traversal(True, True, True)


    #
    # while (True == True):
    #     valor = programa.menu()
    #     if valor == 1:
    #         numero = input("Ok digite um valor inteiro, por favor !")
    #         arvore_binaria.insert(None, Node(int(numero)))
    #         print("Valor cadastrado com sucesso na árvore binária !")
    #     elif valor == 2:
    #         arvore_binaria.traversal(True, False, False)
    #     elif valor == 3:
    #         arvore_binaria.traversal(False, True, False)
    #     elif valor == 4:
    #         arvore_binaria.traversal(False, False, True)



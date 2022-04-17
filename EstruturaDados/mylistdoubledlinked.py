
from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """Insere <elemento> na posiÃ§Ã£o <indice>"""
        pass

    @abstractmethod
    def append(self, elemento):
        """Insere um elemento na última posicao"""
        pass

    @abstractmethod
    def remove(self, elemento):
        """Remove primeira ocorrÃªncia de <elemento>"""
        pass

    @abstractmethod
    def removeAll(self, elemento):
        """Remove primeira ocorrÃªncia de <elemento>"""
        pass

    @abstractmethod
    def count(self, elemento):
        """Conta a quantidade de <elemento> na lista"""
        pass

    @abstractmethod
    def clear(self):
        """Apaga a lista"""
        pass

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro Ã­ndice de <elemento>"""
        pass

    @abstractmethod
    def length(self):
        """Retorna o tamanho da lista"""
        pass

    @abstractmethod
    def removeAll(self, elemento):
        """Apaga todas as ocorrencias daquele elemento na lista"""
        pass

    @abstractmethod
    def replace(self, indice, elemento):
        """substitui na posição <index> o valor existente com <elemento>."""
        pass

    @abstractmethod
    def removeAt(self, index):
        """Remove o elemento que se encontra na posicao <index> da lista"""
        pass

class DoublyLinkedListMylist(ListADT):

    class _DoublyNode:

        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

        def __str__(self):
            if self._elem is not None:
                return str(self._elem) + ' '
            else:
                return '|'

    def __init__(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def insert(self, index, elem):
        if index >= self._length:   # se o indice se inserÃ§Ã£o passado for maior que a lista
            index = self._length    # atualiza para o Ãºltimo indice
        if not self.ifNotExists(elem):
            if self.empty():  # Caso da lista vazia
                new_node = self._DoublyNode(elem, self._header, self._trailer)
                self._header._next = new_node
                self._trailer._prev = new_node
            elif index == 0:  # caso da inserÃ§Ã£o na primeira posiÃ§Ã£o da lista
                new_node = self._DoublyNode(elem, self._header, self._header._next)
                self._header._next._prev = new_node
                self._header._next = new_node
            else:  # outros casos de inserÃ§Ã£   // neste tipo de insercao eu so vou alterar o proximo do meu anterior e o anterior do proximo
                this = self._header._next
                successor = this._next
                pos = 0
                while pos < index - 1:  # caminhando dentro da lista encadeada
                    this = successor
                    successor = this._next
                    pos += 1
                new_node = self._DoublyNode(elem, this, successor)
                this._next = new_node
                successor._prev = new_node

            self._length += 1
        else:
            raise NameError("O elemento '"+str(elem)+"' já existe na lista!")



    def append(self, elemento):
        if not self.ifNotExists(elemento):
            self.insert(self._length + 1, elemento)
        else:
            raise NameError("O elemento '" + str(elemento) + "' já existe na lista!")


    def remove(self, elemento):
        pass

    def removeAt(self, index):
        if (self._length == 0):
            raise NameError("A lista está vazia !")
            return
        result = None  # armazena a primeira posiÃ§Ã£o do elemento
        pos = 0
        aux = self._header._next
        successor = aux._next
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if pos == index:
                aux._prev._next = successor
                successor._prev = aux._prev
                self._length -= 1
                return
            aux = aux._next
            successor = aux._next
            pos += 1
        raise NameError("index não encontrado !")

    def removeAll(self, elemento):
        this = self._header._next
        successor = this._next
        tamanho = ((self._length+1) - 1)
        pos = 0
        index = 0

        while pos < tamanho:  # caminhando dentro da lista encadeada
            if this._elem == elemento:
                this._prev._next = successor
                successor._prev =  this._prev
                self._length -= 1
            pos += 1
            this = successor
            successor = this._next
            index += 1
        print(index)


    def count(self, elem):
        result = 0
        this = self._header._next
        if self._length > 0:
            while this._next is not None:   # aqui a lista Ã© percorrida
                if this._elem == elem:
                    result += 1
                this = this._next
        return result

    def replace(self, indice, elemento):
        if (self._length == 0):
            raise NameError("A lista está vazia !")
            return
        result = None  # armazena a primeira posiÃ§Ã£o do elemento
        pos = 0
        aux = self._header._next
        successor = aux._next
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if pos == indice:
                aux._prev._elem = elemento
                successor._prev._elem = elemento
                return
            aux = aux._next
            successor = aux._next
            pos += 1
        raise NameError("index não encontrado !")

    def clear(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def index(self, elem):
        result = None   # armazena a primeira posiÃ§Ã£o do elemento
        pos = 0
        aux = self._header._next
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if aux._elem is elem:
                result = pos
            aux = aux._next
            pos += 1
        return result  # se o elemento nÃ£o estiver na lista, retorna None

    def length(self):
        return self._length

    def ifNotExists(self, elem):
        pos = 0
        aux = self._header._next
        # Vamos percorrer a lista em busca de elem
        while pos < self._length:
            if aux._elem == elem:
                return True
            aux = aux._next
            pos += 1
        return False

    def empty(self):
        return self._length == 0

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._header
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'



if __name__ == '__main__':
    '''ll = LinkedList()
    ll.insert(0, 0)
    ll.insert(1, 1)
    ll.insert(1, 2)
    ll.insert(20, 3)
    ll.insert(0, 4)
    print(ll)
    ll.remove(4)
    print(ll)
    ll.remove(1)
    print(ll)'''

    lista = DoublyLinkedListMylist()
    lista.insert(0, 0)
    lista.insert(0, 1)
    lista.append(1)

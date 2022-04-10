from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """Insere <elemento> na posiÃ§Ã£o <indice>"""
        pass

    @abstractmethod
    def remove(self, elemento):
        """Remove primeira ocorrÃªncia de <elemento>"""
        pass

    @abstractmethod
    def append(self, elemento):
        """Insere um elemento na última posicao"""
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

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro Ã­ndice de <elemento>"""
        pass

    @abstractmethod
    def length(self):
        """Retorna o tamanho da lista"""
        pass


class Node(object):

    def __init__(self, element=None, next_element=None):
        self._element = element
        self._next = next_element

    def __str__(self):
        if not self._next:
            return '|' + self._element.__str__() + '|'
        else:
            return '|' + self._element.__str__()


class LinkedList(ListADT):

    def __init__(self, elem=None):
        if elem:
            self._head = Node(elem)     # AtenÃ§Ã£o ao manipular esta referÃªncia
            self._tail = self._head     # Facilita a inserÃ§Ã£o no fim da lista
            self._length = 1
        else:
            self._head = None   # AtenÃ§Ã£o ao manipular esta referÃªncia
            self._tail = None   # Facilita a inserÃ§Ã£o no fim da lista
            self._length = 0

    def insert(self, index, elem):
        # a inserÃ§Ã£o pode acontecer em trÃªs locais: inÃ­cio, meio e fim da lista
        # separei em mÃ©todos diferentes (privados) para facilitar o entendimento e a legibilidade
        n = Node(elem)  # nÃ³ a ser inserido na lista
        if index == 0:  # primeiro local de inserÃ§Ã£o Ã© no comeÃ§o da lista
            self.__insert_at_beginning(n)
        elif index >= self._length: # segundo local de inserÃ§Ãµa Ã© no fim da lista
            self.__insert_at_end(n)  # se o Ã­ndice passado foi maior que o tamanho da lista, insiro no fim
        else:  # por fim, a inserÃ§Ã£o no meio da lista
           self.__insert_in_between(index, n)
        self._length += 1  # apÃ³s inserido, o tamanho da lista Ã© modificado

    def append(self, elem):
        n = Node(elem)
        self.__insert_at_end(n)

    def __insert_at_beginning(self, n):
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:  # se houver elemento na lista
            n._next = self._head  # o head atual passa a ser o segundo elemento
            self._head = n  # e o novo nÃ³ criado passa a ser o novo head

    def __insert_at_end(self, n):
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:
            self._tail._next = n  # o Ãºltimo elemento da lista aponta para o nÃ³ criado
            self._tail = n  # o nÃ³ criado passa a ser o Ãºltimo elemento

    def __empty_list_insertion(self, node):
        # na inserÃ§Ãµa na lista vazia, head e tail apontam para o nÃ³
        self._head = node
        self._tail = node

    def __insert_in_between(self, index, n):  # 3
        pos = 0  # a partir daqui vamos localizar a posiÃ§Ã£o de inserÃ§Ã£o
        aux = self._head  # variÃ¡vel auxiliar para nos ajudar na configuraÃ§Ã£o da posiÃ§Ã£o do novo nÃ³
        while pos < index - 1:  # precorre a lista atÃ© a posiÃ§Ã£o imediatamente anterior
            aux = aux._next  # Ã  posiÃ§Ã£o onde o elemento serÃ¡ inserido
            pos += 1
        n._next = aux._next  # quando a posiÃ§Ã£o correta tiver sido alcanÃ§ada, insere o nÃ³
        aux._next = n

    def remove(self, elem):
        if not self.empty():  # SÃ³ pode remover se a lista nÃ£o estiver vazia, nÃ£o Ã©?!
            aux = self._head
            if aux._element == elem:  # Caso especial: elemento a ser removido estÃ¡ no head
                self._head = aux._next  # head passa a ser o segundo elemento da lista
            else:
                removed = False  # Flag que marca quando a remoÃ§Ã£o foi feita
                while aux._next and not removed:  # verifico se estamos no fim da lista e nÃ£o foi removido elemento
                    prev = aux
                    aux = aux._next  # passo para o prÃ³ximo elemento
                    if aux._element == elem:  # se for o elemento desejado, removo da lista
                        prev._next = aux._next
                        removed = True  # marco que foi removido
            self._length -= 1

    def removeAt(self, indexelemento):
        result = self.element(indexelemento)
        if (result != None):
            self.remove(result)
        else:
            raise NameError("index não existe na lista")

    def replace(self, indice, elemento):
        result = self.replaceChange(indice, elemento)


    def removeAll(self, elem):
        if not self.empty():  # SÃ³ pode remover se a lista nÃ£o estiver vazia, nÃ£o Ã©?!
            aux = self._head
            if aux._element == elem:  # Caso especial: elemento a ser removido estÃ¡ no head
                self._head = aux._next  # head passa a ser o segundo elemento da lista
                self._length -= 1

            aux = self._head

            while aux._next:  # verifico se estamos no fim da lista e nÃ£o foi removido elemento
                prev = aux
                aux = aux._next
                if aux._element == elem:  # se for o elemento desejado, removo da lista
                    prev._next = aux._next
                    self._length -= 1
                    aux = prev

    def count(self, elem):
        counter = 0
        if not self.empty():  # Verifica se a lista nÃ£o estÃ¡ vazia (sÃ³ faz sentido contar em lists nÃ£o vazias!)
            aux = self._head  # Se a lista nÃ£o estiver vazia, percorre a lista contando as ocorrÃªncias
            if aux._element is elem:
                counter += 1
            while aux._next:  # precorrendo a lista....
                aux = aux._next
                if aux._element is elem:
                    counter += 1
        return counter

    def clear(self):
        self._head = None  # todos os nÃ³s que compunham a lista serÃ£o removidos da memÃ³ria pelo coletor de lixo
        self._tail = None
        self._length = 0

    def index(self, elem):
        result = None
        pos = 0
        aux = self._head
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if aux._element is elem:
                result = pos
            aux = aux._next
            pos += 1
        return result  # se o elemento nÃ£o estiver na lista, retorna None

    def replaceChange(self, index, elementonovo):
        result = None
        pos = 0
        aux = self._head

        while not result and pos < self._length:
            if pos is index:
                aux._element = elementonovo
            aux = aux._next
            pos += 1

    def element(self, index):
        result = None
        pos = 0
        aux = self._head
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:
            if pos is index:
                result = aux._element
                return result
            aux = aux._next
            pos += 1
        return result

    def length(self):
        return self._length

    def empty(self):
        return not self._head

    def __len__(self):
        return self._length

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._head
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(0, 0)
    ll.insert(1, 1)
    ll.insert(1, 2)
    ll.insert(2, 3)
    ll.insert(20, 3)
    ll.insert(0, 4)
    ll.insert(3, 4)
    ll.insert(4, 4)
    ll.append(20000)
    ll.append(101010101)
    print(ll)
    ll.replace(7,10000)  resolver problema que so vai ate o 7
    print(ll)
    print(len(ll))
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
    def replace(self, indice, elemento):
        """substitui na posição <index> o valor existente com <elemento>."""
        pass

    @abstractmethod
    def remove(self, elemento):
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
    def removeAll(self, elemento):
        """Apaga todas as ocorrencias daquele elemento na lista"""
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


class MyList(ListADT):

    def __init__(self):
        self._data = list()  # repositÃ³rio/local onde as informaÃ§Ãµes serÃ£o armazenadas
        self._length = 0  # variÃ¡vel que armazena o tamanho da lista

    def insert(self, indice, elemento):
        self._data.insert(indice, elemento)
        self._length = self._length + 1

    def append(self, elemento):
        self._data.append(elemento)
        self._length = self._length + 1

    def replace(self, indice, elemento):
        if (len(self._data) == 0):
            raise NameError("A lista está vazia !")
            return
        try:
            self._data[indice] = elemento
        except IndexError:
            raise NameError("index não existe na lista")
            return
        except TypeError:
            raise NameError("índice deve ser inteiro e não string")
            return

    def remove(self, elemento):
        self._data.remove(elemento)
        self._length -= 1

    def removeAll(self, elemento):
        contador = 0
        while (contador < len(self._data)):
            if (self._data[contador] == elemento):
                self.remove(elemento)
                self._length -= 1
            contador += 1

    def removeAt(self, index):
        if (len(self._data) == 0):
            raise NameError("A lista está vazia !")
            return
        try:
            if (self._data[index] in self._data):
                self._data.pop(index)
                self._length -= 1
        except IndexError:
            raise NameError("index não existe na lista")
            return
        except TypeError:
            raise NameError("índice deve ser inteiro e não string")
            return

    def count(self, elemento):
        return self._data.count(elemento)

    def clear(self):
        self._data = list()
        self._length = 0

    def index(self, elemento):
        return self._data.index(elemento)

    def length(self):
        return self._length

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return self._data.__str__()

    def __iter__(self):
        return self._data.__iter__()


if __name__ == '__main__':
    lista = MyList()
    lista.insert(0, 1)
    lista.insert(1, 'teste')
    lista.insert(2, 1)
    lista.insert(3, 'teste')
    lista.append('alomeudeus')
    lista.replace(0, "troquei ehhe")
    print(lista)

    lista.removeAll('teste')
    # lista.removeAt(1 )
    print(lista)

    lista.insert(1, 1)
    lista.insert(2, 1)
    lista.insert(4, 1)
    print(lista.count(1))

    lista.insert(0, 30)
    print(lista)

    print(lista.index(30))

    print("quantidadade ", len(lista))

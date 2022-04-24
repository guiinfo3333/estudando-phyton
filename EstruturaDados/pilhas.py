from abc import ABC, abstractmethod


class EmptyStack(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Stack(ABC):

    @abstractmethod
    def push(self, elem):
        """Empilha <elemento>"""
        pass

    @abstractmethod
    def pop(self):
        """Desempilha elemento da pilha"""
        pass

    @abstractmethod
    def top(self):
        """Verifica qual Ã© o elemento que se encontra no topo da pilha, sem removÃª-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a pilha estÃ¡ vazia"""
        pass


class ArrayStack(Stack):
    """ImplementaÃ§Ã£o de pilha que utiliza uma lista Python para armazenar as informaÃ§Ãµes"""

    def __init__(self):
        """Pilha vazia"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)  # o topo da pilha Ã© a Ãºltima posiÃ§Ã£o da lista interna

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
       Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        return self._data.pop()


if __name__ == '__main__':
    pilha = ArrayStack()

    pilha.push(5)
    pilha.push(3)
    print(pilha)
    print(len(pilha))
    print(pilha.is_empty())
    try:
        pilha.pop()
        print(pilha.top())
        print(pilha)
        pilha.pop()
        print(pilha)
        pilha.pop()
    except EmptyStack:
        print("pilha vazia: nÃ£o pode retirar elemento!")
    else:
        print("ExecuÃ§Ã£o sem erros")
    finally:
        print("fim!")


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


class Parser:
    __tokens = [
        "class", "Parser", ":", "def", "__init__", "(", "self", "program", ")", "_program", "="
    ]
    __keywords = [
        "class", "Parser", ":", "def", "__init__", "(", "self", "program", ")", "_program", "="
    ]

    __tokensespeciais_geral = ["(", "[", "{", ")", "]", "}"]
    __tokensespeciais_abrindo = ["(", "[", "{"]
    __tokensespeciais_fechando = [")", "]", "}"]

    def __init__(self, program):
        self._program = program.split()
        self._tokens_programa = program.split()
        self._tokens_especiais_do_programa = []

    @property
    def retornaTokensGerais(self):
        return self._tokens_programa

    def retornaTokenEspecial(self):
        return self._tokens_especiais_do_programa

    def __str__(self):
        return self._tokens_especiais_do_programa.__str__()

    def __str__(self):
        return self._tokens_especiais_do_programa.__str__()

    def tokenizer(self):
        lista_de_token = []
        lista_de_token_especiais = []
        for result in self._program:
            if result in self.__tokens:
                lista_de_token.append(result)
            if result in self.__tokensespeciais_geral:
                lista_de_token_especiais.append(result)

        self._tokens_programa = lista_de_token
        self._tokens_especiais_do_programa = lista_de_token_especiais
        return lista_de_token

    def scan(self):
        """Este método deve percorrer todos os tokens do programa para identificar
        se o programa está bem formado"""
        pass

    def parse(self):
        """Este método deve retornar True, se o programa estiver bem formado, False,
        caso contrário"""
        pass


if __name__ == '__main__':
    string = "class class class ( ] ( ]"
    parser = Parser(string)
    print(parser.tokenizer())
    print("Tokens especiais do meu programa :")
    print(list(parser.retornaTokenEspecial()))


# Deve imprimir True
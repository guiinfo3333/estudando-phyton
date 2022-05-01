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
    __reserved_words = [
        'False', 'class', 'from', 'or', 'None', 'continue', 'global', 'pass', 'True', 'def', 'if',
        'raise', 'and', 'del', 'import', 'return', 'as', 'elif', 'while', 'async', 'in', 'except', ' try',
        'assert', 'else', 'is', 'lambda', 'with', 'await',
        'finally', 'nonlocal', 'yield', 'break', 'for', 'not'
    ]

    __tokensespeciais_geral = ["(", "[", "{", ")", "]", "}"]
    __tokensespeciais_abrindo = ["(", "[", "{"]
    __tokensespeciais_fechando = [")", "]", "}"]

    def __init__(self, program):
        self._program = program.split()
        self._programatodo = []
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
            if (result[::-1] in self.__reserved_words) or (result in self.__tokensespeciais_geral):
                self._programatodo.append(result)
            else:
                raise NameError("palavra ! '" + str(result) + "' não pode ser colocada no programa")
            if result in self.__tokens:
                lista_de_token.append(result)
            if result in self.__tokensespeciais_geral:
                lista_de_token_especiais.append(result)

        self._tokens_programa = lista_de_token
        self._tokens_especiais_do_programa = lista_de_token_especiais
        return lista_de_token

    def scan(self):
        error = False
        contador = 0
        tokens_especiais = self._tokens_especiais_do_programa
        tamanho_token_especiais = len(tokens_especiais)

        if not (tamanho_token_especiais % 2 == 0):
            raise NameError("Quantidade ímpar de tokens especiais !")
        else:
            while (contador < (tamanho_token_especiais / 2)):
                if (tokens_especiais[contador] == "("):
                    if not (tokens_especiais[(tamanho_token_especiais - 1) - contador] == ")"):
                        error = True
                elif (tokens_especiais[contador] == "["):
                    if not (tokens_especiais[(tamanho_token_especiais - 1) - contador] == "]"):
                        error = True
                elif (tokens_especiais[contador] == "{"):
                    if not (tokens_especiais[(tamanho_token_especiais - 1) - contador] == "}"):
                        error = True
                contador = contador + 1
        if error:
            raise NameError("Elementos não estão fechando corretamente ")


if __name__ == '__main__':
    string = "ssalc ssalc [  ( ) ]"
    parser = Parser(string)
    print(parser.tokenizer())
    print("Tokens especiais do meu programa :")
    print(list(parser.retornaTokenEspecial()))
    parser.scan()


# Deve imprimir True

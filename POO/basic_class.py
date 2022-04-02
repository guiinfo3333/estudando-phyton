from abc import ABC #abstract base class

from collections.abc import MutableSequence
from numbers import Complex

class Numero(Complex):
    def __getitem__(self, item):
        super.__getitem()

filmes = Numero()
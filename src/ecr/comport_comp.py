from abc import abstractmethod
from ecr.comportamento import Comportamento

# Comportamento composto é um comportamento composto de varios comportamentos
class ComportComp(Comportamento):
    def __init__(self, comportamentos):
        pass 

    # Deve retornar a accao a ser activada
    def activar(self, percepcao):
        pass

    # Define o comportamento de seleção de uma acção das disponiveis
    @abstractmethod
    def seleccionar_accao(self, accoes):
        pass
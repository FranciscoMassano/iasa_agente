from abc import ABC, abstractmethod

# Interface que define o comportamento dos objectos reaccao e ComportComp
class Comportamento(ABC):
    # Comportamento relaciona padrões de perceção com padrões de ação, pode ter várias reações
    # Podem haver comportamentos compostos, um comportamento composto por comportamentos
    @abstractmethod
    def activar(self, percepcao):
        pass
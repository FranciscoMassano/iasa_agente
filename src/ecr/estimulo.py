from abc import ABC, abstractmethod

# Interface que define os diversos estimulos de acordo com o tipo de percepcao
class Estimulo(ABC):
    
    # metodo abstacto que indica o estimulo consoante a percepçao realizada
    # retorna um float que representa a intensidade de acordo com a percepcao realizada
    @abstractmethod
    def detectar(self, percepcao):
        pass
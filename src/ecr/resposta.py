# Define uma resposta a estímulos, em termos de acção a realizar e da respectiva prioridade
# A Accao esta definida no package SAE providenciado no inicio do projeto
class Resposta:

    #constructor define os elementos de uma resposta
    def __init__(self, accao):
        pass

    # Todas as accoes tem uma prioridade
    # Retorna uma accao 
    def activar(self, percepcao, intensidade = 0.0):
        pass
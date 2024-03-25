import os
import sys
sys.path.append('C:\\Users\\Francisco\\Desktop\\iasa_agente\\src') 


from ecr.comportamento import Comportamento

class Explorar(Comportamento):

    # Esta classe Explorar e um tipo de comportamento
    # Escolhe uma direcao aleatoriamete das disponiveis
    # A partir dessa direcao obtem uma resposta (com RespostaMover)
    # Esta resposta e ativada, disto resulta a accao a ser devolvida
    def ativar(self, percepcao):
        pass
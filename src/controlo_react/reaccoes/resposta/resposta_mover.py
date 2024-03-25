
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from ecr.resposta import Resposta
from sae.agente.accao import Accao






class RespostaMover(Resposta):

    # Chama-se o constructor da classe resposta
    # A direcao e proviniente da direcao escolhida no comportamento
    def __init__(self, direcao):
        super().__init__(Accao(direcao))
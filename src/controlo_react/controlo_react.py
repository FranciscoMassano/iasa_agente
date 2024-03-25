
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.sae.agente.controlo import Controlo


class ControloReact(Controlo):
    def __init__(self, comportamento):
        pass
    
    #Devolve a accao definida pelo comportamento
    #A accao e obtida atraves da activavao de um comportamento
    def processar(self, percepcao):
        pass
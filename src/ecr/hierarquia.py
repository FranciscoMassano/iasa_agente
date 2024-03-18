import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.ecr.comport_comp import ComportComp

# Define uma hierarquia de comportamentos
class Hierarquia(ComportComp):

    # Das accoes disponiveis, retorna a primeira
    def seleccionar_accao(self, accoes):
        pass
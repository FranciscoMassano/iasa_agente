import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.ecr.comport_comp import ComportComp

# Este classe filtra as accoes por prioridade
class Prioridade(ComportComp):
    # De todas as accoes, deve devolver a com maior prioridade
    def seleccionar_accao(self, accoes):
        pass
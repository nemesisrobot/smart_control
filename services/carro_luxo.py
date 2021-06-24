#Autor:Diego Silva
#Data:24/06/2021
#Descrição:classe para carro de luxo
from sys import path
path.append('/services')

from services.carros import *

class CarroLuxo(Carros):

    def potencia_carro(self):
        return '400 a 900 cavalos'

    def valor_aluguel_carro(self):
        return 5000



#Autor:Diego Silva
#Data:24/06/2021
#Descrição:classe para carro de popular
from sys import path
path.append('/services')

from services.carros import *

class CarroPopular(Carros):

    def potencia_carro(self):
        return '100 a 200 cavalos'

    def valor_aluguel_carro(self):
        return 1000

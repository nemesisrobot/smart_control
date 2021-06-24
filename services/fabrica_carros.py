#Autor:Diego Silva
#Data:24/06/2021
#Descrição:Classe para pegar atributos de cada tipo de carro

from services.carro_luxo import *
from services.carro_popular import *

class Fabrica():

    def aluga(self, tipo):
        if tipo == 1:
            return CarroLuxo()

        if tipo == 2 :
            return CarroPopular()

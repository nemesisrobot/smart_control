#Author:Diego Silva
#Date: 24/06/2021
#Description:classe abstrata para carros

import abc

class Carros(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def potencia_carro(self):
        pass

    @abc.abstractmethod
    def valor_aluguel_carro(self):
        pass
from random import randint
from cocinero import Cocinero

cocineros = [
    Cocinero('Juan', 5),
    Cocinero('Marcela', 8),
    Cocinero('Martin', 9),
]

class Restaurante:
    def __init__(self, nombre, reputacion = 0):
        self.nombre = nombre
        self.reputacion = reputacion

    def aceptar_pedido(self, pedido):
        self.pedido = pedido
        self.cuenta = 0
        for item in self.pedido:
            self.cuenta += item['precio']
        return self.cuenta        

    def cobrar_pedido(self,dinero, cuenta):
        if dinero > cuenta:
            self.preparar_pedido()
            return dinero - cuenta
        else:
            return "Dinero insuficiente"

    def preparar_pedido(self):
        self.cocinero = self.asignar_cocinero()


    def asignar_cocinero(self):
        cocinero = cocineros[randint(0,2)]
        return cocinero

    

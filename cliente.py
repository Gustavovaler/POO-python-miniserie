
from menu import menu


class Cliente:
    def __init__(self, nombre, distancia, dinero = 1000):
        self.nombre = nombre
        self.distancia = distancia
        self.dinero = dinero

    def elegir_menu(self):
        pass

    def enviar_pedido(self):
        pass

    def recibir_pedido(self):
        pass
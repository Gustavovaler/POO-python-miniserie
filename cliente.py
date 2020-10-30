from random import randint
from menu import menu
from restaurante import Restaurante

class Cliente:
    def __init__(self, nombre, distancia, dinero = 1000):
        self.nombre = nombre
        self.distancia = distancia
        self.dinero = dinero

    def elegir_menu(self):
        comida = menu['comidas'][randint(0,3)]
        bebida = menu['bebidas'][randint(0,3)]
        postre = menu['postres'][randint(0,3)]
        pedido = [comida, bebida, postre]
        restaurante = Restaurante('Pippo')
        restaurante.aceptar_pedido(pedido)

    def enviar_pedido(self):
        pass

    def recibir_pedido(self):
        pass


cliente = Cliente('Gustavo', 0)
cliente.elegir_menu()
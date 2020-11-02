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
        self.pedido = [comida, bebida, postre]
        print(f"El pedido del cliente es: {comida['nombre']}, {bebida['nombre']},{postre['nombre']}")
        self.enviar_pedido()
        
    def enviar_pedido(self):
        self.restaurante = Restaurante('Pippo')
        cuenta = self.restaurante.aceptar_pedido(self.pedido)
        print(f'El total del pedido es $ {cuenta}')
        self.cambio = self.restaurante.cobrar_pedido(self.dinero, cuenta)
        if self.cambio == "Dinero insuficiente":
            print("No se pudo realizar la compra por falta de dinero")
        else:
            print(f"Compra pagada, me sobró {self.cambio} pesos")
            self.recibir_pedido(self.restaurante.preparar_pedido())


    def recibir_pedido(self, entrega):
        if entrega == 300:
            print('La calidad del restaurante es excelente')
        elif entrega < 300 and entrega >= 150:
            print('La calidad del restaurante es regular')
        else:
            print('La calidad del restaurante es mala')

cliente = Cliente('Gustavo', 0)
cliente.elegir_menu()
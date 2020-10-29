

class Restaurante:

    def __init__(self, nombre, pedido = None):
        self.nombre = nombre
        self.pedido = pedido
        self.reputacion = 0
        self.cocineros = []


    def __str__(self):
        return f'Restaurante: {self.nombre} /  Reputación: {self.reputacion}'

    def recibir_pedido(self):
        pass

    def pedir_pago(self):
        pass

    def asignar_cocinero(self):
        pass

    def enviar_pedido(self):
        pass



restaurante = Restaurante('La Farola')

print(restaurante)


class Restaurante:
    def __init__(self, nombre, reputacion = 0):
        self.nombre = nombre
        self.reputacion = reputacion
        self.cocineros = []


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
        pass


    def asignar_cocinero(self):
        pass

    

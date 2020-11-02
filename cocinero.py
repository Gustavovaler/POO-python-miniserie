

class Cocinero:
    def __init__(self, nombre, experiencia, energia = 100):
        self.nombre = nombre
        self.experiencia = experiencia
        self.energia = energia

    def cocinar(self, pedido):
        self.entrega = self.experiencia * self.energia / len(pedido) 
        return self.entrega
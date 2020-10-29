from menu import menu

class Cliente:
    def __init__(self, nombre, distancia = 3, dinero = 1000):
        self.nombre = nombre
        self.distancia = distancia
        self.dinero = dinero

    def __str__(self):
        return f'Cliente: {self.nombre} / Experiencia: {self.distancia} / Dinero: {self.dinero}'


    def elegir_menu(self):
        pass


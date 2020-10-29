

class Cocinero:
    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia

    def __str__(self):
        return f'Cocinero: {self.nombre} / Experiencia: {self.experiencia}'

    

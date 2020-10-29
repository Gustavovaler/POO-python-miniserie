
# definición de la clase Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Nombre: {self.nombre} y es del tipo Persona'


#esta es la instanciación de la clase Persona

persona = Persona('Gustavo')

print(persona)




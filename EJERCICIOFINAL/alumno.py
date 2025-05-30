class Alumno:
    def __init__(self, apellidos, nombre):
        self.apellidos = apellidos
        self.nombre = nombre
        

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

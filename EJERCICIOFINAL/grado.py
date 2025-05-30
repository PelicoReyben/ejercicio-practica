class Grado:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.alumnos = []
        

    def inscribir_alumno(self, alumno):
        if len(self.alumnos) < 3:
            self.alumnos.append(alumno)
            return True
        return False
    
    def mostrar_Alumno(self):
        return self.alumnos
    
# main.py

from grado import Grado
from alumno import Alumno

grados = {}

def agregar_grado():
    codigo = input("Ingrese código de grado: ")
    nombre = input("Ingrese nombre del grado: ")
    grados[codigo] = Grado(codigo, nombre)
    print("........................se agregó el grado exitosamente")

def inscribir_alumno():
    apellidos = input("Ingrese Apellidos: ")
    nombre = input("Ingrese Nombre: ")
    alumno = Alumno(apellidos, nombre)

    print("................Seleccione el grado en el que inscribirá al alumno")
    for grado in grados.values():
        print(f"{grado.codigo} {grado.nombre}")

    codigo_grado = input("Ingrese el código del grado: ")
    if codigo_grado in grados:
        if grados[codigo_grado].inscribir_alumno(alumno):
            print("...................Alumno inscrito exitosamente")
        else:
            print("No se puede inscribir más alumnos en este grado.")
    else:
        print("Grado no encontrado.")

def ver_alumnos_por_grado():
    for grado in grados.values():
        print(f"{grado.codigo} {grado.nombre}")
        print("--------------------------------------------------------------")
        for alumno in grado.mostrar_alumnos():
            print(alumno)
        print("--------------------------------------------------------------")

def main():
    while True:
        print("\n1. Agregar Grado")
        print("2. Inscribir Alumno")
        print("3. Ver Alumnos por Grado")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_grado()
        elif opcion == '2':
            inscribir_alumno()
        elif opcion == '3':
            ver_alumnos_por_grado()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

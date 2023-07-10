import tkinter as tk

class Aplicacion:
    def _init_(self):
        self.alumnos = []
        self.notas = []

    def cargar_alumnos(self):
        alumno = input("Ingrese el nombre del alumno: ")
        nota = float(input("Ingrese la nota del alumno: "))
        self.alumnos.append(alumno)
        self.notas.append(nota)
        print("Alumno cargado correctamente.")

    def listar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos cargados.")
        else:
            for i in range(len(self.alumnos)):
                print(f"Alumno: {self.alumnos[i]} - Nota: {self.notas[i]}")

    def mostrar_alumnos_aprobados(self):
        if not self.alumnos:
            print("No hay alumnos cargados.")
        else:
            print("Alumnos con notas mayores o iguales a 7:")
            for i in range(len(self.alumnos)):
                if self.notas[i] >= 7:
                    print(f"Alumno: {self.alumnos[i]} - Nota: {self.notas[i]}")

    def mostrar_menu(self):
        while True:
            print("\n--- Menú ---")
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Mostrar alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.cargar_alumnos()
            elif opcion == "2":
                self.listar_alumnos()
            elif opcion == "3":
                self.mostrar_alumnos_aprobados()
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Intente nuevamente.")


aplicacion1 = Aplicacion()
aplicacion1.mostrar_menu()
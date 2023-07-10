import tkinter as tk

class AdminAlumnos:
    def _init_(self):
        self.alumnos = []
        self.notas = []

    def cargar_alumnos(self):
        nombre = input("Ingrese el nombre del alumno: ")
        nota = float(input("Ingrese la nota del alumno: "))
        self.alumnos.append(nombre)
        self.notas.append(nota)
        print("Alumno cargado exitosamente.")

    def listar_alumnos(self):
        for i in range(len(self.alumnos)):
            print(f"Nombre: {self.alumnos[i]}, Nota: {self.notas[i]}")

    def mostrar_notas_mayores_o_iguales_a_7(self):
        for i in range(len(self.alumnos)):
            if self.notas[i] >= 7:
                print(f"Nombre: {self.alumnos[i]}, Nota: {self.notas[i]}")

if _name_ == "_main_":
    admin = AdminAlumnos()

    def cargar_alumnos():
        admin.cargar_alumnos()
        entry_nombre.delete(0, tk.END)
        entry_nota.delete(0, tk.END)

    def listar_alumnos():
        admin.listar_alumnos()

    def mostrar_notas_mayores_o_iguales_a_7():
        admin.mostrar_notas_mayores_o_iguales_a_7()

    root = tk.Tk()
    root.title("Administrar Alumnos")

    # Crear los widgets de la interfaz
    label_nombre = tk.Label(root, text="Nombre:")
    label_nombre.pack()

    entry_nombre = tk.Entry(root)
    entry_nombre.pack()

    label_nota = tk.Label(root, text="Nota:")
    label_nota.pack()

    entry_nota = tk.Entry(root)
    entry_nota.pack()

    button_cargar = tk.Button(root, text="Cargar Alumno", command=cargar_alumnos)
    button_cargar.pack()

    button_listar = tk.Button(root, text="Listar Alumnos", command=listar_alumnos)
    button_listar.pack()

    button_notas_mayores = tk.Button(root, text="Mostrar Notas >= 7", command=mostrar_notas_mayores_o_iguales_a_7)
    button_notas_mayores.pack()

    root.mainloop()
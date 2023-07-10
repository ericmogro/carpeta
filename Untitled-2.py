class Persona ():
    
    def __int__(self):
        self.nombre = input("ingrese el nombre: ")
        self.edad = int(input("ingrese edad: "))
    def imprimir (self):
        print("el nombre es: ", self.nombre)
        print("la edad es: ",self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("ingrese el sueldo: "))
    def imprimir(self):
        super().__init__()
        print(" El sueldo es: ",self.sueldo)
    def impuesto (self):
        if self.sueldo > 3000000:
            print("paga impuesto")
        else: 
            print("no paga impuesto")

persona = Empleado()
persona.imprimir()
persona.impuesto()
                



    

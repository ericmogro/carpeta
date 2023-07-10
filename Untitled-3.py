class Agenda():

    def __init__ (self):
        self.nombre =[]
        self.telefono = []
        self.mail= []
    def carga (self):
        for x in range (1):
            nombre = input ("ingrese nombre: ")
            self.nombre.append(nombre)
            telefono = int(input("ingrese el telefono: "))
            self.telefono.append(telefono)
            mail = int(input("ingrese el mail: "))
            self.mail.append(mail)
    def listado (self):
        



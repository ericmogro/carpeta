import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Ingrese usuario y contraseña")

        self.label1=tk.Label(self.ventana1,text="usuario: ")
        self.label1.grid(column=0,row=0)
        self.label2=tk.Label(self.ventana1,text="clave: ")
        self.label2.grid(column=0,row=1)

        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1,width=20,textvariable=self.dato1)
        self.entry1.grid(columm=1,row=0)

        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1,width=20,textvariable=self.dato2)
        self.entry2.grid(columm=1,row=1)

        self.botton=tk.Button(self.ventana1,text="ingresar",command=self.ingresar)
        self.botton.grid(column=1,row=2)
        
        self.ventana1.mainloop()

        def ingresar (self):
            if self.dato1.get() == "juan" and self.dato2.get() == "abc123":
                self.ventana1.title (" correcto")
            else:
                self.ventana1.title ("incorrecto")

aplicacion1 = Aplicacion()



            
            



        




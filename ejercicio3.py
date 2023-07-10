import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1,width=20,textvariable=self.dato1)
        self.entry1.grid(columm=1,row=0)
        
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1,width=20,textvariable=self.dato2)
        self.entry2.grid(columm=1,row=1)

        self.botton=tk.Button(self.ventana1,text="ingresar",command=self.ingresar)
        self.botton.grid(column=1,row=3)

        self.label=tk.Label(self.ventana1,text="la suma es: ")
        self.label.grid(column=1,row=4)

        self.ventana1.mainloop()

    def suma1 (self):
        self.valor1=int(self.dato1.get())
        self.valor2=int(self.dato2.get())
        self.suma=self.valor1+self.valor2
        self.label.configure(text=self=suma)
            
aplicacion=Aplicacion()


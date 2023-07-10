import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("ingresar numero")

        self.label1=tk.Label(self.ventana1,text="numero 1")
        self.label1.grid(column=0,row=0)
        self.label2=tk.Label(self.ventana1,text="numero 2")
        self.label2.grid(column=0,row=1)

        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1,width=30,textvariable=self.dato1)
        self.entry1.grid(columm=1,row=0)
        
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1,width=30,textvariable=self.dato2)
        self.entry2.grid(columm=1,row=1)

        self.botton1=tk.Button(self.ventana1,text="+",command=self.suma)
        self.botton1.grid(column=1,row=2)
        self.botton2=tk.Button(self.ventana1,text="-",command=self.resta)
        self.botton2.grid(column=1,row=3)
        self.botton3=tk.Button(self.ventana1,text="*",command=self.multiplicar)
        self.botton3.grid(column=1,row=4)
        self.botton4=tk.Button(self.ventana1,text="/",command=self.dividir)
        self.botton4.grid(column=1,row=5)

        
        self.label3=tk.Label(self.ventana1,text=" resultado ")
        self.label3.grid(column=1,row=6)
        self.label4=tk.Label(self.ventana1,text=" ")
        self.label4.grid(column=1,row=6)

        self.ventana1.mainloop()

    def suma (self):
        self.valor1=int(self.dato1.get())
        self.valor2=int(self.dato2.get())
        self.sum=self.valor1+self.valor2
        self.label1.configure(text=self.suma)
        
    def resta(self):
        self.valor1=int(self.dato1.get())
        self.valor2=int(self.dato2.get())
        self.rest=self.valor1-self.valor2
        self.label2.configure(text=self.resta)
        
    def multiplicar(self):
        self.valor1=int(self.dato1.get())
        self.valor2=int(self.dato2.get())
        self.multi=self.valor1*self.valor2
        self.label3.configure(text=self.multiplicar)
        
    def dividir(self):
        self.valor1=int(self.dato1.get())
        self.valor2=int(self.dato2.get())
        self.div=self.valor1/self.valor2
        self.label4.configure(text=self.dividir)

aplicacion1=Aplicacion()
        

        


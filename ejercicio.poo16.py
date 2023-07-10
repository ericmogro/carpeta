import tkinter as tk

class Aplicacion():
    def __init__(self):

        self.ventana1=tk.Tk() 
        self.ventana1.geometry("400x400")

        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=0,row=1)

        self.label1=tk.Label(self.ventana1,text="monto plazo fijo")
        self.label1.grid(column=0,row=0)

        self.label2=tk.Label(self.ventana1,text="interes mensual 8%")
        self.label2.grid(column=0,row=2)

        self.label3=tk.Label(self.ventana1,text="monto a cobrar (monto inicial + interes): ")
        self.label3.grid(column=0, row=3)

        self.label4=tk.Label(self.ventana1,text="-------------")
        self.label4.grid(column=0,row=4)

        self.seleccion=tk.IntVar()
        self.seleccion.set(0)

        self.radio1=tk.Radiobutton(self.ventana1, text="30 dias",variable=self.seleccion,value=1)
        self.radio1.grid(column=1,row=0 )
        self.radio2=tk.Radiobutton(self.ventana1, text="60 dias",variable=self.seleccion,value=1)
        self.radio2.grid(column=1,row=1)
        self.radio3=tk.Radiobutton(self.ventana1, text="90 dias",variable=self.seleccion,value=1)
        self.radio3.grid(column=1,row=2 )

        self.boton1=tk.Button(self.ventana1,text="calcular plazo", command=self.calcular)
        self.boton1.grid(column=1,row=3)
    
    def calcular(self):
        if self.seleccion.get()==1:
            self.valor1=int(self.dato.get())
            self.resultado=(8*self.valor1)/100
            self.label5.configure(text=self.resultado)
        
        if self.seleccion.get()==2:
            self.valor1=int(self.dato.get())
            self.resultado=((8*self.valor1)/100)*2
            self.label5.configure(text=self.resultado)
        
        if self.seleccion.get()==3:
            self.valor1=int(self.dato.get())
            self.resultado=((8*self.valor1)/100)*3
            self.label5.configure(text=self.resultado)

aplicacion1 = Aplicacion()
            
            
            
        
    
    




      


    
        

        
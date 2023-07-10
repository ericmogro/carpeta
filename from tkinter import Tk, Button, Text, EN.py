from tkinter import Tk, Button, Text, END, re

class Aplicacion:

    def _init_(self):
        self.ventana1=Tk()
        
        self.pantalla=Text(self.ventana1,state="disabled", width=40, height=3,
                            background="gray99", foreground="black", font=("helvetica", 15))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.operacion=""
        boton1=self.crearBoton(u"\232B",escribir=False )
        boton2=self.crearBoton("%")
        boton3=self.crearBoton(u"\u00F7" , bg="orange")
        boton4=self.crearBoton(7)
        boton5=self.crearBoton(8)
        boton6=self.crearBoton(9)
        boton7=self.crearBoton("*", bg="orange" )
        boton8=self.crearBoton(4)
        boton9=self.crearBoton(5)
        boton10=self.crearBoton(6)
        boton11=self.crearBoton("-", bg="orange")
        boton12=self.crearBoton(1)
        boton13=self.crearBoton(2)
        boton14=self.crearBoton(3)
        boton15=self.crearBoton("+", bg="orange")
        boton16=self.crearBoton(0,)
        boton17=self.crearBoton(".")
        boton18=self.crearBoton("=",  bg="orange")

        botones=[boton1, boton2, boton3, boton4, boton5, boton6, 
                 boton7, boton8, boton9, boton10, boton11, boton12, 
                 boton13, boton14, boton15, boton16, boton17, boton18]
        
        contador=0
        for fila in range(1, 5):
            for columna in range (4):
                botones[contador].grid(row=fila, column=columna)
                contador=contador+1
        botones[17].grid(row=5, column=0, columnspan=4)

                

    def crearBoton(self, valor, bg="orange" ,escribir=True, ancho=9, alto=1):
            return Button(self.ventana1, text=valor, width=ancho, 
                          height=alto, font=("Helvetica", 15), 
                          command=lambda:self.click(valor, escribir))
            
    def click(self, texto, escribir):
        if not escribir:
                if texto == "=" and self.operacion!="":
                        self.operacion=re.sub(u"\u00F7","/", self.operacion)
                        resultado = str(eval(self.operacion))
                        self.operacion = ""
                        self.limpiarpantala()
                        self.mostrarpantalla(resultado)
                elif texto == u"\232B":
                      self.operacion = ""
                      self.limpiarpantala()
        else: 
              self.operacion+=str(texto)
              self.mostrarpantalla(texto)

    def mostrarpantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
        return

    def limpiarpantala(self):        
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        return

    
aplicacion=Aplicacion()
aplicacion.ventana1.mainloop()
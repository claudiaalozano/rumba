from tkinter import *
root = Tk()
root.geometry("600x600")
def MenuPrincipal():

    tittle_text= Label(root, text="Prueba Interface", font=("Arial", 20))
    tittle_text.config(font=17)
    tittle_text.pack(pady=2)

    main_text = Label(root, text = "Por favor introduzca el numero de zonas")
    main_text.pack(pady=80)
    main_text.config(font=15)

    s = Spinbox(root, from_=0, to_=100000, increment=1)
    s.pack(pady=10)
    s.config()

    buttom = Button(root, text="Aceptar", command=lambda: calculos(s.get()))
    buttom.pack(pady=10)

def calculos(n):
    n= int(n)
    root.destroy()

    if n == 0:
        return 0

    new=Tk()
    new.geometry("600x600")
    zonas=[]

    for i in range(n):
        string= "Zona " + str(i)
        text= Label(new, text=string)
        text.pack(pady=2)

        #Largo de la habitación
        largo=Label(new, text="Largo en cm")
        largo.pack()
        l=Text(new, width=30, height=1)
        l.pack()

        
        #Ancho de la habitación
        ancho=Label(new, text="Ancho en cm")
        ancho.pack()
        a= Text(new, width=30, height=1)
        a.pack()

        zonas.append((l,a))

    buttom= Button(new, text="Obteniendo resultados", command=lambda: showFinal(zonas,new))
    buttom.pack(pady=15)


def showFinal(zonas, ventana):
    velocidad=3

    if not check(zonas):
        t= Label(ventana, text="Los valores introducidos no son válidos.")
        t.config(font=25)
        t.pack(pady=40)
        t.after(2000,t.destroy)

        return 0

    superficie = 0

    for zona in zonas:
        superficie = superficie + float(zona[0].get("1.0", END)) * float(zona[1].get("1.0", END))
    
    tiempo= superficie/velocidad
    final =Tk()
    final.geometry("600x600")
    t=Label(final, text="Tiempo estimado de la roomba")
    t.config(font=20)
    t.pack(pady=30)
    z=Label(final,text=("Tiempo: " + str(tiempo) + " segundos" ))
    z.pack()


def check(zonas):
    for zona in zonas:
        try:
            float(zona[0].get("1.0" , END))
            float(zona[1].get("1.0" , END))
        except:
            return False
    return True


MenuPrincipal()

root.mainloop()

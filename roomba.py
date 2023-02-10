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
        string= "Zona" + str(i)
        text= Label(new, text=string)
        text.pack(pady=2)

        #Largo de la habitación
        largo=Label(new, text="Largo en cm")
        l=Text(next, width=30, height=1)
        l.pack()

        
        #Ancho de la habitación
        ancho=Label(new, text="Ancho en cm")
        ancho.pack()
        a= Text(new, width=30, height=1)
        a.pack()

        zonas.append((l,a))

    buttom= Button(new, )
MenuPrincipal()
root.mainloop()

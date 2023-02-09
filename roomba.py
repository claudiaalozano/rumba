from tkinter import *
def MenuPrincipal():
    root = Tk()
    root.geometry("600x600")

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

MenuPrincipal()
root.mainloop()

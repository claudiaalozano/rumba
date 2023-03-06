# rumba

<h1 align="center">Roomba</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/claudiaalozano/rumba.git)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea vamos a realizar dos ejercicios:


+El primero cosiste en desarrolla una interfaz, para ello usaremos tanto Gtk como tinker (encontramos una explicación paso a paso para crearla).

  -[Con Gtk](#id1)
  
  -[Con Tinker](#id2)
      
+El segundo en desarrolar un roomba, que nos calule el tiempo estimado que tardará en limpiar una superficie determinada. En este ejericio ponemos en prátia lo de la interfaz gráfica; puesto que se le pedira al usuario una serie de datos para calcular el tiempo estimado.

  -[Rommba](#id3)

***
## Integrantes:
1. [Alba](https://github.com/albabernal03) 
2. [Claudia](https://github.com/claudiaalozano)

***

<h2>Guía de creacion de una interfaz gráfica:</h2>

Una interfaz gráfica es un medio visual a través del cual es usuario puede interatuar y realizar tareas graficamente.

**CREAR INTERFAZ USANDO LA LIBRERIA GTK**<a name="id1"></a>

La biblioteca GTK se usa para desarrollar el entorno gráfico GNOME, así como sus aplicaciones, a la vez que algunos otros entornos gráficos. La biblioteca GTK permite el desarrollo sencillo de interfaces gráficas y su uso conjunto con Python permite el desarrollo rápido de aplicaciones gráficas potentes.

**Pasos:**

**1.** En el principio, tenemos que importar el módulo Gtk para poder acceder a las clases y funciones GTK + . Dado que el sistema de un usuario puede tener varias versiones de GTK + instaladas al mismo, queremos asegurarnos de que cuando importamos GTK que se refiere a GTK + 3 y no cualquier otra versión de la biblioteca, que es el propósito de la declaración. Asimismo creamos una ventana vacía.

```
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()

```

**2.** Ahora establecemos que al clicar en X se cierre la ventana y mostramos esta ventana.

```
win.connect("delete-event", Gtk.main_quit)
win.show_all()

```

**3.** Por último, se comienza el bucle de procesamiento + GTK que deja de funcionar cuando la ventana se cierra.

```
Gtk.main()

```


**4.** Añadimos un título a la ventana y un botón.

```
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Titulo :)")

        self.button = Gtk.Button(label="boton")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("hola mundo")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

```



---------------------------------------------------------------------------------------------------------------------------------------------------------------

**CREAR INTERFAZ USANDO TINKER**<a name="id2"></a>

**Pasos:**

**1.** En primer lugar, lo primero que neesitamos es importar el módulo Tinker y crear una ventana, esto es la raíz, para la cual usaremos la función Tk(), será el contenedor de nuestra aplicación, aquí iran todos los widgets.

A la raíz siempre se le añade un buble infinito , ya que una vez abrimos la aplicación siempre debe estar esperando órdenes.

```
from tinker import *

#Creamos la raíz
Ventana= Tk()

#Bucle de aplicación, es como un while True
Ventana.mainloop()

```
**2.** A continuación le añadimos un título a nuestra ventana principal con el método title() e impondremos que su tamaño no sea modificable su tamaño con el método resizable(0,0); si pusieramos resizable(1,1) podríamos agrandar la ventana con el ratón en ambos en ambos ejes.

Especificamos su tamaño con el método geometry() y el color de fondo con el método config().

```
from tinker import *

#Creamos la raíz
Ventana=Tk()
Ventana.resizable(0,0) #Impedimos redimensionar la ventana
Ventana.geometry('250x300') #Tamaño por defecto
Ventana.config(bg='white') #Fondo
Ventana.title('Aplicación') #Título

#Bucle de aplicación
Ventana.mainloop()

```
 **3.** Ahora utilizamos la etiqueta label que nos permite crear texto estático. Para ello crear un Label pasando como argumentos la raíz(ventana) y el texto a mostrar, luego la incluimos en nuestra ventana con la función grid(), la función grid() dispone los elementos como si fuera una tabla, indicando como parámetros la fila y columna de la tabla para maquetar los elementos de nuestra ventana.
 
 ```
 from tkinter import *
 
#Creamos raíz
Ventana = Tk()
Ventana.resizable(0,0) #Impedimos redimensionar la ventana
Ventana.geometry('250x300') #Tamaño por defecto
Ventana.config(bg='white') #Color de fondo
Ventana.title('Aplicación') #Titulo de ventana

#Cremos label
Etiqueta = Label(Ventana, text = "Mi primera etiqueta")
Etiqueta.grid(row=0, column=0)

#Bucle de aplicación
Ventana.mainloop()
 
 ```
La etiqueta tiene color de fondo por defecto, por lo que vamos a especificarle el mismo color de fondo que la raíz y además aumentaremos el tamaño de letra, también pondremos las letras verdes y añadiremos un margen para que no aparezca pegada al borde.

```
from tkinter import *

#Creamos raíz
Ventana = Tk()
Ventana.resizable(0,0) #Impedimos redimensionar la ventana
Ventana.geometry("250x300") #Tamaño por defecto
Ventana.config(bg="white") #Color de fondo
Ventana.title("Mi Aplicación") #Titulo de ventana

#Cremos label
Etiqueta = Label(Ventana, text = "Mi primera etiqueta")
Etiqueta.grid(row=0, column=0)
Etiqueta.config(bg="white",        #Color de fondo
                fg="green",        #Color de letras
                font=("Arial", 12),#Tipo y tamaño de letra
                padx=10, pady=10)  #Margenes
                
#Bucle de aplicación
Ventana.mainloop()

```
Asimismo, podemos modificar el texto de la etiqueta durante de la ejecución, esto se hace creando una variable de tipo StringVar() y asignandola a nuestra etiqueta, el label mostrará en cada momento el valor de esta variable.

```
from tkinter import *

#Creamos raíz
Ventana = Tk()
Ventana.resizable(0,0) #Impedimos redimensionar la ventana
Ventana.geometry("250x300") #Tamaño por defecto
Ventana.config(bg="white") #Color de fondo
Ventana.title("Mi Aplicación") #Titulo de ventana

#Variable label
TextoEtiqueta = StringVar()
TextoEtiqueta.set("Hola")

#Cremos label
Etiqueta = Label(Ventana, text = "Mi primera etiqueta")
Etiqueta.grid(row=0, column=0)
Etiqueta.config(bg="white",        #Color de fondo
                fg="green",        #Color de letras
                font=("Arial", 12),#Tipo y tamaño de letra
                padx=10, pady=10,  #Margenes
                textvariable=TextoEtiqueta)  #Texto variable
                
#Bucle de aplicación
Ventana.mainloop()
```

**4.** Otras de las cosas que podemos añadir es la posibilidad de introducir texto manualmente, esto lo haremos a través de un widget Entry.

```
from tkinter import *

#Creamos raíz
Ventana = Tk()
Ventana.resizable(0,0) #Impedimos redimensionar la ventana
Ventana.geometry("250x300") #Tamaño por defecto
Ventana.title("Mi Aplicación") #Titulo de ventana

#Variable de captura de texto
Captura = StringVar()

#Cremos campo de texto
Entrada = Entry(Ventana)
Entrada.grid(row=0, column=0)
Entrada.config(textvariable=Captura)

#Bucle de aplicación
Ventana.mainloop()

```

Lo primero se ha creado una variable Captura de tipo StringVar(), esta variable es para capturar los datos introducidos en el campo de texto, posteriormente en el config del campo de texto (variable Entrada) hemos especificado que textvariable es Captura, esto hará que guardemos en esta variable lo introducido en el campo de texto, pero para poder utilizarlo utilizar los botones.


**5.** Los botones lo definimos a través de un widget Button. Crearemos un botón y lo colocaremos a la derecha de nuestro campo de texto, con la función grid() le especificaremos la columna 1 (la anterior era 0)

```
from tkinter import *

#Creamos raíz
Ventana = Tk()
Ventana.resizable(0,0) #Impedimos redimensionar la ventana
Ventana.geometry("250x300") #Tamaño por defecto
Ventana.title("Mi Aplicación") #Titulo de ventana

#Variable de captura de texto
Captura = StringVar()
#Cremos campo de texto
Entrada = Entry(Ventana)
Entrada.grid(row=0, column=0)
Entrada.config(textvariable=Captura)

#Creamos botón
Boton = Button(Ventana, text="AQUI")
Boton.grid(row=0, column=1)

#Bucle de aplicación
Ventana.mainloop()

```
Acabamos de crear el botón pero este no hace nada.

**6.** Le damos función al botón

```
from tkinter import *

def Copiar():
    """Lo obtenido por Captura lo pasamos a Resultado"""
    Resultado.set(Captura.get())
    
#Creamos raíz
Ventana = Tk()
Ventana.resizable(0,0) #Impedimos redimensionar la ventana
Ventana.geometry("170x90") #Tamaño por defecto
Ventana.title("Mi Aplicación") #Titulo de ventana

#Captura de texto
Captura = StringVar()
#Impresión de texto
Resultado = StringVar()

#Cremos campo de texto
Entrada = Entry(Ventana)
Entrada.grid(row=1, column=0)
Entrada.config(textvariable=Captura) #El texto se guarda en Captura

#Creamos botón
Boton = Button(Ventana, text="AQUI", command=Copiar) #Llama a Copiar
Boton.grid(row=1, column=1)

#Label de resultados 
Etiqueta = Label(Ventana, text = "") 
Etiqueta.grid(row=2, column=0, sticky="w") #En la tercera fila y alineado a la izquierda
Etiqueta.config(textvariable=Resultado) #Se muestra el texto de Resultado

#Etiqueta de título
Etiqueta2 = Label(Ventana, text = "REPETIDOR") 
Etiqueta2.grid(row=0, column=0, columnspan=2) #Ocupando dos columnas

#Bucle de aplicación
Ventana.mainloop()

```

**7.** Esto son algunas de las cosas que se puede hacer con la ventana gráficamente. Muchimas más cosas que se pueden utilizar son:

       -Frame(marcos): Los Frames son marcos contenedores de otros widgets. Pueden tener tamaño propio y posicionarse en distintos lugares de otro contenedor (ya sea    la raíz u otro marco).
       
```
from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('hola.ico') #icono de la ventana, en ico o xbm en Linux

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1) 
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25) #tamaño del borde en píxeles
frame.config(relief="sunken") #relieve del frame hundido

root.config(cursor="arrow") #tipo del cursor
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# Finalmente bucle de la aplicación
root.mainloop()

```

      -Radiobutton: Se utilizan cuando quieres ofrecerle al usuario la posibilidad de elegir una opción entre varias.
      
 ```
 from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")

# Configuración de la raíz
root = Tk()

opcion = IntVar()

Radiobutton(root, text="Opción 1", variable=opcion, 
            value=1, command=seleccionar).pack()
Radiobutton(root, text="Opción 2", variable=opcion, 
            value=2, command=seleccionar).pack()
Radiobutton(root, text="Opción 3", variable=opcion,   
            value=3, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

# Finalmente bucle de la aplicación
root.mainloop()
 
 ```
 
      -Checkbutton: si queremos simplemente proponer una única opción es mejor utilizar un botón de selección.
      
 ```
 from tkinter import *

def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if (azucar.get()):
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"

    monitor.config(text=cadena)

# Configuración de la raíz
root = Tk()
root.title("Cafetería")
root.config(bd=15)

leche = IntVar()    # 1 si, 0 no
azucar = IntVar()   # 1 si, 0 no

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="¿Cómo quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, 
            offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azúcar", variable=azucar, onvalue=1, 
            offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

# Finalmente bucle de la aplicación
root.mainloop()
 
 ```
       -Menú
       
```
from tkinter import *

# Configuración de la raíz
root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Finalmente bucle de la aplicación
root.mainloop()


```
     -Dialogs(diálogos): Las ventanas emergentes, cuadros de diálogo o simplemente Pop Ups, sirven para mostrar o pedir información rápida al usuario. Reciben ese nombre porque no forma parte de la ventana principal, sinó que aparecen de golpe encima.

      La ventana emergente por excelencia es la MessageBox, que sirve para mostrar un icono y un mensaje, pero tiene algunas variantes. Desde la clásico ventana con la opción de aceptar, la de alerta para informar de excepciones o errores, y las de aceptar o rechazar algo.
      
```
+MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje

+MessageBox.showwarning("Alerta", "Sección sólo para administradores.")

+MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")

+resultado = MessageBox.askquestion("Salir", 
    "¿Está seguro que desea salir sin guardar?")

if resultado == "yes":
    root.destroy()  # Destruir, alternativa a quit
    
+resultado = MessageBox.askokcancel("Salir", 
    "¿Sobreescribir fichero actual?")

if resultado == True:
    # Hacer algo
    
    
+resultado = MessageBox.askretrycancel("Reintentar",
    "No se puede conectar")

if resultado == True:
    # Hacer algo
    
+from tkinter import colorchooser as ColorChooser

def test():
    color = ColorChooser.askcolor(title="Elige un color")
    print(color)
    
    
+....

```
---------------------------------------------------------------------------------------------------------------------------------------------------------------

<h2>Código roomba:</h2><a name="id3"></a>

```
from tkinter import *
root = Tk()
root.geometry("600x600")

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

```
---------------------------------------------------------------------------------------------------------------------------------------------------------------


<h2>Código menú (ventana gráfica):</h2>

```
from roomba import *

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


```

---------------------------------------------------------------------------------------------------------------------------------------------------------------



<h2>Explicación paso a paso del código del roomba:</h2>






---------------------------------------------------------------------------------------------------------------------------------------------------------------


<h2>Resultados:</h2>

**En primer lugar nos pide que introduamos el número de zonas**


![interfaz 1](https://user-images.githubusercontent.com/91721875/223163257-f4a4b36b-0d76-48e9-a260-e9c74b441e80.png)




***

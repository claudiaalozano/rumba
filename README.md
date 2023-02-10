# rumba

<h1 align="center">Roomba</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/claudiaalozano/rumba.git)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea vamos a realizar dos ejercicios:


+El primero cosiste en desarrolla una interfaz, para ello usaremos tanto Gtk como tinker.

  -[Con Gtk](#id1)
  
  -[Con Tinker](#id2)
      
+El segundo en desarrolar un roomba, que nos calule el tiempo estimado que tardará en limpiar una superficie determinada.

***
## Integrantes:
1. [Alba](https://github.com/albabernal03) 
2. [Claudia](https://github.com/claudiaalozano)

***

<h2>Guía de creacion de una interfaz gráfica:</h2>

Una interfaz gráfica es un medio visual a través del cual es usuario puede interatuar y realizar tareas graficamente.

**CREAR INTERFAZ USANDO LA LIBRERIA GTK**<a name="id1"></a>

**Pasos:**



---------------------------------------------------------------------------------------------------------------------------------------------------------------

**CREAR INTERFAZ USANDO TINKER**<a name="id2"></a>

**Pasos:**

**1.** En primer lugar, lo primero que neesitamos es importar el módulo Tinker y crear una ventana, esto es la raíz, para la cual usaremos la función Tk(), será el      contenedor de nuestra aplicación, aquí iran todos los widgets.

A la raíz siempre se le añade un buble infinito , ya que una vez abrimos la aplicación siempre debe estar esperando órdenes.

```
from tinker import *

#Creamos la raíz
Ventana= Tk()

#Bucle de aplicación, es como un while True
Ventana.mainloop()

```
**2.** A continuaión le añadimos un título a nuestra ventana principal con el método title() e impondremos que su tamaño no sea modificable su tamaño con el método resizable(0,0); si pusieramos resizable(1,1) podríamos agrandar la ventana con el ratón en ambos en ambos ejes.

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

***

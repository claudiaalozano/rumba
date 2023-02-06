# rumba

<h1 align="center">rumba</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/claudiaalozano/rumba.git)

***
<h2>¿De qué trata esta tarea?</h2>
En esta tarea vamos a realizar dos ejercicios. El primero que hay que desarrollar una interfaz y el segundo que tenemos que desarrollar otra interfaz donde aparecerá las dimensiones de una habitación donde tenemos que calcular el tiempo que tarda una roomba en limpiarlo. 

***
## Integrantes:
1. [Alba](https://github.com/albabernal03) 
2. [Claudia](https://github.com/claudiaalozano)

***

<h2>Guía de creacion de una interfaz gráfica:</h2>

**Pasos:**

**1.** En primer lugar importamos las librerías que necesitamos para desarrollar el programa, en esta ocasión hemos importado las siguientes librerias:

       -Pandas: Esta librería la utilizamos para leer y crear el Dataframe.
       -Numpy: Esta librería nos proporciona una gran cantidad de funciones matemáticas, de las cuales usamos por ejemplo: .mean(), .std(), .mean()...
       -Matplotlib.pyplot: Esta librería lo que nos permite es la creación de gráficos en dos dimensiones, como diagrama de barras, histogramas...
       -Seaborn: Esta libreria se podría explicar como una extensión del Matplotlib.
 
 **2.** A continuación creamos uba función donde se crea el dataset, el cual es limpiado; eliminando los valores nulos con uso de la función **dropna** y ordenado con ayuda de la función conocida como **sort**. Asimismo dentro de esta función encontramos su lectura con uso de **Pandas**.
 
 **3.** Ahora creamos distintas funciones con las que haremos los calculos estadísticos, dentro de cada función usamos la librería numpy para realizar los cálculos.
 
        -media: para su cálculo utilizamos la función .mean()
        -desviación típica: para su cálculo utilizamos la función .std()
        -mediana: para su cáculo utilizamos la función .median()
        -moda: para su cálculo utilizamos la función .mode()
        -cuartiles: para su cálculo utilizamos la función .quantile()

**4.** Creamos una funcion que nos muestre la cantidad de naranjas que pensan menos de 130 gramos. Para que cuente la cantidad utilizamos la función .count()

**5.** Por último creamos los distintos diagramas.
       
       -Diagrama de sectores: utilizamos la librería Matplotlib. Dentro de esta función encontramos uso de diversas funciones como son:
       
                              *ax.pie(): se utiliza para trazar gráficos circulares.
                              *plt.subplots(): es una función que devuelve una tupla que contiene una figura y objeto (s) de ejes. Por lo tanto, al usar fig, ax = plt.subplots() descomprime esta tupla en las variables fig y ax. Teniendo fig es útil si desea cambiar los atributos a nivel de figura o guardar la figura como un archivo de imagen más tarde (por ejemplo, con fig.savefig('yourfilename.png')).
                              *plt.title(): lo utlizamos para especificar el título de la visualización representada.
    
       -Diagrma de barras: utilizamos dos librerías: Matplotlib y Seaborn.
                           
                              *sns.countplot(): se usa para mostrar los conteos de observaciones en cada contenedor categórico usando barras.
                             
       
       -Diagrama de dispersión: utilizamos la libreía Matplotlib.
       
                               *plt.scatter(): se usa para crear diagramas de dispersión

***

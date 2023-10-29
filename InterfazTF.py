import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from main import *

matrizPesos = generarMatrizSimetrica()

dijkstra = AlgortimoDeDijkstra(matrizPesos)
grafo = createVisualGraph(matrizPesos)
grafo.render('MyGrafo', format='png')

def boton1_accion():
    dijkstra.actualizarMatriz()
    nueva_imagen = Image.open("MyGrafo.png")
    nueva_imagen = nueva_imagen.resize((400, 350))
    nueva_imagen_tk = ImageTk.PhotoImage(nueva_imagen)
    imagen_label.configure(image=nueva_imagen_tk)
    imagen_label.image = nueva_imagen_tk 
    etiqueta_resultado.configure(text="") 

def boton2_accion():
    valor_entry2 = int(entry2.get())
    valor_entry3 = int(entry3.get())
    camino, peso = dijkstra.encontrarCaminoMinimo(valor_entry2, valor_entry3)
    etiqueta_resultado.configure(text=f"Camino: {camino}\nPeso: {peso}")

ventana = tk.Tk()
ventana.title("Algortimo de Dijkstra")

ventana.geometry("780x374")

imagen_fondo = ImageTk.PhotoImage(Image.open("fondo.png"))
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crea un marco para la imagen
marco_imagen = tk.Frame(ventana, bg="#748cab", padx=10, pady=10)
marco_imagen.grid(row=0, column=0, rowspan=4)

image = Image.open("MyGrafo.png")

new_size = (400, 350)  # Replace with the desired size
image = image.resize(new_size)

imagen = ImageTk.PhotoImage(image)

imagen_label = tk.Label(marco_imagen, image=imagen)
imagen_label.pack()

# Estilo para los botones
estilo_boton = ttk.Style()
estilo_boton.configure('TButton', font=('Arial', 8), foreground='#1d2d44', background='#1d2d44', padding=5)

# Estilo para las etiquetas
estilo_etiqueta = ttk.Style()
estilo_etiqueta.configure('TLabel', font=('Arial', 8), foreground='#f0ebd8', background='#3e5c76', padding=5)

# Crear los botones y etiquetas con los estilos
boton1 = ttk.Button(ventana, text="Actualizar Grafo", command=boton1_accion, style='TButton')
etiqueta2 = ttk.Label(ventana, text="Ingrese el nodo inicial", style='TLabel')
etiqueta3 = ttk.Label(ventana, text="Ingrese el nodo final", style='TLabel')
boton2 = ttk.Button(ventana, text="Hallar camino minimo", command=boton2_accion, style='TButton')
etiqueta_resultado = ttk.Label(ventana, text="", style='TLabel')

boton1.grid(row=0, column=1, padx=20, pady=5)

etiqueta2.grid(row=1, column=0, padx=20, pady=5)
entry2 = tk.Entry(ventana, width=10)
entry2.grid(row=1, column=1, padx=20, pady=5)

etiqueta3.grid(row=2, column=0, padx=20, pady=5)
entry3 = tk.Entry(ventana, width=10)
entry3.grid(row=2, column=1, padx=20, pady=5)

boton2.grid(row=3, column=0, padx=20, pady=5)
etiqueta_resultado.grid(row=3, column=1, padx=20, pady=5)

# Separa la distancia entre los botones y los Entry en la misma fila
boton1.grid(row=0, column=1, padx=(110, 0), pady=5)

etiqueta2.grid(row=1, column=1, padx=5, pady=5, columnspan=1)
entry2.grid(row=1, column=2, padx=5, pady=5, columnspan=1)

etiqueta3.grid(row=2, column=1, padx=5, pady=5, columnspan=1)
entry3.grid(row=2, column=2, padx=5, pady=5, columnspan=1)

boton2.grid(row=3, column=1, padx=5, pady=5, columnspan=1)
etiqueta_resultado.grid(row=3, column=2, padx=5, pady=5, columnspan=1)


ventana.mainloop()
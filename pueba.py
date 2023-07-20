import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import timeit
import random
from sorts import *

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def burbuja():
    tamano = int(element_entry.get())
    rango = int(range_entry.get())
    ax.clear()
    ax.set_ylabel("Tiempo (segundos)")
    ax.set_xlabel("Tamaño de la lista")

    # Datos para diferentes casos de Big O
    x = np.arange(0, tamano + 1, rango)

    # Caso O(n) - Linear Time
    y_on = x / 1000000  # Convertir microsegundos a segundos

    # Caso O(n^2) - Quadratic Time
    y_n2 = (x ** 2) / 1000000  # Convertir microsegundos a segundos

    ax.plot(x, y_on, label="O(n)", color='blue', linestyle='--')
    ax.plot(x, y_n2, label="O(n^2)", color='red', linestyle='--')

    tmpx = [0]
    tmpy = [0]

    for i in range(0, tamano + 1, rango):
        lista = [random.randint(0, tamano - 1) for _ in range(i)]
        if i == 0:
            ax.plot(0, 0, 'g', label="Bubble Sort")
        tiempo_bubble_sort = timeit.timeit(lambda: quicksort(lista), number=1)
        ax.plot([tmpx[0], len(lista)], [tmpy[0], tiempo_bubble_sort], "g")
        tmpx[0] = len(lista)
        tmpy[0] = tiempo_bubble_sort

    ax.legend()
    canvas.draw()

# Crear la ventana Tkinter
root = tk.Tk()
root.title('Gráficas de la Big O')
root.state('zoomed')  # Mostrar en pantalla completa

# Crear el Frame para la sección de los botones
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Crear los botones y las entradas
ttk.Label(button_frame, text="Elementos: ", foreground="blue", font=("Arial", 16)).pack(pady=10)
element_entry = ttk.Entry(button_frame, foreground="blue", font=("Arial", 16))
element_entry.pack(pady=10)

ttk.Label(button_frame, text="Rango de recorrido: ", foreground="blue", font=("Arial", 16)).pack(pady=10)
range_entry = ttk.Entry(button_frame, foreground="blue", font=("Arial", 16))
range_entry.pack(pady=10)

ttk.Button(button_frame, text='Bubble Sort', command=burbuja).pack(pady=10)
ttk.Button(button_frame, text='Bubble Sort', command=burbuja).pack(pady=10)
ttk.Button(button_frame, text='Bubble Sort', command=burbuja).pack(pady=10)
ttk.Button(button_frame, text='Bubble Sort', command=burbuja).pack(pady=10)
ttk.Button(button_frame, text='Bubble Sort', command=burbuja).pack(pady=10)
ttk.Button(button_frame, text='Bubble Sort', command=burbuja).pack(pady=10)


# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño del gráfico

# Crear el widget para mostrar el gráfico
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Agregar la figura del gráfico a un Frame para ubicarla a la derecha de los botones
graph_frame = ttk.Frame(root)
graph_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
graph_frame.grid_rowconfigure(0, weight=1)
graph_frame.grid_columnconfigure(0, weight=1)

# Mostrar la ventana
root.mainloop()

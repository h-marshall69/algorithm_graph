import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import timeit
import random
from sorts import *

def add_asymptotes(ax, tamano, rango):
    # Complejidad O(n)
    x = np.linspace(0, tamano, 100)
    ax.plot(x, x / rango, 'r--', label='O(n)')

    # Complejidad O(n^2)
    ax.plot(x, (x / rango) ** 2, 'm--', label='O(n^2)')

    # Complejidad O(log n)
    ax.plot(x, np.log2(x / rango), 'c--', label='O(log n)')

def order_sort(ax, sort_func, lista, x, y, label, color):
    tiempo_sort_microseconds = timeit.timeit(lambda: sort_func(lista), number=1)
    tiempo_sort_seconds = tiempo_sort_microseconds / 1e6  # Convertir microsegundos a segundos
    tiempo_sort_seconds_10x = tiempo_sort_seconds * 1000000000  # Ajustar a segundos * 10
    print(tiempo_sort_seconds_10x)
    ax.plot([x[0], len(lista)], [y[0], tiempo_sort_seconds_10x], color)
    x[0] = len(lista)
    y[0] = tiempo_sort_seconds_10x


def sort_graph(sort_func, label, color):
    tamano = int(element_entry.get())
    rango = int(range_entry.get())
    ax.clear()
    ax.set_ylabel("Tiempo (segundos * 10)")
    ax.set_xlabel("Tamaño de la lista")

    add_asymptotes(ax, tamano, rango)  # Agregar las asíntotas al gráfico

    tmpx = [0]
    tmpy = [0]

    for i in range(0, tamano + 1, rango):
        lista = [random.randint(0, tamano - 1) for _ in range(i)]
        if sort_func == heapify_wrap:  # Si es heapify_wrap, utilizarlo con los argumentos adicionales
            if i == 0:
                ax.plot(0, 0, color, label=label)
            order_sort(ax, sort_func, lista, tmpx, tmpy, label, color)
        else:
            if i == 0:
                ax.plot(0, 0, color, label=label)
            order_sort(ax, sort_func, lista, tmpx, tmpy, label, color)

    ax.legend()
    canvas.draw()

# Crear la ventana Tkinter
root = tk.Tk()
root.title('Gráficas de la Big O')
root.state('zoomed')  # Mostrar en pantalla completa

# Crear el Frame para la sección de los botones
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Definir variables para los valores por defecto de los inputs
element_default = tk.StringVar(value="2000")  # Valor por defecto de elementos
range_default = tk.StringVar(value="100")  # Valor por defecto del rango

# Crear los botones y las entradas
ttk.Label(button_frame, text="Elementos: ", foreground="blue", font=("Arial", 16)).pack(pady=10)
element_entry = ttk.Entry(button_frame, foreground="blue", font=("Arial", 16), textvariable=element_default)
element_entry.pack(pady=10)

ttk.Label(button_frame, text="Rango de recorrido: ", foreground="blue", font=("Arial", 16)).pack(pady=10)
range_entry = ttk.Entry(button_frame, foreground="blue", font=("Arial", 16), textvariable=range_default)
range_entry.pack(pady=10)

ttk.Button(button_frame, text='Bubble Sort', command=lambda: sort_graph(bubble_sort, "Bubble Sort", 'g')).pack(pady=10)
ttk.Button(button_frame, text='QuickSort', command=lambda: sort_graph(quicksort, "QuickSort", 'b')).pack(pady=10)
ttk.Button(button_frame, text='Selection Sort', command=lambda: sort_graph(selection_sort, "Selection Sort", 'y')).pack(pady=10)
ttk.Button(button_frame, text='Shell Sort', command=lambda: sort_graph(shell_sort, "Shell Sort", 'g')).pack(pady=10)
ttk.Button(button_frame, text='Merge Sort', command=lambda: sort_graph(merge_sort, "Merge Sort", 'b')).pack(pady=10)
ttk.Button(button_frame, text='Heap Sort', command=lambda: sort_graph(heap_sort, "Heap Sort", 'y')).pack(pady=10)
ttk.Button(button_frame, text='Heapify', command=lambda: sort_graph(heapify, "Heapify", 'y')).pack(pady=10)
ttk.Button(button_frame, text='Merge Sort', command=lambda: sort_graph(comb_sort, "Comb Sort", 'b')).pack(pady=10)
ttk.Button(button_frame, text='Heapify', command=lambda: sort_graph(cocktail_sort, "Cocktail Sort", 'y')).pack(pady=10)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(12, 8))  # Ajustar el tamaño del gráfico

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

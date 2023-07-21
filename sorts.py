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

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

def order_sort(ax, sort_func, lista, x, y, label, color):
    tiempo_sort = timeit.timeit(lambda: sort_func(lista), number=1)
    ax.plot([x[0], len(lista)], [y[0], tiempo_sort], color)
    x[0] = len(lista)
    y[0] = tiempo_sort

def sort_graph(sort_func, label, color):
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

    # Caso O(n log n) - Logarithmic Time
    y_n_log_n = x * np.log(x) / 1000000  # Convertir microsegundos a segundos

    ax.plot(x, y_on, label="O(n)", color='blue', linestyle='--')
    ax.plot(x, y_n2, label="O(n^2)", color='red', linestyle='--')
    ax.plot(x, y_n_log_n, label="O(n log n)", color='green', linestyle='--')

    tmpx = [0]
    tmpy = [0]

    for i in range(0, tamano + 1, rango):
        lista = [random.randint(0, tamano - 1) for _ in range(i)]
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

# Crear los botones y las entradas
ttk.Label(button_frame, text="Elementos: ", foreground="blue", font=("Arial", 16)).pack(pady=10)
element_entry = ttk.Entry(button_frame, foreground="blue", font=("Arial", 16))
element_entry.pack(pady=10)

ttk.Label(button_frame, text="Rango de recorrido: ", foreground="blue", font=("Arial", 16)).pack(pady=10)
range_entry = ttk.Entry(button_frame, foreground="blue", font=("Arial", 16))
range_entry.pack(pady=10)

ttk.Button(button_frame, text='Bubble Sort', command=lambda: sort_graph(bubble_sort, "Bubble Sort", 'g')).pack(pady=10)
ttk.Button(button_frame, text='QuickSort', command=lambda: sort_graph(quicksort, "QuickSort", 'b')).pack(pady=10)
ttk.Button(button_frame, text='Selection Sort', command=lambda: sort_graph(selection_sort, "Selection Sort", 'y')).pack(pady=10)
ttk.Button(button_frame, text='Shell Sort', command=lambda: sort_graph(shell_sort, "Bubble Sort", 'g')).pack(pady=10)
ttk.Button(button_frame, text='Merge Sort', command=lambda: sort_graph(merge_sort, "Merge Sort", 'b')).pack(pady=10)
ttk.Button(button_frame, text='Heap Sort', command=lambda: sort_graph(heap_sort, "Heap Sort", 'y')).pack(pady=10)
ttk.Button(button_frame, text='Merge Sort', command=lambda: sort_graph(merge_sort, "Merge Sort", 'b')).pack(pady=10)
ttk.Button(button_frame, text='Heapify', command=lambda: sort_graph(heapify, "Heapify", 'y')).pack(pady=10)
ttk.Button(button_frame, text='Merge Sort', command=lambda: sort_graph(comb_sort, "Comb Sort", 'b')).pack(pady=10)
ttk.Button(button_frame, text='Heapify', command=lambda: sort_graph(cocktail_sort, "Cocktail Sort", 'y')).pack(pady=10)

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

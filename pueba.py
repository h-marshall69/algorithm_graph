import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import timeit
import random

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

def order_selection_sort(ax, lista, x, y):
    tiempo_selection_sort = timeit.timeit(lambda: selection_sort(lista), number=1)
    ax.plot([x[0], len(lista)], [y[0], tiempo_selection_sort], "g")
    x[0] = len(lista)
    y[0] = tiempo_selection_sort

def selection_sort_graph():
    tamano = int(element_entry.get())
    rango = int(range_entry.get())
    ax.clear()
    ax.set_ylabel("Tiempo (segundos)")
    ax.set_xlabel("Tamaño de la lista")

    # Datos para diferentes casos de Big O
    x = np.arange(0, tamano + 1, rango)

    # Caso O(n log n) - Logarithmic Time
    y_n_log_n = x * np.log(x) / 1000000  # Convertir microsegundos a segundos

    # Caso O(n^2) - Quadratic Time
    y_n2 = (x ** 2) / 1000000  # Convertir microsegundos a segundos

    # Caso O(n^3) - Cubic Time (opcional, si deseas mostrarlo)
    y_n3 = (x ** 3) / 1000000  # Convertir microsegundos a segundos
    # Caso O(1) - Constant Time
    y_1 = np.full_like(x, 1) / 1000000  # Convertir microsegundos a segundos

    ax.plot(x, y_1, label="O(1)", color='purple', linestyle='--')
    ax.plot(x, y_n_log_n, label="O(n log n)", color='green', linestyle='--')
    ax.plot(x, y_n2, label="O(n^2)", color='red', linestyle='--')
    # ax.plot(x, y_n3, label="O(n^3)", color='orange', linestyle='--')  # Descomenta esta línea si deseas mostrar O(n^3)

    tmpx = [0]
    tmpy = [0]

    for i in range(0, tamano + 1, rango):
        lista = [random.randint(0, tamano - 1) for _ in range(i)]
        if i == 0:
            ax.plot(0, 0, 'g', label="SelectionSort")
        order_selection_sort(ax, lista, tmpx, tmpy)

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

ttk.Button(button_frame, text='selection sort', command=selection_sort_graph).pack(pady=10)


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

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import random
from matplotlib.figure import Figure
from sorts import *

root = Tk()
root.geometry("800x550")
root.title("Transición de gráficos")
frame1 = Frame(root, highlightbackground="blue", highlightthickness=2)
frame2 = Frame(root)

fig = Figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=frame2)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def ordenar():
    ax.cla()
    ax.set_ylabel("Tiempo (segundos)")
    ax.set_xlabel("Tamaño de la lista")

    canvas.draw()
    tmpx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tmpy = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tamano = 5001
    lista = []
    for i in range(0, tamano, 100):
        if var1.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, 'g', label="Bubble Sort")
            order_bubble_sort(ax, lista, tmpx, tmpy)
        if var2.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, 'r', label="Quicksort")
            order_quicksort(ax, lista, tmpx, tmpy)
        
        if var3.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, 'b', label="Selection Sort")
            order_selection_sort(ax, lista, tmpx, tmpy)

        if var4.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, 'y', label="Insertion Sort")
            order_insertion_sort(ax, lista, tmpx, tmpy)
        
        if var5.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#FF00FF', label="Shell Sort")
            order_shell_sort(ax, lista, tmpx, tmpy)
        
        if var6.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#FFA500', label="Merge Sort")
            order_merge_sort(ax, lista, tmpx, tmpy)
        
        if var7.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#800080', label="Heap Sort")
            order_heap_sort(ax, lista, tmpx, tmpy)
        
        if var8.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#444444', label="Comb Sort")
            order_comb_sort(ax, lista, tmpx, tmpy)

        if var9.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#CCCCCC', label="Cocktail Sort")
            order_cocktail_sort(ax, lista, tmpx, tmpy)

        canvas.draw()
        root.update()
        time.sleep(0.0001)
        ax.legend()

var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()
var5 = BooleanVar()
var6 = BooleanVar()
var7 = BooleanVar()
var8 = BooleanVar()
var9 = BooleanVar()
checkbox1 = Checkbutton(frame1, text="Bubble Sort", variable=var1, width=20)
checkbox2 = Checkbutton(frame1, text="Quicksort", variable=var2, width=20)
checkbox3 = Checkbutton(frame1, text="Selection Sort", variable=var3, width=20)
checkbox4 = Checkbutton(frame1, text="Insertion Sort", variable=var4, width=20)
checkbox5 = Checkbutton(frame1, text="Shell Sort", variable=var5, width=20)
checkbox6 = Checkbutton(frame1, text="Merge Sort", variable=var6, width=20)
checkbox7 = Checkbutton(frame1, text="Heap Sort", variable=var7, width=20)
checkbox8 = Checkbutton(frame1, text="Comb Sort", variable=var8, width=20)
checkbox9 = Checkbutton(frame1, text="Cocktail Sort", variable=var9, width=20)
simular = Button(frame1, text = "Simular", command=ordenar)

frame1.pack(side="left")
frame2.pack(side="right")

checkbox1.pack()
checkbox2.pack()
checkbox3.pack()
checkbox4.pack()
checkbox5.pack()
checkbox6.pack()
checkbox7.pack()
checkbox8.pack()
checkbox9.pack()
simular.pack()
root.mainloop()
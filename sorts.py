import time

# Función para realizar el Bubble Sort y capturar el tiempo de ejecución
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

def shell_sort(lista):
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    mitad = len(lista) // 2
    lista_izq = lista[:mitad]
    lista_der = lista[mitad:]
    
    lista_izq = merge_sort(lista_izq)
    lista_der = merge_sort(lista_der)
    
    return merge(lista_izq, lista_der)
    
def merge(lista_izq, lista_der):
    lista_ordenada = []
    i, j = 0, 0
    
    while i < len(lista_izq) and j < len(lista_der):
        if lista_izq[i] < lista_der[j]:
            lista_ordenada.append(lista_izq[i])
            i += 1
        else:
            lista_ordenada.append(lista_der[j])
            j += 1
    
    lista_ordenada += lista_izq[i:]
    lista_ordenada += lista_der[j:]
    
    return lista_ordenada

def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

def heapify(lista, n, i):
    maximo = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and lista[izquierda] > lista[maximo]:
        maximo = izquierda

    if derecha < n and lista[derecha] > lista[maximo]:
        maximo = derecha

    if maximo != i:
        lista[i], lista[maximo] = lista[maximo], lista[i]
        heapify(lista, n, maximo)

def comb_sort(lista):
    n = len(lista)
    factor = 1.3
    gap = n
    intercambio = True

    while intercambio or gap > 1:
        gap = int(gap / factor)
        intercambio = False
        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambio = True

def cocktail_sort(lista):
    n = len(lista)
    intercambio = True
    inicio = 0
    fin = n - 1

    while intercambio:
        intercambio = False
        for i in range(inicio, fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambio = True
        fin -= 1
        
        for i in range(fin, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                intercambio = True
        inicio += 1

def order_bubble_sort(ax, lista, x, y):
    
    inicio = time.time()
    bubble_sort(lista)
    fin = time.time()
    nosesdsd = (fin -inicio)
    ax.plot([x[0], len(lista)], [y[0], nosesdsd], "g")
    #ax.plot(len(lista), nosesdsd, "g")
    x[0] = len(lista)
    y[0] = fin - inicio

listanose1 = []
listanose2 = []
def order_bubble_sort2(lista):
    inicio = time.time()
    bubble_sort(lista)
    fin = time.time()
    nosesdsd = (fin -inicio)
    listanose1.append(len(lista))
    listanose2.append(nosesdsd)
    

def order_quicksort(ax, lista, x, y):
    inicio = time.time()
    quicksort(lista)
    fin = time.time()
    ax.plot([x[1], len(lista)], [y[1], (fin - inicio)], "r")
    x[1] = len(lista)
    y[1] = fin - inicio

def order_selection_sort(ax, lista, x, y):
    inicio = time.time()
    selection_sort(lista)
    fin = time.time()
    ax.plot([x[2], len(lista)], [y[2], (fin - inicio)], "b")
    x[2] = len(lista)
    y[2] = fin - inicio

def order_insertion_sort(ax, lista, x, y):
    inicio = time.time()
    insertion_sort(lista)
    fin = time.time()
    ax.plot([x[3], len(lista)], [y[3], (fin - inicio)], "y")
    x[3] = len(lista)
    y[3] = fin - inicio

def order_shell_sort(ax, lista, x, y):
    inicio = time.time()
    shell_sort(lista)
    fin = time.time()
    ax.plot([x[4], len(lista)], [y[4], (fin - inicio)], "#FF00FF")
    x[4] = len(lista)
    y[4] = fin - inicio

def order_merge_sort(ax, lista, x, y):
    inicio = time.time()
    merge_sort(lista)
    fin = time.time()
    ax.plot([x[5], len(lista)], [y[5], (fin - inicio)], "#FFA500")
    x[5] = len(lista)
    y[5] = fin - inicio

def order_heap_sort(ax, lista, x, y):
    inicio = time.time()
    heap_sort(lista)
    fin = time.time()
    ax.plot([x[6], len(lista)], [y[6], (fin - inicio)], "#800080")
    x[6] = len(lista)
    y[6] = fin - inicio

def order_comb_sort(ax, lista, x, y):
    inicio = time.time()
    comb_sort(lista)
    fin = time.time()
    ax.plot([x[7], len(lista)], [y[7], (fin - inicio)], "#444444")
    x[7] = len(lista)
    y[7] = fin - inicio

def order_cocktail_sort(ax, lista, x, y):
    inicio = time.time()
    cocktail_sort(lista)
    fin = time.time()
    ax.plot([x[8], len(lista)], [y[8], (fin - inicio)], "#CCCCCC")
    x[8] = len(lista)
    y[8] = fin - inicio
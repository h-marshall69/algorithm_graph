import random

def generate_sorted_list(size):
    return list(range(size))

def generate_reversed_list(size):
    return list(range(size, 0, -1))

def generate_random_list(size):
    return [random.randint(0, size) for _ in range(size)]

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
    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half = lista[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1

def heapify(lista, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lista[i] < lista[l]:
        largest = l

    if r < n and lista[largest] < lista[r]:
        largest = r

    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        heapify(lista, n, largest)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

def comb_sort(lista):
    n = len(lista)
    gap = n
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        swapped = False
        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                swapped = True

def cocktail_sort(lista):
    n = len(lista)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (lista[i] > lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (lista[i] > lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                swapped = True
        start = start + 1

def heapify_wrap(lista):
    n = len(lista)
    for i in range(n, -1, -1):
        heapify(lista, n, i)
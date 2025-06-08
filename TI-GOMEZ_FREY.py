"""
Estructuras de Datos y Algoritmos - Trabajo Práctico
Autor: Javier Gomez Frey

Este programa implementa y compara tres algoritmos de ordenamiento:
- Ordenamiento Burbuja (Bubble Sort)
- Ordenamiento por Mezcla (Merge Sort)
- Ordenamiento Rápido (Quick Sort)
"""

import random
import time
import matplotlib.pyplot as plt
import numpy as np

def generate_random_array(size):
    """Genera un array aleatorio de enteros con el tamaño especificado."""
    return [random.randint(1, 1000) for _ in range(size)]

def bubble_sort(arr):
    """
    Implementación del algoritmo de Ordenamiento Burbuja.
    Complejidad Temporal: O(n^2)
    Complejidad Espacial: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    """
    Implementación del algoritmo de Ordenamiento por Mezcla.
    Complejidad Temporal: O(n log n)
    Complejidad Espacial: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Función auxiliar para merge sort que combina dos arrays ordenados."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """
    Implementación del algoritmo de Ordenamiento Rápido.
    Complejidad Temporal: O(n log n) caso promedio, O(n^2) peor caso
    Complejidad Espacial: O(log n)
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_func, arr):
    """Mide el tiempo de ejecución de un algoritmo de ordenamiento."""
    arr_copy = arr.copy()
    start_time = time.time()
    sort_func(arr_copy)
    end_time = time.time()
    return end_time - start_time

def compare_algorithms(sizes):
    """Compara el rendimiento de todos los algoritmos de ordenamiento con diferentes tamaños de arrays."""
    bubble_times = []
    merge_times = []
    quick_times = []

    for size in sizes:
        arr = generate_random_array(size)
        
        bubble_time = measure_time(bubble_sort, arr)
        merge_time = measure_time(merge_sort, arr)
        quick_time = measure_time(quick_sort, arr)
        
        bubble_times.append(bubble_time)
        merge_times.append(merge_time)
        quick_times.append(quick_time)
        
        print(f"\nTamaño del array: {size}")
        print(f"Tiempo Bubble Sort: {bubble_time:.4f} segundos")
        print(f"Tiempo Merge Sort: {merge_time:.4f} segundos")
        print(f"Tiempo Quick Sort: {quick_time:.4f} segundos")
    
    return bubble_times, merge_times, quick_times

def plot_results(sizes, bubble_times, merge_times, quick_times):
    """Grafica los resultados de la comparación."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, 'o-', label='Ordenamiento Burbuja')
    plt.plot(sizes, merge_times, 's-', label='Ordenamiento por Mezcla')
    plt.plot(sizes, quick_times, '^-', label='Ordenamiento Rápido')
    plt.xlabel('Tamaño del Array')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Rendimiento de Algoritmos de Ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.savefig('comparacion_ordenamiento.png')
    plt.close()

def main():
    # Tamaños de arrays para pruebas
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
    
    print("Iniciando comparación de algoritmos...")
    bubble_times, merge_times, quick_times = compare_algorithms(sizes)
    
    # Graficar los resultados
    plot_results(sizes, bubble_times, merge_times, quick_times)
    print("\nLos resultados han sido graficados y guardados como 'comparacion_ordenamiento.png'")

if __name__ == "__main__":
    main()

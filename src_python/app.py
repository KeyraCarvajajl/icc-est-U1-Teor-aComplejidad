from benchmarking import Benchmarking
from sortMethods import SortMethods
import matplotlib.pyplot as plt

if __name__ == "__main__":

    benchmarking = Benchmarking()
    sortMethods = SortMethods()

    tamanios = [500, 600, 700]
    max_tamanio = max(tamanios)
    arreglo_base = benchmarking.build_arreglo(max_tamanio)

    metodos = {
        "burbuja": sortMethods.sort_bubble,
        "burbujaMejorado": sortMethods.sort_bubble_optimized,
        "insercion": sortMethods.sort_insertion,
        "seleccion": sortMethods.sort_selection,
        "shell": sortMethods.sort_shell
    }

    resultados = []

    for tamanio in tamanios:
        arreglo = arreglo_base[:tamanio]
        for nombre, metodo in metodos.items():
            copia = arreglo.copy()
            tiempo = benchmarking.medir_tiempo(metodo, copia)
            resultados.append((tamanio, nombre, tiempo))

    for tamanio, nombre, tiempo in resultados:
        print(f"Tamano: {tamanio}, Algoritmo: {nombre}, Tiempo: {tiempo:.4f} segundos")

    
    tiempos_by_metodo = {nombre: [] for nombre in metodos.keys()}
    for tamanio, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append((tamanio, tiempo))

    plt.figure(figsize=(10, 6))
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre)

    plt.title("Comparación de Tiempos de Métodos de Ordenamiento")
    plt.xlabel("Tamaño del Arreglo")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

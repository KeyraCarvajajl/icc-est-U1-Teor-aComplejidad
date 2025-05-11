import random
import time

class Benchmarking:

    def __init__(self):
        print("\n----- Benchmarking Iniciando -----")

    def build_arreglo(self, size):
        arreglo = []
        for i in range(size):
            numero = random.randint(0, 50000)
            arreglo.append(numero)
        return arreglo

    def medir_tiempo(self, metodo_ordenamiento, arreglo):
        inicio = time.perf_counter()
        metodo_ordenamiento(arreglo)
        fin = time.perf_counter()
        return fin - inicio

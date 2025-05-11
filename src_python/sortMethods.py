class SortMethods:
    def sort_bubble(self, array):
        arreglo = array.copy()
        tam = len(arreglo)
        for i in range(tam):
            for j in range(0, tam - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo

    def sort_bubble_optimized(self, array):
        arreglo = array.copy()
        tam = len(arreglo)
        for i in range(tam):
            hubo_intercambio = 0
            for j in range(0, tam - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    hubo_intercambio = 1
            if hubo_intercambio == 0:
                break
        return arreglo

    def sort_insertion(self, array):
        arreglo = array.copy()
        tam = len(arreglo)
        for i in range(1, tam):
            valor_actual = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > valor_actual:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = valor_actual
        return arreglo

    def sort_selection(self, array):
        arreglo = array.copy()
        tam = len(arreglo)
        for i in range(tam - 1):
            indice_min = i
            for j in range(i + 1, tam):
                if arreglo[j] < arreglo[indice_min]:
                    indice_min = j
            arreglo[i], arreglo[indice_min] = arreglo[indice_min], arreglo[i]
        return arreglo

    def sort_shell(self, array):
        arreglo = array.copy()
        tam = len(arreglo)
        gap = tam // 2
        while gap > 0:
            for i in range(gap, tam):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo

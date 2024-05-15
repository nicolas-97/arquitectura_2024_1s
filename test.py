class QuickSort:
    @staticmethod
    def particionar(arr, bajo, alto):
        pivote = arr[alto]
        i = bajo - 1
        j = bajo
        while j < alto:
            if arr[j] < pivote:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1

    @staticmethod
    def ordenar_rapido(arr, bajo, alto):
        if bajo < alto:
            pi = QuickSort.particionar(arr, bajo, alto)
            QuickSort.ordenar_rapido(arr, bajo, pi - 1)
            QuickSort.ordenar_rapido(arr, pi + 1, alto)

    @staticmethod
    def quickSort(input) -> list:
        arr = input.copy()
        QuickSort.ordenar_rapido(arr, 0, len(arr) - 1)
        return arr


# Ejemplo de uso
arr = [5, 3, 8, 6, 2, 7, 1, 4]
print("Lista original:", arr)
sorted_arr = QuickSort.quickSort(arr)
print("Lista ordenada:", sorted_arr)

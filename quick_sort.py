class QuickSort:
    @staticmethod
    def particionar(arr, bajo, alto):
        pivote = arr[alto]
        i = bajo - 1
        for j in range(bajo, alto):
            if arr[j] < pivote:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
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
        n = len(arr)
        QuickSort.ordenar_rapido(arr, 0, n - 1)
        return arr


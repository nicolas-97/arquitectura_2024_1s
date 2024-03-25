class QuickSort():
    def quickSort(input) -> list:
        QuickSort._quickSortRecursive(input, 0, len(input) - 1)
        return input

    def _quickSortRecursive(arr, low, high):
        if low < high:
            pi = QuickSort._partition(arr, low, high)
            QuickSort._quickSortRecursive(arr, low, pi - 1)
            QuickSort._quickSortRecursive(arr, pi + 1, high)

    def _partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

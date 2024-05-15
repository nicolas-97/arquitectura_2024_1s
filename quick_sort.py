class QuickSort():
    @staticmethod
    def partition(arr, start, end):
        pivot = arr[end]
        left_pointer = start - 1
        for current_index in range(start, end):
            if arr[current_index] <= pivot:
                left_pointer += 1
                arr[left_pointer], arr[current_index] = arr[current_index], arr[left_pointer]
        arr[left_pointer + 1], arr[end] = arr[end], arr[left_pointer + 1]
        return left_pointer + 1

    @staticmethod
    def quickSort(arr):
        def _quick_sort(arr, start, end):
            if start < end:
                pivot_index = QuickSortModified.partition(arr, start, end)
                _quick_sort(arr, start, pivot_index - 1)
                _quick_sort(arr, pivot_index + 1, end)
        
        _quick_sort(arr, 0, len(arr) - 1)
        return arr

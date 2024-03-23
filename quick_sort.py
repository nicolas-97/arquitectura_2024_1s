class QuickSort:
    @staticmethod
    def quickSort(input_list) -> list:
        if len(input_list) <= 1:
            return input_list
        else:
            pivot = input_list[0]
            less_than_pivot = [x for x in input_list[1:] if x <= pivot]
            greater_than_pivot = [x for x in input_list[1:] if x > pivot]
            return QuickSort.quickSort(less_than_pivot) + [pivot] + QuickSort.quickSort(greater_than_pivot)

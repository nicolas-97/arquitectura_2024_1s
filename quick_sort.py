class QuickSort:
    @staticmethod
    def quickSort(input_list):
        if len(input_list) <= 1:
            return input_list

        pivot = input_list[-1]

        smaller = [x for x in input_list if x < pivot]
        larger = [x for x in input_list if x > pivot]

        return QuickSort.quickSort(smaller) + [pivot] + QuickSort.quickSort(larger)

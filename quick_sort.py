class QuickSort():
    
    def quickSort(input) -> list:  
        if len(input) < 2:  
            return input  
        pivot = input[0]  
        left = [x for x in input[1:] if x < pivot]  
        right = [x for x in input[1:] if x >= pivot]  
        return QuickSort.quickSort(left) + [pivot] + QuickSort.quickSort(right)  


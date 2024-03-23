import unittest

from quick_sort import QuickSort

class Test(unittest.TestCase):
    def test_test_quick_sort_empty(self):
        input_data = []
        self.assertEqual(QuickSort.quickSort(input_data), [])

    def test_test_quick_sort_one_element(self):
        input_data = [1]
        self.assertEqual(QuickSort.quickSort(input_data), [1])
    
    def test_quick_sort_ascendent(self):
        input_data = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(QuickSort.quickSort(input_data), input_data)

    def test_quick_sort_descendent(self):
        input_data = [10,9,8,7,6,5,4,3,2,1]
        self.assertEqual(QuickSort.quickSort(input_data), sorted(input_data))


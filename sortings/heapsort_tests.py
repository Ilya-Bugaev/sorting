import random

import pytest
from bubble_sort import bubble_sort
from heapsort import heapsort


class TestHeapsortBasic:
    def test_empty(self):
        assert heapsort([]) == []
    
    def test_single(self):
        assert heapsort([5]) == [5]
    
    def test_sorted(self):
        assert heapsort([1, 2, 3]) == [1, 2, 3]
    
    def test_reverse(self):
        assert heapsort([3, 2, 1]) == [1, 2, 3]
    
    def test_duplicates(self):
        assert heapsort([2, 1, 2]) == [1, 2, 2]


class TestHeapsortEdgeCases:    
    def test_all_same(self):
        assert heapsort([3, 3, 3]) == [3, 3, 3]
    
    def test_negative(self):
        assert heapsort([-1, -3, -2]) == [-3, -2, -1]
    
    def test_mixed(self):
        assert heapsort([1, -1, 0]) == [-1, 0, 1]
    
    def test_large_range(self):
        assert heapsort([100, 1, -100]) == [-100, 1, 100]



class TestHeapsortParametrized:  
    @pytest.mark.parametrize("input_arr,expected", [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 1, 2], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([2, 1, 2], [1, 2, 2]),
        ([-1, -3], [-3, -1]),
        ([1, -1, 0], [-1, 0, 1]),
    ])
    def test_various_cases(self, input_arr, expected):
        assert heapsort(input_arr.copy()) == expected


class TestHeapsortPropertyBased:
    def test_random_arrays(self):
        """Сравнение на случайных массивах"""
        for _i in range(10):  # 10 случайных тестов
            size = random.randint(3, 100)
            arr = [random.randint(-100, 100) for n in range(size)]
            
            arr_copy1 = arr.copy()
            arr_copy2 = arr.copy()
            
            heapsort_result = heapsort(arr_copy1)
            bubble_sort_result = bubble_sort(arr_copy2)
            assert heapsort_result == bubble_sort_result










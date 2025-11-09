import pytest
from quicksort import quicksort


class TestQuickSort:
    
    def test_empty_list(self):
        assert quicksort([]) == []
    
    def test_single_element(self):
        assert quicksort([5]) == [5]
    
    def test_sorted_list(self):
        assert quicksort([1, 2, 3]) == [1, 2, 3]
    
    def test_reverse_sorted(self):
        assert quicksort([3, 2, 1]) == [1, 2, 3]
    
    def test_duplicates(self):
        assert quicksort([2, 1, 2]) == [1, 2, 2]


class TestQuickSortParametrized:
    
    @pytest.mark.parametrize("input_list,expected", [
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
    def test_quick_sort(self, input_list, expected):
        assert quicksort(input_list) == expected

import pytest
from bubble_sort import bubble_sort


class TestBubbleSort:
    
    def test_empty_list(self):
        assert bubble_sort([]) == []
    
    def test_single_element(self):
        assert bubble_sort([5]) == [5]
    
    def test_sorted_list(self):
        assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    
    def test_reverse_sorted(self):
        assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    
    def test_duplicates(self):
        assert bubble_sort([2, 1, 2]) == [1, 2, 2]


class TestBubbleSortParametrized:
    
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
    def test_bubble_sort(self, input_list, expected):
        assert bubble_sort(input_list) == expected


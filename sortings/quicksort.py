 
def quicksort(arr):

    #массивы длиной 0 или 1 уже отсортированы
    if len(arr) <= 1:
        return arr
    
    #Выбираем опорный элемент (pivot) - средний элемент
    pivot = arr[len(arr) // 2]
    
    #Разделяем массив на три части:
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    #Рекурсивно сортируем левую и правую части и объединяем
    return quicksort(left) + middle + quicksort(right)

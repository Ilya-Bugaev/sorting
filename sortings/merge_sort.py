def merge_sort(arr):
    #Базовый случай: массивы длиной 0 или 1 уже отсортированы
    if len(arr) <= 1:
        return arr
    
    #Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    #Рекурсивно сортируем обе половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    #Объединяем отсортированные половины
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = j = 0
    
    #Сравниваем элементы из обоих массивов и добавляем меньший в результат
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    #Добавляем оставшиеся элементы из левого массива
    while i < len(left):
        result.append(left[i])
        i += 1
    
    #Добавляем оставшиеся элементы из правого массива
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

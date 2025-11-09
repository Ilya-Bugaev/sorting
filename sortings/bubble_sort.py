# Функция сортировки пузырьком

def bubble_sort(nums):
    flag = True
    while flag:
        flag = False
        for i in range(len(nums)- 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                flag = True

    return nums



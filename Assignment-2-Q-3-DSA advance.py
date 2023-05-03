def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  

    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    lesser_sorted = quick_sort(lesser)
    greater_sorted = quick_sort(greater)
    
    return lesser_sorted + equal + greater_sorted

my_list = [4, 2, 8, 6, 10, 12, 14, 16, 18, 20]

sorted_list = quick_sort(my_list)

print(sorted_list)
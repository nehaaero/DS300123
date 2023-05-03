def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

my_list = [4, 2, 8, 6, 10, 12, 14, 16, 18, 20]

sorted_list = insertion_sort(my_list)

print(sorted_list)
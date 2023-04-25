def find_kth_largest_smallest(arr, k):
    """
    Find the Kth largest and Kth smallest number in an array.
    Args:
        arr (list): The input array.
        k (int): The value of K for finding Kth largest and Kth smallest.
    Returns:
        tuple: A tuple containing the Kth largest and Kth smallest numbers.
    """
    arr.sort()

    kth_smallest = arr[k - 1]

    kth_largest = arr[len(arr) - k]

    return kth_largest, kth_smallest

arr = [10, 2, 15, 7, 3, 9, 8, 11]
k = 3
kth_largest, kth_smallest = find_kth_largest_smallest(arr, k)
print("Kth largest number is:", kth_largest)
print("Kth smallest number is:", kth_smallest)
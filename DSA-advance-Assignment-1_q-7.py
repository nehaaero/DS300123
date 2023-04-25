def move_negative_to_one_side(arr):
    """
    Move all the negative elements to one side of the array.
    Args:
        arr (list): The input array.
    Returns:
        list: The updated array with all negative elements moved to one side.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
  
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

arr = [-3, 2, 1, -5, 6, -8, 9, -4, 7]
updated_arr = move_negative_to_one_side(arr)
print("Array with negative elements moved to one side:", updated_arr)   
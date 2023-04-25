def count_pairs_with_sum(arr, target_sum):
    """
    Count the number of pairs in an array that sum up to a given target sum.
    Args:
        arr (list): The input array.
        target_sum (int): The target sum to be checked.
    Returns:
        int: The count of pairs that sum up to the target sum.
    """
  
    freq_map = {}
    count = 0  

    for num in arr:
        complement = target_sum - num

        if complement in freq_map:
            count += freq_map[complement]

        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    return count

arr = [1, 5, 3, 7, 9, 2, 8, 4]
target_sum = 10
result = count_pairs_with_sum(arr, target_sum)
print("Number of pairs with sum", target_sum, "is:", result)
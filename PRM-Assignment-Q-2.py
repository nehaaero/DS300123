def sort_list_by_second_last_character(n, lst):
    sorted_lst = sorted(lst, key=lambda x: x[-2])
    return sorted_lst

# Read input
n = int(input())
lst = []
for i in range(n):
    lst.append(input())

# Sort the list based on the 2nd last character
sorted_lst = sort_list_by_second_last_character(n, lst)

# Print the sorted list
print(sorted_lst)


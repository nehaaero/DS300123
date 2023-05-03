def sort_strings_like_dict(string_list):
  return sorted(string_list, key=lambda x: x.lower())

my_list = ["Apple", "banana", "cherry", "Date", "elderberry"]
sorted_list = sort_strings_like_dict(my_list)
print(sorted_list)
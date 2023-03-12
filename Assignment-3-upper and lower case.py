def count_upper_lower(string):
    upper_count=0
    lower_count=0
    for char in string:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
    return upper_count, lower_count
sample_string='The quick Brow Fox'
upper_count, lower_count=count_upper_lower(sample_string)
print(f"no of upper case characters={upper_count}")
print(f"no of llower case characters={lower_count}")

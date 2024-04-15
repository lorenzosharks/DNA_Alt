my_list = [10, 20, 30, 40, 50, 60]
index_to_keep = 2  # Keep elements at index 0, 1, 2 (inclusive)

# Slice the list to keep elements up to index_to_keep (inclusive)
my_list = my_list[:index_to_keep + 1]

print(my_list)  # Output: [10, 20, 30]

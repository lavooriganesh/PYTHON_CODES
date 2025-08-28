data = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
print("Original Dictionary:", data)

unique_dict = {}
for key, value in data.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

print("Dictionary after removing duplicates:", unique_dict)

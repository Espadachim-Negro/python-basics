items=["apple", "banana", "apple", "cherry", "banana"]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print('Без дубликатов:', unique)
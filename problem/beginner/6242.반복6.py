blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
result = {}
for blood in blood_type:
    result[blood] = blood_type.count(blood)
print(result)
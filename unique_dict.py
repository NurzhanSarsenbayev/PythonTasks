# Написать программу, которая будет выводить все уникальные значения в словарей


my_list = [{"V": "S001"}, {"V": "S002"},
           {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {" V ": "S009"},
           {" VIII ": "S007"}]
print(my_list)

unique =set()
for item in my_list:
    for value in item.values():
        unique.add(value)
    # item.keys item.items
print(unique)
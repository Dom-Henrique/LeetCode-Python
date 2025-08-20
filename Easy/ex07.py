# Tirar duplicadas
list1 = [1, 2, 4, 5, 8, 10]
list2 = [1, 3, 6, 7, 4, 6]

list3 = list1
list3.extend(list2)
list3.sort()

print(set(list3))
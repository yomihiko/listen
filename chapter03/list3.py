list_a = [1, 2, 3]
all_list = [list_a, list_a, list_a]
print(all_list)
list_a.append(4)
print(all_list)
all_list[0].append(5)
print(all_list)
all_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
all_list[0].append(5)
print(all_list)
all_list = [list_a.copy(), list_a.copy(), list_a.copy()]

all_list[0].append(5)
print(all_list)

all_list = [list_a[:], list_a[:], list_a[:]]

all_list[0].append(8)
print(all_list)

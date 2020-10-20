numbers = [1, 2, 3, 4, 5]
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
numbers.insert(1, 1.5)
print(numbers)
numbers2 = [1, 2, 3, 4, 5]
numbers3 = [5, 6, 7, 8, 9]
print(numbers2.extend(numbers3) is None)
print(numbers2)
numbers4 = [10, 11, 12, 13, 14]
numbers2 = numbers2 + numbers4
print(numbers2)
numbers.pop(0)
print(numbers)
numbers.pop()
print(numbers)
list = ['a', 'i', 'u']
list.remove('i')
print(list)
print(numbers2.index(3))
print(1 in numbers2)
print(100 in numbers2)
numbers = [5, 3, 1, 4, 2]
numbers.sort(reverse=True)
print(numbers)
numbers = [5, 3, 1, 4, 2]
print(sorted(numbers))

def createIntList(numbers=[]):
    for i in range(10):
        numbers.append(i)
    return numbers


print(createIntList())
print(createIntList([4, 5, 6]))
p = [1, 2, 3]
createIntList(p)
print(p)

numbers = createIntList()
print(numbers)
numbers2 = createIntList()
print(numbers)

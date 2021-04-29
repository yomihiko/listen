numbers = [1, 5, 6, 11, 3, 5, 7, 3]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)

words = ['python', 'django', 'tkinter']
upper_words = [word.upper() for word in words]
print(upper_words)

even_numbers = [x for x in range(1, 11) if x % 2 == 1]
print(even_numbers)

table = [[x*y for x in range(1, 10)] for y in range(1, 10)]
print(table)

zerotable = [[0 for _ in range(5)] for _ in range(5)]
print(zerotable)

docs = {x: 'デフォルト値' for x in range(5)}
print(docs)

numbers = [1, 3, 5, 6, 7, 9, 11, 13]
square_gen = (num ** 2 for num in numbers)
print(square_gen)
for num in square_gen:
    print(num)

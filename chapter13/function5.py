def makeSquares(n):
    for i in range(1, n+1):
        yield i**2


def my_range(start, end, step):
    cuurentNumber = start
    while cuurentNumber < end:
        yield cuurentNumber
        cuurentNumber += step


squares = makeSquares(10)
for i in squares:
    print(i, end=',')

for i in my_range(1, 10, 0.5):
    print(i, end=',')

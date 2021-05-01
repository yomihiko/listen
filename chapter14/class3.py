class A:
    def __init__(self):
        self.number = 10


class B:
    number = 10


a = A()
print(a.number)

print(B.number)

b1 = B()
b2 = B()
B.number = 20
print(b1.number)
print(b2.number)

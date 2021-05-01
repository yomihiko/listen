class A:
    def __init__(self):
        self.count = 1

    def __len__(self):
        return 10

    def __iter__(self):
        return self

    def __next__(self):
        current = self.count
        if current > 10:
            raise StopIteration
        self.count += 1
        return current

    def __str__(self):
        return 'Aクラス'


a = A()
print(a)
print(len(a))
for count in a:
    print(count)

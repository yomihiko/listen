class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            value = '名無しさん'
        self._name = value


tanaka = Person('田中')
print(tanaka.name)
nanasi = Person('')
print(nanasi.name)

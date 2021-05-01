class Student:
    def __init__(self, name):
        self.name = name
        self.score = {}

    def addScore(self, subjectName, point):
        self.score[subjectName] = point

    def getScore(self, subjectName):
        return self.score.get(subjectName, '教科なし')


a = Student('やまみ')
print(a.name)
a.addScore('国語', 400)
print(a.getScore('国語'))
print(a.getScore('算数'))
print(type(a))

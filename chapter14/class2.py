class Character:
    def __init__(self, name):
        self.name = name

    def showProfile(self):
        print('名前：{0} 種族:Character'.format(self.name))


class Monster(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 20

    def showProfile(self):
        print('名前：{0} 種族:Monster HP:20'.format(self.name))


c = Character('キャラA')
print(c.name)
c.showProfile()
m = Monster('モンスターA')
print(m.name)
m.showProfile()

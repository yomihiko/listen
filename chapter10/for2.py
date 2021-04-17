names = ['真茅', '染岡', '栗松']
for index, name in enumerate(names):
    messeage = '{0}番目 {1}'.format(index + 1, name)
    print(messeage)

foods = ['納豆', 'ヨーグルト', 'チャーハン']
juices = ['コーラ', 'コーヒー', 'カフェラテ']
for food, juice in zip(foods, juices):
    print(food, juice)

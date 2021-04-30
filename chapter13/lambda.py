def mySort(string):
    return string[-1]


myList = ['python', 'ovg', 'kivy', 'apple', 'zoo']
myList.sort(key=mySort)
print(myList)

myList = [('納豆', 78), ('おまめ', 200), ('コーラ', 120), ('ポテチ', 60)]
myList.sort(key=lambda tpl: tpl[1])
print(myList)

numbers = [1, 2, 3, 4, 5]
for i in map(lambda num: '{0}です'.format(num), numbers):
    print(i, end=',')

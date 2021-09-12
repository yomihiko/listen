"""
with open('hello2.txt', 'x', encoding='utf-8') as file:
    file.write('hello')
"""

try:
    file = open("hello3.txt", "x", encoding='utf-8')
except FileExistsError:
    print('ファイルが既に存在しています')
else:
    file.write('hello')
finally:
    file.close()
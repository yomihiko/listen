text = """おはよう
こんにちは
こんばんは"""

file = open('./hello.txt', 'w', encoding='utf-8')

file.write(text)

file.close()

text = "追記"

file = open('./hello.txt', 'a', encoding='utf-8')

file.write(text)

file.close()

text = "追記"

# with open('./hello.txt', 'x', encoding='utf-8') as file:
#     file.write(text)

with open('shiro.by', 'wb') as file:
    file.write(b'\x89')

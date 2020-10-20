#  シーケンス型としての文字列操作
text = 'あいうえお'
print(text[0])
print(text[1])
print(text[-1])
# print(text[5])

text_len = len(text)
print(text[text_len - 1])
print(text[1:4])
print(text[1:])
print(text[:4])
print(text[:100])
print(text[-3:])
print(text[::2])
print(text[1:4][::2])
print(text[::-1])  # 逆順にする

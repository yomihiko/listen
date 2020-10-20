fmt = '名前は{}です'
name = 'ジャーヴィス'
fmt = fmt.format(name)  # 文字列のフォーマット
print(fmt)

fmt = '名前は{}{}ですわ'
print(fmt.format('佐藤', 'がん'))

fmt = '{0}{1}{0}'
print(fmt.format('ジャーヴィス', 'かわいいよ'))

passd = 'dust'
han = 'kakaka'
print(f'{han}{passd}')

name = 'なめ'
print('私の名前は%sです' % name)

languages = 'Python,Ruby,PHP,Perl'
lang_list = languages.split(',')
print(','.join(lang_list))
print('\n'.join(lang_list))
print(languages.replace('P', 'K'))  # 置き換え
print(languages.count('P'))  # 数える
print(languages.startswith('P'))  # 始まるか
print(languages.startswith('K'))

print(languages.find('PHP'))

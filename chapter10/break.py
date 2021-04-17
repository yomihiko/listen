# while True:
#     user_input = input()
#     if not user_input:
#         break
#     elif user_input == 'skip':
#         continue
#     print('あなたの入力は' + user_input)

names = ['キタサンブラック', 'アグネスタキオン', 'ダイタクヘリオス']

for name in names:
    if name.endswith('ヘリオス'):
        print('いました')
        break

else:
    print('いませんでした')

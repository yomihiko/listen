names = ["佐藤", "鈴木", "田中"]
for name in names:
    print(name)

nums = (1, 2, 3)
for num in nums:
    print(num)

str = 'Hello World!!'
for s in str:
    print(s)

members = {'ドメイン': '米田', 'パフェ': '鈴木'}
for member in members:
    print(members[member])
    print('{0}は{1}'.format(member, members[member]))

for member in members.values():
    print(member)

for k, v in members.items():
    print('{0}は{1}'.format(k, v))

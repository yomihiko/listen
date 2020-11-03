score = {}
science = score.get('science', 'ね')
print(science)
score['science'] = 50
science = score.get('science', 'ね')
print(science)
math = score.get('math')
print(math)
print(type(None))

m = {'ぐら': 'がう', '修羅': 'くぬい'}
n = {'あ': 'い'}
m.update(n)
print(m)
m.update({'あ': 'お'})
print(m)
d = m.pop('あ')
print(d)
print(m)
print('ぐら' in m)

print(m.keys())
print(m.values())
print(m.items())

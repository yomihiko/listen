mutable = {'list', 'dict', 'set'}
imutable = {'str', 'number', 'tuple'}
seq = {'list', 'tuple', 'str'}
print(mutable & seq)
print(3)
print(mutable | seq)
mutable.union(seq)
print(imutable - seq)
print(imutable.difference(seq))
print(mutable ^ seq)
print(mutable.symmetric_difference(seq))
print(mutable | seq - mutable & seq)

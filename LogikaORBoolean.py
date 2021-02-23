#not, or , and, xor

print('===not')
a = False
c = not a
print('hasil a : ', a)
print('hasil c : ', c)

print('==Or==')
a = False
b = False
c = a or b
print(a, 'or',b , ':' , c)

a = False
b = True
c = a or b
print(a, 'or',b , ':' , c)

a = True
b = False
c = a or b
print(a, 'or',b , ':' , c)

a = True
b = True
c = a or b
print(a, 'or',b , ':' , c)
print('=============End===============')
a = False
b = False
c = a and b
print(a, 'and',b , ':' , c)

a = False
b = True
c = a and b
print(a, 'and',b , ':' , c)

a = True
b = False
c = a and b
print(a, 'and',b , ':' , c)

a = True
b = True
c = a and b
print(a, 'and',b , ':' , c)
print('=============XOR===============')
a = False
b = False
c = a ^ b
print(a, 'XOR',b , ':' , c)

a = False
b = True
c = a ^ b
print(a, 'XOR',b , ':' , c)

a = True
b = False
c = a ^ b
print(a, 'XOR',b , ':' , c)
a = True
b = True
c = a ^ b
print(a, 'XOR',b , ':' , c)
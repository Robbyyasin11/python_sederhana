#assignment mempersingkat tandap operasi
# misal a = a+1 assigment -> a += 1
#langsung contoh soal aritmatika,bitwise

a = 6 # assignment
print('nilai a =', a)

a += 3 # artinya a = a+3
print('nilai a +=3 : ', a)

a -= 2 # artinya a = a-2
print('nilai a -=2 : ', a)

a *= 4 # artinya a = a*4
print('nilai a *=4 : ', a)

a /= 2 # artinya a = a*2
print('nilai a /=2 : ', a)

#modulus / sisa bagi [%]
b = 10
b %= 3
print('\nnilai b %=3 : ', b)
#floor devision / pembulatan hasil bagi [//] 
b = 10
b //= 2
print('nilai b //=2 : ', b)
#pangkat [**]
b = 4
b **= 2
print('nilai b **=2 : ', b)

print('\n')
#operasi bitwise
print(5*'=','operasi bitwise', 5*'=')
print(5*'=','OR', 5*'=')
c = True
print('nilai c :',c )
c |= False
print('nilai',c,'|= False : ',c)
c = False
print('nilai c :',c )
c |= False
print('nilai',c,'|= False : ',c)
#AND
print(5*'=','AND', 5*'=')
c = True
print('nilai c :',c )
c &= True
print('nilai',c,'&= True : ',c)
c = False
print('nilai c :',c )
c &= True
print('nilai',c,'&= True : ',c)
#XOR
print(5*'=','AND', 5*'=')
c = False
print('nilai c :',c )
c ^= True
print('nilai',c,'^= True : ',c)
c = True
print('nilai c :',c )
c ^= True
print('nilai',c,'^= True : ',c)
print('\n')
#perpindahan langkah
print(5*'=','perpindahan langkah', 5*'=')
print(5*'=','>>', 5*'=')
l = 0b0010
print('nilai l: ',l)
l >>= 1
print('nilai l >>= 1: ',format(l,'04b'))
print(5*'=','<<', 5*'=')
l <<= 2
print('nilai l <<= 2: ',format(l,'04b'))







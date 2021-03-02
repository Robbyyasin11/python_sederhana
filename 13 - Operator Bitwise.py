#Operator Bitwise , operator binar, binary

a = 9
b = 5
# Bitwise OR atau (|)
c = a | b 
print(2*"=","OR",2*"=")
print("nilai : ",a," , binary : ",format(a,"08b"))
print("nilai : ",b," , binary : ",format(b,"08b"))
print('------------------------------------- (|)')
print("nilai : ",c,", binary : ",format(c,"08b"))
#nilai a menjadi biner dengan penulisan 08b -> 0 u/spasi
# 8 jumlah index (mulai 0-7)
# b inisial binary
print('\n')
# Bitwise AND atau (&)
c = a & b 
print(2*"=","AND",2*"=")
print("nilai : ",a," , binary : ",format(a,"08b"))
print("nilai : ",b," , binary : ",format(b,"08b"))
print('------------------------------------- (&)')
print("nilai : ",c,", binary : ",format(c,"08b"))
print('\n')
# Bitwise XOR atau (^)
c = a ^ b 
print(2*"=","XOR",2*"=")
print("nilai : ",a," , binary : ",format(a,"08b"))
print("nilai : ",b," , binary : ",format(b,"08b"))
print('------------------------------------- (^)')
print("nilai : ",c,", binary : ",format(c,"08b"))
print('\n')

# Bitwise Not atau (~)
print(2*"=","NOT",2*"=")
c =  ~a 
print("nilai : ",a,", binary : ",format(c,"08b"))
print('------------------------------------- (~)')
print("nilai : ",c,", binary : ",format(c,"08b"))
print('------------------------------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai : ',d^e,'binary : ',format(d^e,"08b"))
print('\n')

#shifting : memindahkan/loncat sesuai jumlah lompatan/perpindahan
print(2*"=",">>[rigth]",2*"=")
l = int(input('input nilai lompatan (1-5) : '))
print('nilai shifting: ',l)
c = a >> l
print("nilai : ",a,", binary : ",format(a,"08b"))
print("nilai : ",c,", binary : ",format(c,"08b"))
print('\n')
print(2*"=","<<[left]",2*"=")
c = a << l
print("nilai : ",a,", binary : ",format(a,"08b"))
print("nilai : ",c,", binary : ",format(c,"08b"))
print('\n')




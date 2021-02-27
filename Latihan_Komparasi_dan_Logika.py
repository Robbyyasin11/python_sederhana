#soal
#  1. ----0+++++5-----8++++11----
#       0<x<5 || 8<x<11
#  2. +++0---5+++8---11+++
#       x<0 || 8<x>5 || x<11

print(5*"=","nomor 1",5*"=")
print(" 1. 0<x<5 || 8<x<11")

x = float(input("nilai x: "))
y = 0 < x < 5
z = 8 < x < 11
c = y or z
print("nilai 0 <",x,"< 5: ", y)
print("nilai 8 <",x,"< 11 : ", z)
print("hasil dari soal 1: ", c)
print(20*"=")

#---------------------------------------
#x<0 || 8<x>5 || x<11
print(5*"=","nomor 2",5*"=")
print("2. x<0 || 8<x>5 || x<11 ")
x = float(input("nilai x: "))
y = x < 0
z = 8 < x > 5
c = x < 11
v = y or z or c
print("nilai 0 > ",x ,": ", y )
print("nilai 8 < ",x ," > 5 : ", z )
print("nilai 11 > ",x ,": ", c )
print("hasil dari nomor 2 : " , v )
print(20*"=")


print(20*"=")




# 1. cara membuat strting

data = " ini adalah string"
print(data)
print(type(data))


#1. cara membaut string
'''
	1. dengan menggunanan single quote '...'
	2. dengan menggunakan double quete "..."

'''

data = 'Menggunakan single quote'
print (data)

data = "mengggunakan double quote"
print(data)


print('"halo, apa kabar ?"')
print("'halo, apa kabar ?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' Menjadi string

print('ini adalah hari jum\'at')
print('g\'day, ist\'t it ?')


# backlash \\ untuk menjadikan \ string
print("C:\\user\\Ucup")

#tab [\t\t\t] berfungsi dalam string
print ("ucup\t\t\tolong, semakin jauhan")

# backspace
print("ucup \botong")

#Newline
print("baris Pertama.\nbaris kedua.") # LF -> Line Feed -> Unix,macos,Linux
print("baris Pertama.\nbaris kedua.") # LF -> Line Feed -> commodare, acorn,lisp
print("baris Pertama.\r\nbaris kedua.") # CRLF -> line Feed carriage return -> dipakai oleh windows

# 3. string literal atau raw

#hati2
print('C:\\new folder') # akan salah pathnya

#menggunakan raw string
print(r'C:\new folder')
#multiline  literal string
print(
"""
Nama : Roby
Kelas: 3 SMP
"""
)

# multiline literal string dan RAW

print(
r"""
Nama : Roby
Kelas : 3 SMP
Website : www.roby.com\newID
"""
)



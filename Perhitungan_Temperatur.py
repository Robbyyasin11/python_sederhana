print ("\n program Konversi Temperatur\n")
print ("=============Celcius===============")
c = float(input('masukan suhu dalam celcius: '))
print("Suhu dalam ", c, "Celcius")
#reamur
r = (4/5)*c
print ("Suhu Reamur: ", r, "reamur")

#fahrenheit
f = ((4/5)*c)+32
print ("Suhu Reamur: ", f, "fahrenheit")

#Kelvin
k = c+273 
print ("Suhu Reamur: ", k, "kelvin")

print ("=============Fahrenheit===============")
f = float(input("Masukan Suhu dalam Fahrenheit: "))
print("Suhu dalam ", f, "Fahrenheit")

#celcius
c = (5/9)*(f-32)
print ("suhu Celcius : ",c, "celcius")

#Reamur
r = (4/9)*(f-32)
print ("suhu Celcius : ",r, "celcius")

#kelvin
k = ((5/9)*(f-32))+273
print ("suhu Celcius : ",k, "celcius")

print ("=============Kelvin===============")
k = float(input("Masukan Suhu dalam Kelvin: "))
print("Suhu dalam ", k, "Fahrenheit")

#celcius
c = k-273
print ("suhu Celcius : ",c, "celcius")

#Reamur
r = (4/5)*(k-273)
print ("suhu reamur : ",r, "reamur")

#Fahrenheit
f = ((9/5)*(k-273)) + 32
print ("suhu Fahrenheit : ",k, "Fahrenheit")


print("======is=========")
x = 5
y = 3
print("nilai x: ", x , "id x : ", hex(id(x)))
print("nilai y: ", y , "id y : ", hex(id(y)))
hasil = x is y
print("hasil: ", hasil)
#hex id digunakan untuk mendefinisikan id penyimpanan di memory
#bila sama nilai maka id di tmptkan yang sama
# is => perbandingan dengan nilai hex id bukan perbandingan nilai dari variabel[x or y] 
#yang menghasilkan true or false
print("======is not ========")
x = 5
y = 6
print("nilai x: ", x , "id x : ", hex(id(x)))
print("nilai y: ", y , "id y : ", hex(id(y)))
hasil = x is not y
print("hasil: ", hasil)
#hex id digunakan untuk mendefinisikan id penyimpanan di memory
#bila sama nilai maka id di tmptkan yang sama
# is not => perbandingan dengan nilai hex id bukan perbandingan nilai dari variabel[x or y] 
#yang menghasilkan true or false
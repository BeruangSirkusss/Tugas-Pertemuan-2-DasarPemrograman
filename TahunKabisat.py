tahun = int(input(" masukan tahun : "))

if tahun %4 == 0 :
    hasil = "kabisat"
else :
    hasil = "bukan kabisat"

print("tahun",tahun,"adalah",hasil)
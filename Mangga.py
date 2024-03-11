mangga = int(input(" masukan berapa kg : "))

if mangga <=2 :
    mangga = 20000 * mangga
elif mangga >2 and mangga <=5 :
    mangga = 18000 * mangga
elif mangga >5 :
    mangga = 16000 * mangga

print ("harga yang harus dibayar", mangga, "kg mangga")
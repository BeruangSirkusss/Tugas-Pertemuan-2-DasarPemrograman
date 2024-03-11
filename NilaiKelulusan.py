english =int(input(" masukan nilai anda english:"))
mtk =int (input(" Masukan Nilai MTK :"))
ipa =int (input(" Masukan Nilai IPA :"))
ips =int (input(" Masukan Nilai IPS :"))
indo =int (input(" Masukan Nilai B.INDO :"))

rata_rata = ( english + mtk + indo ) / 3
rata_rata_semua = (english +mtk +ipa + ips + indo) / 5

if rata_rata >= 75 :
    print (" Dia Lulus ")
elif rata_rata_semua >= 70:
    print(" Maka Dia Lulus ")
elif mtk > 90 and english > 90:
    print(" Maka Dia Lulus ")
else:
    print(" Maka Dia Tidak Lulus ")
umur = int(input(" Masukan Umur :"))

if umur <= 2 :
    panggilan = "Bayi"

elif umur >2 ^ umur <=5 :
    panggilan = "Balita"
    
elif umur >=5 ^ umur <=12 :
    panggilan = "Anak-anak"
    
elif umur >=12 ^ umur <=17 :
    panggilan = "Remaja"
    
elif umur >=17 ^ umur <=30 :
    panggilan = "Dewasa"
    
elif umur >30 :
    panggilan = "Orangtua"
    
print ("Umur",umur,"Tahun disebut",panggilan)
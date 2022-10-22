sayac=0
harf =0
plakaMi=True
harfvesonsayi = 0
plaka = input("lÜTFEN BİR PLAKA GİRİNİZ : ")
if(8<len(plaka)or 7>len(plaka)): #Plakanın uzunlugunu kontrol ettim.
    plakaMi=False
for i in range(len(plaka)): #Plakadaki sayi sayisini buldum ve sayaca attim
    if(plaka[i]=='1'or plaka[i]=='2'or plaka[i]=='3'or plaka[i]=='4'or plaka[i]=='5'or 
        plaka[i]=='6'or plaka[i]=='7'or plaka[i]=='8'or plaka[i]=='9'or plaka[i]=='0'):
        sayac=sayac +1
        
for i in range(len(plaka)-(sayac-2),len(plaka)): #Plakanin sonundaki sayilari kontrol ettim
    if(not(plaka[i]=='1'or plaka[i]=='2'or plaka[i]=='3'or plaka[i]=='4'or plaka[i]=='5'or 
        plaka[i]=='6'or plaka[i]=='7'or plaka[i]=='8'or plaka[i]=='9'or plaka[i]=='0')):
        plakaMi= False        
        
for i in range(2,len(plaka)-(sayac-2)): #Harfleri ascii tablosuna göre kontrol ettim
   harf= harf+1
   if(65>ord(plaka[i]) or ord(plaka[i])>90):
        plakaMi= False
        
if(81<int(plaka[0:2])or 0>int(plaka[0:2])): #Plakanin 82'den kucuk olup olmadıgına baktim
       plakaMi= False
       
if(plaka.islower()): #Plakanin harflerinin kucuk olup olmadıgını kontrol ettim.
    plakaMi=False
harfvesonsayi= harf+(sayac-2)   
if((6<harfvesonsayi or 5>harfvesonsayi)): #Plakadaki harf ve son sayilarin toplamı 6 veya 5 mi diye kontrol ettim
    plakaMi=False
    
if((harf>3 or harf<1)): #Harf sayisini kontrol ettim
    plakaMi=False
    
if(plakaMi==True): #Sonucu yazdirdim
    print("Girilen plaka geçerli.")
else:
    print("Girilen plaka geçersiz.")
    
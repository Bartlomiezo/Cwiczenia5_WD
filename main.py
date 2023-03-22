# #ZAD 1
# plik=open("liczby.txt", "w")
# for i in range(0,31):
#     i=i*2
#     plik.write(str(i)+", ")
# plik.close()
# #ZAD 2
# plik=open("liczby.txt", "r")
# liczby=plik.read()
# print(liczby)
# plik.close()
# #ZAD 3
# with open("liczby2.txt","w+") as plik2:
#     plik2.write("Litwo! Ojczyzno moja! Ty DDjesteś jak zdrowie. Nazywał się niedawno w wielkiej peruce, którą do ojca Podkomorzego,\nMościwego Pana zastępuje i bagnami skradał się dowie kto go myślano do dworu. Tu Kościuszko w polskiej szacie \n siedzi jak noga moja nie mogą. Słońce ostatnich nie czytano w Pańskim pisano zakonie i z Warszaw mam list, \n to mówiąc, że nasi synowie i wróciwszy w miechu. Starzy na to mówiąc, że go kaznodzieją, że zamczysko \nwzięliśmy w posiadłość. Wszakże kto cię stracił. Dziś człowieka rodu, obyczajów! Dość, że oko pańskie jachał \nszlachcic młody panek i już to mówiąc, że nasi synowie i nazwisko.\n")
#     plik2.seek(0)
#     for linia in plik2:
#         print(linia,end="")
#ZAD 4
# class NaZakupy:
#     def __init__(self,np,il,jm,cj):
#         self.nazwa_produktu=np
#         self.ilosc=il
#         self.jednostka_miary=jm
#         self.cena_jednostki=cj
#     def wyswietl_produkt(self):
#         return print(self.nazwa_produktu+", "+str(self.ilosc)+self.jednostka_miary+", "+str(self.cena_jednostki)+"zł/"+self.jednostka_miary)
#     def ile_produktu(self):
#         return print(str(self.ilosc)+self.jednostka_miary)
#     def ile_kosztuje(self):
#         return print(self.ilosc*self.cena_jednostki)
# ziemniak=NaZakupy("Ziemniak",2,"kg",2)
# print(ziemniak.ilosc)
# print(ziemniak.wyswietl_produkt())
# print(ziemniak.ile_produktu())
# print(ziemniak.ile_kosztuje())
#ZAD 5
class ciagArytmetyczny:
    atrybut=[]
    def pobierz_elementy(self,wartosc):
        self.atrybut.extend(wartosc)
    def pobierz_parametry(self,pierwsza_wartosc,roznica,n):
        for i in n:
            
    def wyswietl_dane(self):
        print(self.atrybut)
ciag=ciagArytmetyczny()
ciag.pobierz_elementy([1,2,3,4])
print(ciag.wyswietl_dane())
# #ZAD 6
# class Robaczek:
#     def __init__(self,x,y,krok):
#         self.x=x
#         self.y=y
#         self.krok=krok
#     def idz_w_gore(self, ile_krokow):
#         self.y=self.y+(self.krok*ile_krokow)
#     def idz_w_dol(self,ile_krokow):
#         self.y=self.y-(self.krok*ile_krokow)
#     def idz_w_lewo(self,ile_krokow):
#         self.x = self.x - (self.krok * ile_krokow)
#     def idz_w_prawo(self,ile_krokow):
#         self.x = self.x + (self.krok * ile_krokow)
#     def pokaz_gdzie_jestes(self):
#         return print(str(self.x)+","+str(self.y))
# robak=Robaczek(0,0,2)
# robak.idz_w_gore(2)
# print(robak.pokaz_gdzie_jestes())
# robak.idz_w_dol(1)
# print(robak.pokaz_gdzie_jestes())
# robak.idz_w_prawo(2)
# print(robak.pokaz_gdzie_jestes())
# robak.idz_w_lewo(1)
# print(robak.pokaz_gdzie_jestes())

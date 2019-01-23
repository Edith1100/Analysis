
#Zbudowaæ ramkê (data frame) zawieraj¹c¹ dane pracowników: id, imiê, nazwisko, wiek, sta¿ pracy,
#stanowisko, miasto, pensja. Wype³niæ ramkê danymi, w taki sposób, aby poni¿sze zapytania dawa³y
#sensowne wyniki (tzn. na tyle du¿o ró¿nych wartoœci aby powsta³y zestawienia i wykresy zawieraj¹ce
#po kilka elementów).
#a) Wyszukaæ tych pracowników z Warszawy, który zarabiaj¹ co najmniej 6000 z³ (wyœwietliæ
#listê: imiê, nazwisko, stanowisko)
#b) Obliczyæ sumê zarobków pracowników z Wroc³awia
#c) Obliczyæ œredni¹ wysokoœæ pensji na stanowisku „Programista”
#d) ZnaleŸæ najtañszego pracownika z Poznania
#e) Zrobiæ wykres ko³owy zarobków pracowników z Opola#



imie<-c("Anna","Alina","Agata","Amelia","Adrianna","Barbara","Bogumi³a","Bernadeta","Celina","Dagmara","Dominika","Edyta","Ewa","El¿bieta","Eryka","Halina","Helena","Izabela","Janina","Julia","Kamila","Klara","Klaudia","Krystyna","Karolina","Katarzyna","Magda","Monika","Marta","Michalina","Mieczys³awa","Natalia","Natasza","Nadia","Oksana","Patrycja","Pola","Paulina","Tamara","Tatiana")
nazwisko<-c("Barwiñska","Krysiñska","Gutkowska","Szczodrowska","Grzyma³a","Frej","Niemyjska","Szkutnik","Orliñska","Komor","Sasin","Szwarc","Zub","Wolañska","Dr¹¿kiewicz","Niewiadomska","Deka","Stachyra","Skrodzka","Tworkowska","Roszczyk","Olech","Smo³a","Biela","Kasztelan","Pucha³a","Miller","Fila","W¹sik","£ukawska","Matyja","Sikorska","£awniczak","Bochen","Serwatka","Tracz","Kruszyna","Kraœnicka","P³uciennik","Œwiêtek")
wiek<-c(23,25,27,29,23,25,26,24,25,25,26,29,28,30,32,31,30,33,32,33,35,36,38,45,42,41,46,42,25,26,28,23,30,31,33,36,38,40,38,37)
staz_pracy<-c(1,2,3,3,1,2,2,1,2,2,3,6,4,5,6,8,5,2,6,3,4,4,3,10,10,11,15,20,1,2,2,3,3,2,3,5,6,6,6,7)
stanowisko<-c("kasjer","sprzedawca","kosmetyczka","geodeta","archeolog","aktor","programista","programista","programista","sprzedawca","sprzedawca","programista","tester","tester","programista","programista","analityk","lekarz","analityk","lekarz","programista","programista","aktor","lekarz","programista","ogrodnik","dentysta","weterynarz","architekt","rolnik","dietetyk","analityk","aktor","stewardessa","stewardessa","weterynarz","dietetyk","analityk","weterynarz","architekt")
miasto<-c("Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw","Warszawa","Poznañ","Opole","Wroc³aw")
pensja<-c(1800,1850,2800,2900,1500,2500,3200,3500,4500,2200,1600,7500,6500,5500,5000,12000,8000,4500,4500,7500,9500,6500,3500,16000,22000,3500,15000,15000,15200,3600,3200,5000,5500,2800,2800,4500,5800,5000,4000,9500)

dane_pracownikow<- data.frame(imie,nazwisko,wiek,staz_pracy,stanowisko,miasto,pensja)
dane2<- subset(dane_pracownikow, subset= pensja > 6000 & miasto == "Warszawa" )
dane2

#Wyœwietlenie pracowników z Warszawy, którzy zarabiaj¹ co najmniej 6000z³
dane2[,c("imie","nazwisko","stanowisko")]

#Obliczenie sumy zarobków pracowników z Wroc³awia
sum(dane_pracownikow[which(dane_pracownikow[,6]=="Wroc³aw"),7])

#Obliczyæ œredni¹ wysokoœæ pensji na stanowisku „Programista” 
mean(dane_pracownikow[which(dane_pracownikow[,5]=="programista"),7])

#ZnaleŸæ najtañszego pracownika z Poznania 
min(dane_pracownikow[which(dane_pracownikow[,6]=="Poznañ"),7])          

#Zrobiæ wykres ko³owy zarobków pracowników z Opola 
pracownicy_Opole = subset(dane_pracownikow, subset = miasto == "Opole")
pie(pracownicy_Opole[,"pensja"] ,row.names(pracownicy_Opole))


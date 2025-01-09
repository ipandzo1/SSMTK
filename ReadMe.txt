# SSMTK - Projekat TEMA 1: Razvoj aplikacije za prikupljanje metrika iz eksperimentalne 5G mreže za prenos podataka

## Postavka zadatka: 
• Realizirati mrežu za prenos podataka sačinjenu od korisničkih uređaja baziranih na
Raspberry Pi računaru sa 5G komunikacijskim modulom i eksperimentalne 5G bazne
stanice. 
• Implementirati aplikaciju za prikupljanje metrika kao što su CQI, SNR, RSRP, RSRQ i
drugih dostupnih sa eksperimentalne 5G bazne stanice putem Remote API-ja. Prikupljene
vrijednosti metrika je potrebno spremati u CSV datoteku tako da svaki red predstavlja jedno
mjerenje, a sadrži vremenski trenutak mjerenja, oznaku (ID) uređaja za koji je vezano
mjerenje, te sve raspoložive metrike. 
• Implementirati aplikaciju za prikupljanje raspoloživih metrika sa 5G komunikacijskog
modula na Raspberry Pi računaru. Prikupljene vrijednosti metrika je potrebno spremati u
CSV datoteku. 
• Izvršiti testiranje usluge prenosa podataka između korisničkog uređaja i bazne stanice uz
prikupljanje metrika. Analizirati mjerenja metrika sa bazne stanice i korisničkog uređaja, te
utvrditi na koji način su korelisana. 
• Uvesti u eksperimentalnu 5G mrežu dodatne korisničke uređaje (5G modemi, mobiteli i sl.),
te izvršiti testiranje usluge prenosa podataka uz prikupljanje metrika za različit broj aktivnih
korisničkih uređaja.

#Izrada:
1. Realizirati mrežu za prenos podataka sačinjenu od korisničkih uređaja baziranih na
Raspberry Pi računaru sa 5G komunikacijskim modulom i eksperimentalne 5G bazne
stanice. 

Realizovana je mreža sačinjena od uređaja: Raspberry Pi računara sa 5G komunikacijskim modulom,
5G bazne stanice AMARISOFT CallBox Classic i ZYXEL modela NR5101 - 5G New Radio Gateway. 
Putem Raspberry Pi računara povezali smo se na mrežu koju je pružila 5G bazna stanica. 
Laptop je povezan na mrežu koju je omogućio ZYXEL 5G New Radio, koji je spojen na 
baznu stanicu i vrši konverziju 5G signala bazne stanice u WiFi signal.


2. Implementirati aplikaciju za prikupljanje metrika kao što su CQI, SNR, RSRP, RSRQ i
drugih dostupnih sa eksperimentalne 5G bazne stanice putem Remote API-ja. Prikupljene
vrijednosti metrika je potrebno spremati u CSV datoteku tako da svaki red predstavlja jedno
mjerenje, a sadrži vremenski trenutak mjerenja, oznaku (ID) uređaja za koji je vezano
mjerenje, te sve raspoložive metrike.


Napravljena je skripta koja putem Remote API-ja prikuplja podatke sa bazne stanice o kvaliteti signala.
Implementacija skripte je u toku, trenutno smo prikupili podatke o CQI i dodatne, a u toku je analiza za preostale.

3. Implementirati aplikaciju za prikupljanje raspoloživih metrika sa 5G komunikacijskog
modula na Raspberry Pi računaru. Prikupljene vrijednosti metrika je potrebno spremati u
CSV datoteku. 


Implementirana je skripta qeng.py za prikupljanja metrika sa 5G modula na Rasberry Pi računara.
Korištene su komande iz dokumentacije 5G modula u upotrebi Quectl RG500Q-GL.
Skripta je kreirala traženu CSV datoteku metrics.csv koja je prethodno opisana.


Preostale stavke će biti urađene u nastavku izrade projektnog zadatka.



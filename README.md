# TEMA 1: Razvoj aplikacije za prikupljanje metrika iz eksperimentalne 5G mreže za prenos podataka

## Postavka zadatka

- Realizirati mrežu za prenos podataka sačinjenu od korisničkih uređaja baziranih na Raspberry Pi računaru sa 5G komunikacijskim modulom i eksperimentalne 5G bazne stanice.
- Implementirati aplikaciju za prikupljanje metrika kao što su CQI, SNR, RSRP, RSRQ i drugih dostupnih sa eksperimentalne 5G bazne stanice putem Remote API-ja. Prikupljene vrijednosti metrika je potrebno spremati u CSV datoteku tako da svaki red predstavlja jedno mjerenje, a sadrži vremenski trenutak mjerenja, oznaku (ID) uređaja za koji je vezano mjerenje, te sve raspoložive metrike.
- Implementirati aplikaciju za prikupljanje raspoloživih metrika sa 5G komunikacijskog modula na Raspberry Pi računaru. Prikupljene vrijednosti metrika je potrebno spremati u CSV datoteku.
- Izvršiti testiranje usluge prenosa podataka između korisničkog uređaja i bazne stanice uz prikupljanje metrika. Analizirati mjerenja metrika sa bazne stanice i korisničkog uređaja, te utvrditi na koji način su korelisana.
- Uvesti u eksperimentalnu 5G mrežu dodatne korisničke uređaje (5G modemi, mobiteli i sl.), te izvršiti testiranje usluge prenosa podataka uz prikupljanje metrika za različit broj aktivnih korisničkih uređaja.

## Korišteni uređaji

### Raspberry Pi računar 
Raspberry Pi je računarski uređaj zasnovan na ARM procesoru. Ističe se zbog svoje fleksibilnosti i niske cijene, te dolazi u različitim modelima sa različitim specifikacijama. Njegov operativni sistem je Raspberry Pi OS (Linux varijanta). Popularan je u IoT projektima zbog svojih kompaktnih dimenzija, te  mogućnosti povezivanja sa senzorima i drugim uređajima sa kojih može vršiti prikupljanje metrika. Moguće povezivanje: Ethernet, Wi-Fi, Bluetooth, USB portovi. U našem projektnom zadatku, Raspberry Pi vrši prikupljanje metrika sa 5G komunikacijskog modula. 

### 5G komunikacijski modul - ZYXEL model NR5101 5G New Radio Gateway
ZYXEL NR5101 je 5G New Radio Gateway dizajniran za pružanje visokih brzina prenosa podataka i stabilne 5G veze za različite aplikacije. Ovaj uređaj omogućava povezivanje s 5G mrežom i koristi se kao komunikacijski modul u eksperimentalnim 5G mrežama. U projektnom zadatku, ovaj modul omogućava povezivanje Raspberry Pi s eksperimentalnom 5G baznom stanicom, čime se omogućava prenos podataka i prikupljanje metrika. 

### Eksperimentalna 5G bazna stanica

## Izrada

### 1. Realizacija mreže za prenos podataka

Realizovana je mreža sačinjena od uređaja: Raspberry Pi računara sa 5G komunikacijskim modulom, 5G bazne stanice AMARISOFT CallBox Classic i ZYXEL modela NR5101 - 5G New Radio Gateway. Putem Raspberry Pi računara povezali smo se na mrežu koju je pružila 5G bazna stanica. Laptop je povezan na mrežu koju je omogućio ZYXEL 5G New Radio, koji je spojen na baznu stanicu i vrši konverziju 5G signala bazne stanice u WiFi signal.

### 2. Implementacija aplikacije za prikupljanje metrika sa bazne stanice

Napravljena je skripta koja putem Remote API-ja prikuplja podatke sa bazne stanice o kvaliteti signala. Implementacija skripte je u toku, trenutno smo prikupili podatke o CQI i dodatne, a u toku je analiza za preostale.

### 3. Implementacija aplikacije za prikupljanje metrika sa 5G komunikacijskog modula

Implementirana je skripta `qeng.py` za prikupljanje metrika sa 5G modula na Raspberry Pi računaru. Korištene su komande iz dokumentacije 5G modula u upotrebi Quectl RG500Q-GL. Skripta je kreirala traženu CSV datoteku `metrics.csv` koja je prethodno opisana.

Preostale stavke će biti urađene u nastavku izrade projektnog zadatka.

## Literatura

[1] https://tech-academy.amarisoft.com/RemoteAPI_Python.html?fbclid=IwY2xjawHxBRtleHRuA2FlbQIxMAABHfwqKmdrzcyIm2S0pP-jU3k3pf9CRtq1mfuVHuCnKGYWykr4CxvXI8yRIQ_aem_Zl0GhSs5jDZUbE-Zr8OORw
[2] https://www.raspberrypi.com/
[3] https://www.zyxel.com/global/en/home

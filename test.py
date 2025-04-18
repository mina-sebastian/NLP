import roner
from unidecode import unidecode
ner = roner.NER()



input_texts = ['''
Vile şi terenuri în ţară şi străinătate, bijuterii, tablouri, ceasuri de lux, conturi la bănci din România sau din afară, venituri mari din activităţi de consultanţă se regăsesc în declaraţiile de avere depuse de cei 11 candidaţi la alegerile prezidenţiale din luna mai, transmite Agerpres.

Spre deosebire de alegerile precedente, candidaţii independenţi „conduc” în faţa celor „de partid” în privinţa averilor.

Astfel, la capitolul proprietăţi iese în evidenţă omul de afaceri româno-american John-Ion Banu-Muscel cu vile şi apartamente în România şi Statele Unite ale Americii, 74 hectare de teren în ţară, dar şi o fermă în America, pe o suprafaţă de 135 de hectare.

El este urmat de Victor Ponta – trei apartamente în Bucureşti, Istanbul şi Emiratele Arabe Unite şi de Daniel Funeriu – două apartamente în România, o casă în Germania şi 50 de hectare de teren în Timiş.

Când vine vorba de venituri, tot independenţii se situează în top, urmaţi de candidaţii susţinuţi de partidele „mici”: John-Ion Banu-Muscel – peste 300.000 de dolari, Daniel Funeriu – peste 150.000 de euro (în principal din activităţi de consultanţă), Cristian Terheş – 99.000 de euro, Lavinia Şandru – peste 300.000 lei (mai ales drepturi de autor).

În schimb, primii clasaţi în sondaje nu stau atât de bine la avere.

Crin Antonescu nu are venituri, soţia lui având numeroase proprietăţi şi sute de mii de euro în conturi. Nicuşor Dan stă cu chirie, dar are un teren valoros la Predeal. George Simion nu are niciun fel de proprietăţi şi se bazează pe salariul de parlamentar şi darurile primite la botezul copilului, în timp ce Elena Lasconi are credite de returnat la bănci.

Prezentăm averile celor 11 candidaţi la alegerile prezidenţiale din luna mai, în ordinea prezentată de pe site-ul Biroului Electoral Central:

*** NICUŞOR DAN

Actualul primar general al Capitalei deţine un teren de 7.460 mp la Predeal, cumpărat în anul 2007, dar locuieşte în Bucureşti cu chirie. Mai deţine o maşină veche din anul 1986, marca Citroen, un cont bancar cu suma de 439.000 lei şi a acordat unei persoane un împrumut de 20.000 de euro.

În schimb, Nicuşor Dan a contractat trei împrumuturi bancare în sumă totală de 152.000 de euro.

În declaraţia de avere, el a menţionat şi donaţii primite de la zeci de persoane pentru susţinerea campaniei electorale, în sumă totală de aproximativ 1,2 milioane lei, la care se adaugă 659.000 lei primiţi de la Autoritatea Electorală Permanentă, reprezentând rambursarea cheltuielilor efectuate în campania pentru alegerile locale din 2024.

La capitolul venituri, Nicuşor Dan a trecut venitul încasat anul trecut pentru funcţia de primar al Capitalei – 296.000 lei.

*** CRIN ANTONESCU

Candidatul Alianţei România Înainte (PSD – PNL – UDMR) a trecut în declaraţia de avere două apartamente în Bucureşti (96 mp şi 205 mp) şi un loc de parcare (31 mp), alte două case în judeţul Prahova (84 mp şi 43 mp), la care se adaugă trei terenuri în judeţul Prahova (3.942 mp, 250 mp şi 713 mp), însă doar apartamentul de 96 mp este al lui, restul fiind ale soţiei, Adina Vălean, sau deţinute împreună.

Familia mai are trei autoturisme (BMW, Mercedes, Kia), iar Adina Vălean o colecţie de bijuterii – evaluată la 18.000 de euro, dar şi conturi în bănci din România şi Belgia, cu aproximativ 335.000 de euro şi titluri de stat în valoare de 98.000 de euro.

În ultimul an, Crin Antonescu nu a avut niciun venit, însă Adina Vălean a încasat sume consistente ca fost comisar european (153.000 euro) şi europarlamentar (46.000 de euro), plus 20.000 de euro (diurne), 15.000 de euro (misiuni).

*** VICTOR PONTA

Fost premier şi lider al PSD, Victor Ponta candidează la alegerile prezidenţiale din postura de independent. Deţine un apartament în Bucureşti (95 mp), un apartament cumpărat în anul 2021 la Istanbul – Turcia (200 mp) şi altul achiziţionat în 2022 în Emiratele Arabe Unite (82 mp), un autoturism marca Smart, dar şi ceasuri în valoare de 20.000 de euro dobândite în perioada 2023 – 2024.

Ponta are mai multe conturi bancare, cu aproximativ 130.000 de euro şi a acordat organizaţiei PSD Dâmboviţa un împrumut de 190.000 lei (38.000 euro).

La capitolul venituri, el a trecut un salariu de 240.000 lei încasat de la Camera de Comerţ (fără să menţioneze funcţia pe care a avut-o) şi un salariu de 19.295 lei, fără să spună entitatea de la care a primit aceşti bani, cel mai probabil din consultanţă, el deţinând firma SC VP Projects Advisers SRL (conform declaraţiei de interese).

*** ELENA LASCONI

În declaraţia de avere Elena Lasconi a menţionat şapte terenuri (două agricole – 57.500 mp, un teren forestier – 2.500 mp, trei terenuri intravilan – 6.700 mp şi un teren extravilan de 500 mp), trei apartamente (65 mp, 70 mp, 58 mp), o casă de locuit de 98 mp, dar şi un autoturism marca Opel fabricat în anul 2007.

Lasconi are de returnat două împrumuturi bancare de peste 388.000 de lei.

La capitolul venituri, Elena Lasconi a precizat salariul încasat ca primar al municipiului Câmpulung – 141.000 lei, iar soţul a câştigat în ultimul an fiscal 82.000 de lei, fiind consilier la Camera Deputaţilor.

*** CRISTIAN TERHEŞ

În prezent europarlamentar, Cristian Terheş a menţionat în declaraţia de avere cinci terenuri intravilan situate în judeţele Sălaj şi Bihor, trei apartamente (53 mp, 81 mp şi 53 mp), două autoturisme (Toyota Camry şi Mitsubishi Eclipse Cross), şase conturi bancare ale lui (aproximativ 560.000 lei şi 50.000 de euro) şi şase ale soţiei (90.000 de dolari), o parte fiind deschise la bănci în statul american California.

Terheş a acordat patru împrumuturi Partidului Naţional Conservator Român, cu o valoare cumulată de 220.000 lei, 45.000 euro şi 95.000 USD, menţionând şi hârtii de valoare deţinute de soţie la Treasury Direct – 50.000 dolari.

La capitolul venituri, Cristian Terheş a declarat un salariu anual de la Parlamentul European în valoare de 99.000 de euro, iar soţia are un salariu anual de 50.000 de dolari ca „AR and compliance manager” la compania General Orthocare, Irvine, California, SUA.

*** LAVINIA ŞANDRU

Deputată PD în perioada 2004 – 2008 pe vremea mandatului lui Traian Băsescu, fosta soţie a lui Darius Vâlcov candidează din partea Partidului Umanist Social Liberal, fondat de Dan Voiculescu.

În declaraţia de avere, Lavinia Şandru a menţionat un apartament în Bucureşti (98 mp), două autoturisme (Jeep şi Skoda), bijuterii şi obiecte de artă în valoare de 12.000 euro, mai multe conturi bancare cu aproximativ 41.000 euro şi 700.000 lei, plus 90.000 euro plasaţi într-un fond de investiţii. La acestea se adaugă titluri de stat „tezaur” în valoare de peste un milion de lei şi titluri de stat „Fidelis” – 100.000 de euro.

La capitolul venituri, Lavinia Şandru a trecut în declaraţia de avere sume importante: 165.000 lei – drepturi de autor de la Antena 3, 24.000 lei – drepturi de autor la Teatrul Naţional „Mihai Eminescu” Timişoara, 12.690 lei – drepturi de autor şi 10.716 lei – salariu restant ca preşedinte la Iniţiativa Ecologistă Europeană, 10.000 lei – drepturi de autor de la Tonique Entertaiment Bucureşti, 55.000 lei – drepturi de autor şi 26.616 lei – salariu pentru funcţia de director general la Stratcom Media & Film Bucureşti, 10.000 lei – drepturi de autor de la firma Movingframe SRL.

De asemenea, ea a primit 114.430 lei – dividende de la Stratcom Media & Film şi 99.504 lei de la Movingframe SRL.

*** GEORGE SIMION

Liderul AUR nu are proprietăţi, menţionând în declaraţia de avere doar suma de 60.000 de euro primită la petrecerea de botez organizată în oraşul Gura Humorului, judeţul Suceava, precum şi o donaţie primită de la o persoană, pentru campania electorală, în valoare de 50.000 de euro.

Anul trecut, a deschis un cont bancar unde are 250.000 de lei. A încasat de la Camera Deputaţilor un salariu de aproape 137.000 lei, în timp ce soţia a beneficiat până acum de o indemnizaţie pentru creşterea copilului în cuantum de 15.000 lei, iar anterior a primit un salariu de 8.000 lei de la Ministerul Educaţiei.

*** JOHN-ION BANU-MUSCEL

Banu-Muscel se prezintă ca om de afaceri româno-american şi candidează independent la alegerile prezidenţiale. Potrivit declaraţiei de avere, are în proprietate un apartament în Bucureşti (80 mp) şi în Florida – SUA (110 mp), o casă de 380 metri pătraţi în oraşul McCormick din statul american Carolina de Sud şi o altă casă de 410 mp în Florida, la care se adaugă patru terenuri: 15 hectare intravilan – judeţul Giurgiu, 9 hectare pădure în judeţul Argeş, o păşune de 135 hectare în McCormick şi 50 hectare intravilan în Argeş.

Deţine trei autoturisme (BMW, Porsche şi Deer), un tablou evaluat la 30.000 de dolari şi o colecţie de statuete şi obiecte din bronz evaluate la 25.000 de dolari.

John-Ion Banu-Muscel are în conturi bancare aproximativ 400.000 de dolari şi 300.000 de lei, dar şi active financiare în SUA de 248.000 dolari.

La capitolul venituri, Banu-Muscel a avut în ultimul an un salariu de 75.000 dolari ca manager la compania Ocean Test şi 180.000 de dolari în calitate de doctor.

În plus, el beneficiază de o pensie anuală în SUA de 21.000 dolari şi a încasat 48.000 dolari de la o fermă pe care o are în oraşul McCormick.

*** SILVIU PREDOIU

Fost director adjunct şi director interimar al Serviciului de Informaţii Externe până în anul 2018, Silviu Predoiu candidează din partea Partidului Liga Acţiunii Naţionale. Are în proprietate două apartamente în Bucureşti (73 mp şi 77 mp) şi o casă de vacanţă cu o suprafaţă de 115 mp, două terenuri intravilan (14 mp şi 1.162 mp) şi 5 hectare de teren agricol în judeţul Constanţa.

El mai deţine două autoturisme (Mazda CX5 şi Fiat 850), ceasuri în valoare de 7.000 de euro şi şapte conturi bancare cu 100.000 lei, 35.000 euro şi 20.000 dolari.

La capitolul venituri, Silviu Predoiu a menţionat o pensie de serviciu de 260.000 lei (Casa de pensii a MApN), iar soţia o pensie de serviciu de 100.800 lei (Casa de pensii a SRI).

*** DANIEL FUNERIU

Fost ministru al Educaţiei în Guvernul Emil Boc, Daniel Funeriu candidează ca independent. Deţine două apartamente în Timişoara (124 mp şi 55 mp) şi o casă în Germania (230 mp) cu o curte de 838 mp, dar şi două terenuri agricole în judeţul Timiş de mari dimensiuni – 30,5 hectare şi 19,5 hectare.

Funeriu mai are cinci maşini (Jaguar XJ6, Jaguar S, Mazda CX5, Audi A6 şi Renault Twingo), o colecţie de bijuterii evaluată la 15.000 de euro, conturi bancare, depozite şi fonduri de investiţii de aproximativ 360.000 de euro şi 1,3 milioane yeni.

În ultimul an a raportat venituri importante: 138.000 euro – consultanţă la compania GOPA Pace, 56.000 lei de la Universitatea Bucureşti, 20.000 lei – consultanţă la Infomart, 8.700 euro – consultanţă la Oriensys, plus 25.000 lei reprezentând arendă pământ, în timp ce soţia lui a avut un salariu de 7.000 euro de la UMC.

*** SEBASTIAN CONSTANTIN POPESCU

Candidează pentru a doua oară la alegerile prezidenţiale, din partea Partidului Noua Românie. În declaraţia de avere nu a menţionat niciun venit în ultimul an, în schimb are o casă de 78 mp în localitatea Făureşti (judeţul Vâlcea), un teren intravilan de 2.426 mp şi alte 13 terenuri agricole în aceeaşi comună, având o suprafaţă cumulată de peste 18.000 mp, la rubrica „mod de dobândire” fiind menţionat „contract de întreţinere”.
''']

mapped_texts = list(map(unidecode, input_texts))

output_texts = ner(mapped_texts)

for output_text in output_texts:
  print(f"Original text: {output_text['text']}")
  for word in output_text['words']:
    if word['tag'] != 'O':
        print(f"{word['text']:>20} = {word['tag']}")
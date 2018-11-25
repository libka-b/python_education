
# Dedicnost a polymorfismus

### 1. ukol
Toto zadani bude pouze zahrivaci :) takze pouziju jeden z tradicnich prikladu z fitu :)

Rekl jsem si, ze chci evidovat pocet dopravnich prostredku ktere vjedou do nasi firemni
garaze a protoze chci evidovat pocet dopravnich prostredku, pocet motorovy, nemotorovych a 
nasledne i pocet jednotlivych kusu, tak jsem se rozhodl si na to napsat program :)

Mejme tridu `Garage` ktera prijima do metody `__init__` 2 parametry: `motorized`
 a `non_motorized`. Tyto hodnoty reprezentuji pocet mist pro motorizovana a nemotorizovana
 vozidla. 
 
Dale trida `Garage` ma 3 metody: `add_to_garage`, `leave_garage` a `list_garage`.
Metody add a leave prijimaji jako parametr instanci (ne)motoroveho vozidla, 
ktere chcete pridat/odebrat z/do garaze. Metoda `list_garage` vypise v nejakem rozumnem formatu
vse co v garazi mate.

Dale potrebujeme implementovat (ne)motorova vozidla.
Ra bych, aby jste implementovali obecnou tridu `Vehicle` z ni vydedily 2 tridy: 
`Motorized` a `NonMotorized`. Z kazde pak chci aby jste vydedili alespon 2 tridy,
takze (`Car` a `Bus`)  a   (`Bicycle` a `Scooter`).
Urcite dokazete vymyslet vice dopravnich prostredku, takze si klidne nejake pridejte. 
Najdete spolecne prvky vsech trid a zkuste je naimplementovat podle informaci o kterych
jsme mluvili - pokuste se aby co nejvice spolecnych veci probublalo nahoru. Cim nize, tim
konkretneji.

### 2. ukol 
Tento ukol se zameri predevsim na vicenasobnou dedicnost. 
Dost casto se ve spojeni s timto tematem setkate s vyrazem **Mixins** (Mixiny).
Mixiny jsou jisty druh navrhoveho vzoru, ktery je nutno pouzivot s opatrnosti a velkou
rozvahou. Je velice jednoduche timto navhrem kod zneprehlednit a prodlouzit.

Predstavme si jednoduchy priklad, byli jste zvoleni do poslanecke snemovny. To znamena, ze
jste `BasePoslanec`, jako BasePoslanec umite nekolik zakladnich veci, ktere musi zvladat kazdy poslanec
umite zvanit o nicem, prijimat plat a zvedat ruce pri hlasovani. Ale kde ted pouzit vicenasobnout dedicnost(Mixiny)?

Kazdy poslanec muze ziskat dalsi penize a pravomoce, kdyz se prihlasi ido nejake vyboru, delegace nebo komise. 
Neni moc dulezite, co tyto komise delaji, ale zvednou vam plat, dovoli vam zvanit o vice vecech a muzete hlasovat
o vecech o kterych BasePoslanec ne :) [Vybory, komise a delegace](https://www.psp.cz/sqw/organy.sqw), zde najdete
seznam vsech moznych vyboru atd, pro inspiraci, nicmene nemusite se bat, pokud vas zadny nezaujme, tak nejaky vybor
vymyslete. U vyboru je dulezite, aby mel dlouhy a nic nerikajici nazev napr. **Stálá delegace Parlamentu do Parlamentního 
shromáždění Organizace pro bezpečnost a spolupráci v Evropě**, pak to vypada dulezite a vsichni se boji zeptat, 
co to vlastne delate :)

Abychom si to rekli programatorsky: Vytvorte tridu `BasePoslanec` a pomoci vicenasobne dedicnosti rozsirte jeho 
moznosti, schopnosti a plat. Takze bude dedit(prijimat pravomoce) z nekolika vyboru atd :)


#Funkce pythonu

## Zapis funkce
Funkci v pythonu definuje klicove slovo def:
```python
def nazev_funkce(arg1, arg2, arg3):
    telo_funkce
```

## Argumenty
Kazda funkce muze, ale nemusi prijimat argumenty. Rozlisujeme 2 druhy argumentu

**1. Pozicni argumenty**

nejjednodussi zadavani parametru, ZALEZI na poradi zadanych argumenty,
takze v pripade takovehoto volani funkce:
```python
def foo(a, b, c):
    print(a ,b ,c)
foo(1, 2, 3)
```
bude v a == 1, b == 2 a c == 3

**2. Klicove argumenty**
Tyto argumenty zadavame ve formatu **jmeno=hodnota** . Hned si to ukazeme v nasledujicim kodu,
vcetne nekolika volani teto funkce:
```python
def foo(a, b, c=-1, d=-2):
    print(a, b, c, d)

foo(1, 2)
foo(1, 2, 3)
foo(1, 2, 3, 4)
foo(1, 2, c=5)
foo(1, 2, c=6, d=7)
foo(1, 2, d=7, c=6)

# vsechna tato volani jsou v poradku
# co nejake spatne??
foo(c=1, d=2, 1, 2)
```
Vsechna volani, krome posledniho, jsou v poradku? Proc je posledni spatne?

NIKDY nesmi byt klicove argumenty psany PRED pozicnimi. Schvalne si vyzkousejte
par takovych zapisu, at vite jak to funguje.

Dokazete prijit na vyhody klicovych argumentu?

Predstavte si funkci, ktera prijima velke mnozstvi parametru, ale ne vsechny jsou povinne.
Je logicke, ze nebudete vyplnovat vsechny a nechate jim defaultni hodnoty, ktere jsou za rovnitkem.

## Argumenty II

Dalsi druhy argumenty jsou "sberne" a oznacuji se * nebo ** .

***args** - tyto argumenty slouzi pro sber n-tic jejichz delka neni predem urcena, nebo-li
pro sber pozicnich argumenty

**\*\*kwargs** - tyto argumenty slouzi pro sber parovych(slovnikovych) hodnot,
nebo-li klicovych argumentu.

Hned si ukazeme nekolik ukazkovych kodu a vysvetlime si na nich funkci techto argumentu.
Zacneme s *args:

```python
def foo(*args):
    print(args)
    print(*args)
    
def foo2(a, b, c, d):
    print(a, b, c, d)
    
foo(1, 2, 3, 4)

some_list = (1, 2, 3, 4)

foo2(*some_list)
```

Nez budete cist dal, tak si schvalne zkuste tento kod spustit a urcit, PROC a JAK funguje.

**BACHA SPOJLER**

zacneme s funkci foo(*args). Tuto funkci jsem volal s nekolika pozicnima argumentama. Argumenty
se vezmou, zabali se do **tuple** (nemenitelny list) a predaji se funkci foo.
Kdyz nasledni vypisuji args, tak se mi vypise toto pole jako celek, ALE jakmile zkousim vypsat
*args, tak se toto pole vezme, ROZBALI se a posle se funkci print. Takze je to stejne, jako
kdybychom volali print(1, 2, 3, 4)

U funkce foo2(a, b, c, d), jsme na to sli obracene. Prvni jsme si vytvorili tuple some_list,
a tu jsme s * predali funkci foo2. Co se stalo? * nam toto pole vybalila a po jednom jeho prvky
naskladala na jednotlive pozicni argumenty a, b, c, d. POZOR, pokud by nesedel, pocet prvku
v poli, tak by program skoncil s chybou. 3 prvky nedokazete naparovat na 4 atd.
Vrele vam doporucuji nekolik jednoduchych pokusu s temito argumenty, at je dostanete do ruky.
Brzy zjistite, ze se jedna o opravdu jednoduchou vec.

Ted se podivame na **kwargs.
```python
def foo(**kwargs):
    print(kwargs)
    print(*kwargs)


def foo2(a=1, b=2, c=3):
    print(a, b, c)


foo(a=1, b=2, c=3)

some_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

foo2(**some_dict)
```
Jedna se o obdobny pripad jako v predchozim pripade, opet vyzkousejte nez budete cist dale.

**BACHA SPOJLER**

Jiste zjistite, ze fungovani je velice podobne. V pripade volani funkce foo jsme zapsali 
3 klicove argumenty, ty se vezmou a zabali se do **dictu** (slovniku) a ten se nasledne preda
do funkce foo. 
Prvni zkousime vypsat kwargs samotne. Toto volani nam vypise dict jako celek. 
V druhem pripade zkousime vypsat *kwargs, toto volani nam trosku neocekavane vypise, a, b, c. 
Tzn. klice v danem slovniku. 

Funkce foo2 funguje obdobne jako v pripade *args. Vytvorili jsme si slovnik a ten jsme nasledne s **
predali funkci foo2. ** sly a rozbalily tento dict na sadu klicovych argumentu, ktere se nasledne
priradily k jednotlivym argumentum ve funkci. Klice v dictu MUSI odpovidat nazvum argumentu
ve funkci.

Dokazete z tohoto chovani odhadnout PROC by nefungovalo print(**kwargs)?
Zkuste schvalne vytvorit takovy slovnik aby to mozne bylo. Kdo mi to v utery ukaze, tak dostane
prekvapko :D


**Dodatek**

\*args i **kwargs je mozne michat. Plati stejne poradi jako u argumentu.
Prvni args pak kwargs

v opravdu extremnim pripade vam bude fungovat i toto:

```python
def foo(a, b, c, *args, d=2, **kwargs):
    print(a, b, c, args, d, kwargs)

foo(1, 2, 3, 4, 5, d=2, e=3, f=4)

```
nicmene, pokuste se takovym divocinam vyhnout. Maximalne se setkate s takovymito zapisy:

```python
def foo(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

foo(1, 2, 3, 4, c=4, d=5)
```

## Navratova hodnota funkce
Kazda funkce v Pythonu MA navratovou hodnotu. Prijde vam to zvlastni? Nedivim se. 
Defaultne kazda pythoni funkce vraci **None** a je uplne jedno jestli do funkce napiste,
nebo nenapisete klicove slovo **return**.

Nicmene ukazme si par prikladu :)

```python
def square(a):
    return a*a
    
print(square(5))
```

volani teto funkce je doufam pochopitelne, vcetne toho CO se vraci z funkce.

Ale co de nam vrati v techto nasledujici 2 funkcich?

```python
def foo():
    print("Ahoj")
    

def foo2():
    print("Ahoj")
    return 
    
print(foo(), foo2())

```

Jak uz jsem rekl vyse, bude to **None** . Je dobre si na toto chovani zvyknout, muze byt zdrojem
neprijemnych chyb a omylu.

## Anonymni lambda funkce

Obcas nastanou situace, kdy se nam hodi nekde pouzit funkci "na jedno pouziti".

Prvni si ukazeme jednoduchy pripad:

```python
square = lambda x: x**2
square(3)
```

Co se vlastne stalo ? Je to velice jednoduche. Vytvorili jsme anonymni funkci, ktera je ulozena 
v promenne square. Tato funkce prijima jeden parametr x a vraci vysledek vyrazu x**2.

Lambda funkce mohou prijimat libovolny pocet parametru, ale vzdy vraci pouze vysledek vyrazu,
at uz je sebeslozitejsi.

K cemu je to dobre? Prikladu k pouziti je mnoho. Nicmene se zkuste podivat na built-in funkci 
[map](https://docs.python.org/3/library/functions.html#map)

a tady kratke pouziti lambdy ve spojeni s map:

```python
map_output = map(lambda x: x*2, [1, 2, 3, 4])

print(list(map_output))
for i in map_output:
    print(i)

```

uziti najdeme MNOHEM vice a postupne na ne narazime.
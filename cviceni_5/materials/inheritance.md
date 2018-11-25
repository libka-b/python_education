
# Python dedicnost && polymorfismus??

Dedicnost je zpusob, jak vytvorit vztah mezi objekty. Objekty mohou ZDEDIT chovani od predem existujicich trid,
predku. Vysledny Objekt se potom nazyva potomek. 

## Co to teda znamena??

Timto pristupem nam vznika jista hierarchie objektu, pricemz ty nejvyssi tridy jsou nejobecnejsi a postupne se v nizsich
stupnich hierarchie upresnuji. 
Jak uz jsem rekl vyse, potomci dedi atributy a metody predku(krome privatnich) mohou zdedit, modifikovat, ci uplne potlacit.
Klasicky priklad z rodiny :)

## Kratka ukazka

```python

class Parent:
    def __init__(self, name):
        self.parent_name = name

    def get_personal_info(self):
        return f"I'm parent and my name is {self.parent_name}"


class Child(Parent):
    def __init__(self, name, age, parent_name):
        Parent.__init__(self, parent_name)
        self.child_name = name
        self.age = age

    def get_personal_info(self):
        return f"I'm child, my name is {self.child_name}, my parent is {self.parent_name} and i'm {self.age} years old"


parent = Parent("Tonda Blanik")
print(parent.get_personal_info())

child = Child("Zizala", 28, "Big Tony")
print(child.get_personal_info())

```

## Co jsme si na tomto ukazali? 
Hned nekolik veci, zacneme metodou ***__init\__*** v potomkovi.
Hned na prvnim radku volame **Parent.__init\__**, co to znamena? Abychom mohli mit potomka,
tak logicky potrebujeme predka. Pokud tam tento radek nenapiseme, tak program bude fungovat, ale ztratime pristup
ke vsem parametrum predka. Neni rodic - nemas co dedit. 

V tomto pripade volam predkovu metodu **__init\__** hned na prvnim radku, nicmene nic by se nestalo, kdybych ji dal az
na konec. NICMENE, existuji pripady, kdy nam na jeji pozici zalezi. Dokazete prijit na duvod ???

Je jednoduchy, vsechny promenne a metody predka existuji az PO volani predkovi metody **__init\__** . Takze, kdybychom
chteli promenne predka pouzivat, tak tuto metodu musime predtim zavolat. Take jsem videl, ze v predkovi probihala
kontrola jistych atributu, na co inicializovat potomka, kdyz nam to na predkovi jeste muze umrit? :) 

Dalsi vec, ktera na tomto kratkem prikladu sla videt je, **polymorfismus**. Toto slovo zni na prvni pohled desive, 
ale nejedna se o nic sloziteho. 
Podivejme se na metodu **get_personal_info** (u predka i u potomka), proc kdyz potomek dedi metody predka, tak pri volani
metody nevypsal to same?? To je vec, za kterou muze **polymorfismus**.
Jak uz jsem rekl vyse, tak potomek muze upravit nebo ji dokonce potlacit. 

Tim, ze jsem metodu definoval v potomkovi znovu, tak jsem ji prepsal. V jednoduchosti?? Co je v hierarchii nize, to plati.
Zde maji potomci posledni slovo. 


## Funkce super()

Tato funkce nam vraci objekt, ktery nam umoznuje volat metody predka. Co to znamena?
Ukazeme si to opet na kratkem prikladu, ktery nam to vysvetli nejlepe:

```python

class Parent:
    def __init__(self, name):
        self.parent_name = name

    def get_personal_info(self):
        return f"I'm parent and my name is {self.parent_name}"
        
    def print_fun(self):
        print("PARENT: Fun is when I turn on TV and watching movie with my husband")


class Child(Parent):
    def __init__(self, name, age, parent_name):
        Parent.__init__(self, parent_name)
        self.child_name = name
        self.age = age

    def get_personal_info(self):
        return f"I'm child, my name is {self.child_name}, my parent is {self.parent_name} and i'm {self.age} years old"
        
    def print_fun(self):
        super().print_fun()
        print("CHILD: Thats fine, but better is Sex & Drugs & Rock & Roll")
       
        
child = Child("Honza Beachboy", 28, "Samantha Boring")
child.print_fun()

```

Co jsme to vlastne udelali??? Jak jsem rekl, ditko muze metody predka i modifikovat. Jako v prikladu, souhlasime s rodicem,
ze super party je na gauci u telky, ALE jako spravne dite k tomu chci neco dodat :) takze, zavolam predkovu metodu pomoci volani
funkce **super** a pak si stejne reknu svoje. Uz je to srozumitelnejsi? 


## Inicializace jeste jednou 

Pred par odstavci jsme se bavili o tom, kde napsat predkovu metodu **__init\__** . V nasem prikladu na pozici nezalezelo,
ale uvedme si dalsi velice jednoduchy priklad, kde uz to muze zmenit hodne. 

```python

class Parent:
    def __init__(self, name):
        self.parent_name = name
        self.best_place = "My lovely couch"

    def get_personal_info(self):
        return f"I'm parent and my name is {self.parent_name}"
        
    def print_fun(self):
        print("Fun is when I turn on TV and watching movie with my husband")
        
    def print_my_best_place(self):
        print(self.parent_name, self.best_place)



class Child1(Parent):
    def __init__(self, name, age, parent_name):
        Parent.__init__(self, parent_name)
        self.child_name = name
        self.age = age
        self.best_place = "Nice library"

    def get_personal_info(self):
        return f"I'm child, my name is {self.child_name}, my parent is {self.parent_name} and i'm {self.age} years old"
        
    def print_fun(self):
        super().print_fun()
        print("Thats fine, but better is Sex & Drugs & Rock & Roll")

    def print_my_best_place(self):
        super().print_fun()
        print(self.child_name, self.best_place)


class Child2(Parent):
    def __init__(self, name, age, parent_name):
        self.child_name = name
        self.age = age
        self.best_place = "Pub with a great beer"
        Parent.__init__(self, parent_name)

    def get_personal_info(self):
        return f"I'm child, my name is {self.child_name}, my parent is {self.parent_name} and i'm {self.age} years old"
        
    def print_fun(self):
        super().print_fun()
        print("Thats fine, but better is Sex & Drugs & Rock & Roll")
        
    def print_my_best_place(self):
        super().print_fun()
        print(self.child_name, self.best_place)
       
        
child1 = Child1("Honza Beachboy", 28, "Samantha Boring")
child2 = Child2("Kuba Drunk", 28, "Samantha Boring")
child1.print_fun()
child2.print_fun()

```

Tak jo, co jsem to provedl?? Pro lepsi ukazku jsem si vytvoril jeste jedno ditko. Prijde nekdo na to v cem se lisi? Poradim
je to nekde v metode **__init\__**.

Tak jo...maji volani predkova initu jinde. A ted zaludna otazka, prijde nekdo na to, co to zmeni?? 

Podivame se prvni na **Child1**, ktere vola init predka jako prvni. Predek si nainicializuje promennou `best_place`
a podedi se do potomka. Potomek nasledne jde a prepise ji vlastni hodnotou.
U ditka cislo 2 je to presne obracene, potomek si nainicializuje promennou `best_place` a nasledne vola init predka,
ktery jde a prepise hodnotu potomka.

No jo, ale jak to vyresit?? Co kdyz si chci pamatovat hodnotu u predka i potomka?? 
Resenim jsou privatni promennet. Co to znamena? U predka upravime promennou `best_place` na `__best_place`, tim docilime
toho, ze zustane jenom v predkovi a NEBUDE se dedit. Schvalne si to vyzkousejte.


## Vicenasobna dedicnost

Toto tema je velice diskutabilni, nicmene vam ho nemohu uprit. Jiste by se nasel pripad, kdy se to hodi.
Co to znamena vicenasobna dedicnost? 
Jak zname z bezneho zivota, tak mame vetsinou 2 rodice :) takze, vicenasobna dedicnost zname, ze potomek ma vice nez jednoho predka.
Ukazme si to opet na malem prikladu.

```python

class Mother:
    def __init__(self, eyes, hair_color, legs, fingers):
        self.eyes = eyes
        self.hair_color = hair_color
        self.__legs = legs
        self.__fingers = fingers
        
    def be_sexy(self):
        print("Hi chickas, wanna some drink?")


class Father:
    def __init__(self, eyes, hair_color, legs, fingers):
        self.__eyes = eyes
        self.__hair_color = hair_color
        self.legs = legs
        self.fingers = fingers
        
    def drink_beer(self):
        print("Give me beer and write it by rake")


class Child(Mother, Father):
    def __init__(self, age, name):
        Mother.__init__(self, 'blue', 'black', 1, 13)
        Father.__init__(self, 'brown', 'blond', 2, 10)
        self.age = age
        self.name = name
        
    def introduce_yourself(self):
        print(f"Hi, i'm {self.name}, i'm {self.age}")
        print(f"I have {self.eyes} eyes and {self.hair_color} hair")
        print(f'I have {self.legs} legs and {self.fingers} fingers')
 
 
child = Child(28, "Johny Licker")
 
```
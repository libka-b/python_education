##  print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Jak jsme si na dnesni hodine rekli, tak print je "vypisovaci" funkce.

```python
print("Hello world!")
```

![Hello world output](./images/hw_out.png)

```python
a = "Ahoj"
b = "Pythonyri"

print(a, b)
```

![Hello world output](./images/hw_out_2.png)

Jak vidime, tak defaultne nam print oddeluje jednotlive promenne mezerou, 
ale co kdyz si reknu, ze to tak nechci?

Mame k tomu krasny parametr "sep".

```python
a = "Ahoj"
b = "Pythonyri"

print(a, b, sep=":-)")

```

![Hello world output](./images/hw_out_3.png)

Defaultne nam Python kazdy print ukoncuje znakem "\n" - newline.
Printu toto nastaveni muzeme menit parametrem "end".

```python
print("Ahoj", end="")  #  ukoncuj print prazdnym stringem
print("Pythonyri")  #  ukoncuj defaultne
print("Jak se mate?", end=":-)\n")
```

![Hello world output](./images/hw_out_4.png)

Poslednim parametrem je "file", blize se s nim seznamime na cviceni "Prace se soubory".

[Dokumentace](https://docs.python.org/3/library/functions.html#print)
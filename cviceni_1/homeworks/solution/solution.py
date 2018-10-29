

def solution_print_1():
    """
    Reseni prikladu cislo 1 ze sekce PRINT
    """
    print("Python", "je", "nejlepsi", sep="!!!", end="!!!")


def solution_print_2():
    """
    Reseni prikladu 2 ze sekce print
    """
    print("uz", "nikdy", "PHP", sep="\n!!!\n")


def solution_elif_1():
    """
    Reseni prikladu 1 ze sekce if - elif - else -...
    2 varianty
    """

    numbers = range(1, 11)  # list cisel 1 - 10 , tzn suda i licha

    # tohle je takove tradicni reseni ktere zname
    even = []  # suda
    odd = []  # licha

    for i in numbers:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)

    print("suda:", even)
    print("licha:", odd)

    # tohle je vice pythoni reseni ale musite list projet 2x :(
    even = [i for i in numbers if not i % 2]
    odd = [i for i in numbers if i % 2]

    print("suda:", even)
    print("licha:", odd)


def solution_elif_2():
    """
    Reseni prikladu 2 ze sekce if - elif - else -...
    POZOR: osetreni zadani vstupu tzn. nezadal mi nekdo pismenko? Tu neresim
    Jeste jsme nebrali try - except bloky, ktere jsou na to nejjednodussi
    """

    while True:
        first = int(input("Zadejte prvni cislo:"))
        second = int(input("Zadejte druhe cislo:"))

        if first >= second:
            print("Prvni cislo musi byt mensi nez druhe, opakujte zadani")
            continue

        total_sum = sum(range(first, second + 1))  # built-in fce sum vraci soucet listu

        # muzete resit i tradicne
        # total sum = 0
        # for i in range(first, second + 1)
        #     totals_sum += i

        print(f"soucet cisel mezi {first} a {second} vcetne je {total_sum}")
        break


def solution_elif_3():
    """
    Reseni prikladu 3 ze sekce if - elif - else -...
    POZOR: osetreni zadani vstupu tzn. nezadal mi nekdo pismenko? Tu neresim
    Jeste jsme nebrali try - except bloky, ktere jsou na to nejjednodussi
    """

    actual_sum = 0
    while True:
        num  = int(input("Zadejte cislo vetsi nez 0:"))
        if num < 0:
            print(f"Rekl jsem VETSI nez 0! {num} neni vetsi")

        actual_sum += num

        print(f"Aktualni soucet cisel je {actual_sum}")

        if not num:
            break


def solution_kmp():  # TODO
    pass


if __name__ == "__main__":
    solution_print_1()
    print("", end="\n\n\n")  # pouze opticke oddeleni - nereste
    solution_print_2()
    print("", end="\n\n\n")  # pouze opticke oddeleni - nereste
    solution_elif_1()
    print("", end="\n\n\n")  # pouze opticke oddeleni - nereste
    solution_elif_2()
    print("", end="\n\n\n")  # pouze opticke oddeleni - nereste
    solution_elif_3()
    print("", end="\n\n\n")  # pouze opticke oddeleni - nereste
    solution_kmp()




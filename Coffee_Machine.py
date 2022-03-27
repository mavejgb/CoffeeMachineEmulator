import time             # improt biblioteki na potrzeby opóznenia

iKaw = 0                # zmienna przechowująca ilość sprzedanych kaw
stan1zl = 0             # zmienna przechowywująca stan 1zł
stan2zl = 0             # zmienna przechowywująca stan 2zł
bWarunek = True         # warunek do obsługi pętli
b2zl = True             # warenek do odjęcia 1zł ze stanu, przy zakupie za 2zł


def zl_1():             # funkcja obsługująca wariant 1 zł.
    global stan1zl
    global iKaw

    iKaw += 1
    stan1zl += 1
    kawa_1 = '\033[92m' + " Kawa gotowa, proszę uważaj jest gorąca! Dziękujemy za zakup!"
    return kawa_1


def zl_2():             # funkcja obsługująca wariant 2 zł.
    global stan1zl
    global stan2zl
    global b2zl
    global iKaw

    stan2zl += 2
    kawa_2 = '\033[92m' + "Kawa gotowa, proszę uważaj jest gorąca! odbierz resztę 1zł, dziękujemy za zakup!"
    kawa_2_0 = '\033[93m' + "brak środków do wydania reszty, odbierz swoje 2 zł i wrzuć 1zł, aby kupić kawę."
    if stan1zl > 0:
        b2zl = False
        iKaw += 1
        return kawa_2
    else:
        stan2zl -= 2
        return kawa_2_0


def zl_5():             # funkcja obsługująca wariant 5 zł.
    odpowiedz = '\033[93m' + "Wrzuciłeś nieobsługiwana monetę 5zł, zwrot - odbierz monetę."
    return odpowiedz


def zl_0():             # funkcja obsługująca wariant żeton serwisowy.
    global bWarunek
    bWarunek = False
    odpowiedz_1 = '\033[96m' + "Wrzuciłeś żeton serwisowy, przerwanie pracy automatu!"
    return odpowiedz_1


def errorHandler():             # funkcja obsługująca wyjatki (wpisanie złej wartości na wejsciu).
    return '\033[91m' + "zła moneta!"

while bWarunek:


    print('\033[0m' + "\n Stan monet 1zł =", stan1zl, "; Stan monet 2zł =", stan2zl, "; sprzedanych kaw =", iKaw)
    print("""
       AUTOMAT DO KAWY,  WITAMY!
      Koszt kawy to 1zł, ZAPRASZAMY!
       """)

    choice = int(input(' Wrzuć monetę, aby otrzymać kawę...\n '))          # podanie wartości na wejściu

    operations = {                                                      # coś jak case w jezykach "C".
        0: zl_0,
        1: zl_1,
        2: zl_2,
        5: zl_5
    }

    output = operations.get(choice, errorHandler)()               # przekazanie wartości z wejscia i obsługa wyjątków
    print(output)
    if b2zl == False:
        stan1zl -=1
        b2zl = True

    time.sleep(1)


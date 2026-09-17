# Python szkolenie - Podstawy (dzień 2)

# ==============================================================================
# 6. Łańcuchy znaków (ciąg dalszy)
# ==============================================================================

# --- len() --------------------------------------------------------------------
# Za pomocą len() sprawdzamy długość napisu (liczbę znaków)
tekst_6 = 'Ala ma kota'
print(len(tekst_6))   # 11 --> spacje też są znakami

tekst_6A = 'Ala ma ko\tta'
print(len(tekst_6A))  # 12 --> \t to jeden znak (tabulator)

tekst_6B = ''
print(len(tekst_6B))  # 0 --> pusty napis

tekst_6C = ' '
print(len(tekst_6C))  # 1 --> sama spacja to też znak

"""
haslo = input('Podaj hasło:')
if len(haslo) >= 8:
    print('Hasło posiada odpowiednią ilość znaków')
else:
    print('Hasło wymaga min. 8 znaków. Błąd')
"""

# --- count() ------------------------------------------------------------------
# count() zlicza, ile razy podany znak / fragment występuje w napisie
print("**count**"*3)
tekst_6D = 'banana'
x_6 = 'a'
print(tekst_6D.count('a'))   # 3
print(tekst_6D.count('an'))  # 2
print(tekst_6D.count('x'))   # 0 --> brak wystąpień to 0, a nie błąd
print(tekst_6D.count(x_6))   # 3 --> można podać zmienną

tekst_6E = 'aaaa'
print(tekst_6E.count('a'))   # 4
print(tekst_6E.count('aa'))  # 2 --> count() nie liczy nakładających się wystąpień (a nie 3)

tekst_6F = 'Python'
print(tekst_6F.count('python'))            # 0 --> wielkość liter ma znaczenie
print((tekst_6F.upper()).count('PYTHON'))  # 1 --> najpierw ujednolicamy wielkość liter

# --- strip(), lstrip(), rstrip() ----------------------------------------------
# Usuwają białe znaki (spacje, \t, \n) z brzegów napisu - ze środka już nie!
print('**strip**'*4)
tekst_6G = '       Dominik idzie na     koncert        '

print(tekst_6G)
print(tekst_6G.strip())           # --> usuwa białe znaki z obu stron
print(tekst_6G.lstrip(), end='')  # --> usuwa z lewej strony (l = left)
print(tekst_6G.rstrip())          # --> usuwa z prawej strony (r = right)

# --- split() i join() ---------------------------------------------------------
# split() zamienia tekst na listę, join() zamienia listę na tekst

# :: split()
zdanie_6 = 'Produkty koncza sie i trzeba je uzupelnic'
print(zdanie_6.split())  # bez argumentu dzieli po białych znakach
zdanie_6A = zdanie_6.split()
print(type(zdanie_6A))   # <class 'list'>

csv_line_6 = 'Adam, 25,Kraków'
print(csv_line_6.split(','))       # ['Adam', ' 25', 'Kraków'] --> spacja po przecinku zostaje w elemencie

number_line_6 = '1-6-4-3-4-5'
print(number_line_6.split('-',2))  # ['1', '6', '4-3-4-5'] --> drugi argument to maks. liczba podziałów

# :: join()
lista6_owoce = ['banan','jablko','gruszka']
lista6_owoceB = " ".join(lista6_owoce)
print(type(lista6_owoceB))      # <class 'str'>

print("".join(lista6_owoce))    # bananjablkogruszka
print(" ".join(lista6_owoce))   # banan jablko gruszka
print("-".join(lista6_owoce))   # banan-jablko-gruszka
print(", ".join(lista6_owoce))  # banan, jablko, gruszka

# --- Łańcuchowanie metod ------------------------------------------------------
# strip(), lower(), replace() zwracają NOWY napis (str jest niemutowalny, oryginał się nie zmienia),
# więc na wyniku możemy od razu wywołać kolejną metodę
print("**Łańcuchy**"*4)
przyklad_6 = '      WITAJ W PYTHONIE     '
wynik_czyszczenia_6 = przyklad_6.strip()
wynik_czyszczenia_6 = wynik_czyszczenia_6.lower()
wynik_czyszczenia_6 = wynik_czyszczenia_6.replace('pythonie','świecie')
print(wynik_czyszczenia_6)

# :: To samo w jednej linii
# Kolejność ma znaczenie: replace('pythonie', ...) zadziała dopiero po lower()
wynik_czyszczenia_6B = przyklad_6.strip().lower().replace('pythonie','świecie')
print(wynik_czyszczenia_6B)

email6_czyszczenie = ' adAm@Gmail.com  '
print(email6_czyszczenie.strip().lower())  # adam@gmail.com

# --- Iterowanie po łańcuchach znaków ------------------------------------------
przyklad6_iter = 'Python'

# Index: 0 1 2 3 4 5
# Znak:  P y t h o n

for i in przyklad6_iter:
    print(i)

for index,i in enumerate(przyklad6_iter):
    print(f"Index: {index} Znak: {i}")

# :: Przykład praktyczny - isupper()
przyklad6_iterB = 'PythOn JeT SuEPer'
duzy_znak6 = 0
for i in przyklad6_iterB:
    if i.isupper():
        duzy_znak6 += 1
    print(i)

print(f"Zdanie ma {duzy_znak6} dużych znaków")

# :: Indeksowanie
print(przyklad6_iter[0])    # P --> pierwszy znak
print(przyklad6_iter[-1])   # n --> ostatni znak
# print(przyklad6_iter[8])  # --> IndexError: string index out of range

# --- Metody sprawdzające ------------------------------------------------------
# Zwracają True albo False
# Metoda            Sprawdza, czy...
# .isalpha()        same litery
# .isdigit()        same cyfry
# .isalnum()        litery i/lub cyfry
# .isspace()        same białe znaki
# .islower()        wszystkie litery małe
# .isupper()        wszystkie litery wielkie
# .istitle()        każde słowo z wielkiej, reszta liter małe ('PyTHon'.istitle() --> False)
# .isnumeric()      same znaki numeryczne
# .isidentifier()   poprawna nazwa zmiennej
# .startswith(x)    zaczyna się od x
# .endswith(x)      kończy się na x

zmienna6 = ''
print(zmienna6.isalpha(), zmienna6.isdigit())  # False False --> dla pustego napisu metody is...() zwracają False

# :: Ćwiczenie - uzyskaj True dla wybranych metod sprawdzających
# .isalpha() - czy same litery
example1 = 'Python'
print(example1, example1.isalpha())

# .isdigit() - czy same cyfry
example2 = '123'
print(example2, example2.isdigit())

# .isalnum() - czy litery i/lub cyfry
example3 = 'Python3'
print(example3, example3.isalnum())

# .isspace() - czy same białe znaki
example4 = ' '
print(example4, example4.isspace())

# .islower() - czy wszystkie litery małe
example5 = 'python'
print(example5, example5.islower())

# .isupper() - czy wszystkie litery wielkie
example6 = 'PYTHON'
print(example6, example6.isupper())

# .istitle() - czy każde słowo z wielkiej, a reszta liter małe
example7 = 'To Jest Python'
print(example7, example7.istitle())

# .isnumeric() - czy same znaki numeryczne
example8 = '123'
print(example8, example8.isnumeric())

# .isidentifier() - czy poprawna nazwa zmiennej
example9 = 'moja_zmienna'
print(example9, example9.isidentifier())

# .startswith(x) - czy zaczyna się od x
example10 = 'xpython'
print(example10, example10.startswith('x'))

# .endswith(x) - czy kończy się na x
example11 = 'pythonx'
print(example11, example11.endswith('x'))

# --- Mnożenie i wyrównywanie tekstu -------------------------------------------

# :: Mnożenie tekstu
print('-'*100)
print('haha'*100)
# print('*'*2.5) # --> TypeError: can't multiply sequence by non-int of type 'float' (mnożymy tylko przez int)

# :: Wyrównanie w f-stringu
# Zapis    Działanie
# :^30     wyśrodkowanie na szerokości 30 znaków
# :<30     wyrównanie do lewej
# :>30     wyrównanie do prawej
# :=^30    znak przed ^ < > to wypełniacz (tu '=' zamiast spacji)
raport6 = 'Raport'
print('='*30)
print(f'{raport6:^30}')
print(f'{raport6:=^30}')
print(f'{raport6:<30}')
print(f'{raport6:=<30}')
print(f'{raport6:>30}')
print(f'{raport6:=>30}')
print('='*30)

# --- Sprawdzanie, czy tekst zawiera frazę -------------------------------------
raport6A = 'Raport poszkoleniowy Python'

print('Raport' in raport6A)            # True
print('raport' in raport6A)            # False --> wielkość liter ma znaczenie
print(raport6A.startswith('Raport'))   # True
print(raport6A.startswith('dam'))      # False
print(raport6A.endswith('Python'))     # True
print(raport6A.endswith('Raport'))     # False
print(raport6A.find('poszkoleniowy'))  # 7 --> indeks, od którego zaczyna się szukany fragment
print(raport6A.find('ksiazka'))        # -1 --> gdy fragmentu nie ma
print(raport6A.index('Python'))        # 21 --> działa jak find()...
# print(raport6A.index('ksiazka'))     # --> ...ale gdy fragmentu nie ma: ValueError: substring not found

# --- Porównywanie napisów -----------------------------------------------------
print('python' == 'Python')  # False
print('python' == 'python')  # True

# :: Czy Python > Java?
# Napisy porównujemy znak po znaku według kodów Unicode (ord)
print('Python' > 'Java')     # True --> 'P' (80) > 'J' (74)
print('apple' > 'banana')    # False --> 'a' (97) < 'b' (98)

# :: Wartości ASCII / Unicode
print(ord("A"))    # 65
print(ord("Z"))    # 90
print(ord("a"))    # 97
print(ord("b"))    # 98
print(ord("z"))    # 122
print(chr(80))     # P --> odwrotność ord()
# Wielkie litery mają mniejsze kody niż małe, dlatego 'ala' > 'Ala' --> True

# --- Cięcia, cięcia - slicing -------------------------------------------------
# napis[start:stop:step] --> stop NIE wchodzi do wyniku (tak jak w range)
slice6 = 'Python jest jezykiem programowania'

# :: Wyciągnięcie jednego znaku
print(slice6[0])      # P
print(slice6[6])      # ' ' --> spacja
print(slice6[-1])     # a
# print(slice6[100])  # --> IndexError: string index out of range

# :: Slice od-do
print(slice6[0:6])    # Python
print(slice6[:6])     # Python --> start domyślnie od początku
print(slice6[7:100])  # jest jezykiem programowania --> w slice'ie indeks poza zakresem nie wywala błędu
print(slice6[7:])     # jest jezykiem programowania --> stop domyślnie do końca

# :: Step
print(slice6[::2])    # co drugi znak

# :: Odwrócenie kolejności
print(slice6[::-1])      # cały napis od tyłu
print(slice6[100:4:-1])  # od końca do indeksu 5 włącznie (4 już nie wchodzi)

# :: Praktyczne wykorzystanie - maskowanie numeru karty
karta = "1234567890123456"
zamaskowana = "****-****-****-" + karta[-4:]
print(zamaskowana)   # ****-****-****-3456

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 6.1 - 6.9A <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 6.1 - Poproś użytkownika o imię i nazwisko (jeden input). Wyświetl: imię z wielkiej, nazwisko wielkimi literami.
# Np. "jan kowalski" --> Jan KOWALSKI. (split() + index)
"""
dane = input('Podaj imię i nazwisko: ')
imie, nazwisko = dane.split()
print(imie.capitalize(), nazwisko.upper())

dane = input("Podaj imię oraz nazwisko: ")
spacja = dane.find(" ")  # indeks spacji rozdzielającej imię i nazwisko
print(f"{dane[0:spacja].title()} {dane[spacja + 1:].upper()}")
"""

# 6.2 - Poproś o zdanie. Policz ile jest w nim liter a (zarówno a jak i A).
"""
zdanie = input("Podaj zdanie: ")
print(zdanie.count("a") + zdanie.count("A"))

zdanie = input('Podaj jakieś zdanie: ')
litera = 'a'
litera_duza = 'A'
print(zdanie.count(litera) + zdanie.count(litera_duza))

zdanie = input('Podaj zdanie aby policzyć "a" "A": ')
zdanie_nisko = zdanie.lower()  # po lower() wystarczy liczyć tylko małe 'a'
print(zdanie_nisko.count('a'))
"""

# 6.3 - Poproś o tekst ze spacjami na początku i końcu. Oczyść go (strip), zamień na małe litery i wyświetl ile ma znaków.
"""
tekst = input("Podaj tekst ze spacjami na początku i końcu: ")  # przykładowy tekst: " alA ma "
tekst_clean = tekst.lower().strip()
print(tekst_clean)
print(len(tekst_clean))
"""

# 6.5 - Poproś o hasło. Sprawdź: czy ma min. 8 znaków, czy zawiera cyfrę, czy zawiera wielką literę.
# Wyświetl wynik każdego sprawdzenia.
"""
pasek = input("Podaj hasło: ")
ma_cyfre = False
ma_wielka = False
ma_8_znakow = False
for znak in pasek:
    if znak.isdigit():
        ma_cyfre = True
    if znak.isupper():
        ma_wielka = True
    if len(pasek) >= 8:  # działa, ale długość wystarczy sprawdzić raz, poza pętlą: ma_8_znakow = len(pasek) >= 8
        ma_8_znakow = True
print("Ma 8 znaków:", ma_8_znakow)
print("Ma cyfrę:", ma_cyfre)
print("Ma wielką literę:", ma_wielka)
"""

# 6.8* - Napisz program sprawdzający czy podane słowo jest palindromem (czytane od przodu i tyłu tak samo, np. kajak, anna).
# Ignoruj wielkość liter. (slice)
"""
slowo = input("Podaj słowo: ")
slowo = slowo.lower()
od_tylu = slowo[::-1]
if od_tylu == slowo:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")
"""

# 6.9A - Napisz program, który przyjmie od użytkownika ciąg tekstowy, a następnie usunie z niego znaki ,.!? i
# wyświetli go powiększonego do dużych liter na konsoli. (replace)
"""
tekst = input("Podaj tekst: ")
tekst = tekst.replace(",", "").replace(".", "").replace("!", "").replace("?", "").upper()
print(tekst)
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ==============================================================================
# 7. Listy
# ==============================================================================

# --- Tworzenie list, range() --------------------------------------------------
# Lista jest mutowalna - można zmieniać jej zawartość po utworzeniu
lista_pusta7A = []
lista_pusta7B = list()
lista_range = list(range(1,11))

print(lista_pusta7A)  # []
print(lista_pusta7B)  # []
print(lista_range)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# :: Co może być w liście
lista_number = [2,5,4,3,45,73]                     # int
lista_number_float = [2.4,5.7,4.4,3.5,45.3,73.4]   # float
lista_number_int_float = [2.4,5.7,3,45,73]         # int + float

lista_str = ['banan','owoc','Damian']

lista_bool = [True,False,True]

lista_mieszana = [False,5.7,4.4,'owoc','Damian',True,3,45,73]  # różne typy w jednej liście

# --- Pobieranie wartości z list -----------------------------------------------
#            0          1        2        3        4
owoce7 = ["jabłko", "banan", "gruszka", "kiwi", "mango"]

print(owoce7[0])      # jabłko
print(owoce7[-1])     # mango
print(owoce7[-3])     # gruszka
# print(owoce7[20])   # --> IndexError: list index out of range

print(owoce7[0:3])    # ['jabłko', 'banan', 'gruszka']
print(owoce7[:3])     # to samo --> start domyślnie 0
print(owoce7[:])      # cała lista
print(owoce7[:20])    # cała lista --> w slice'ie indeks poza zakresem nie wywala błędu
print(owoce7[::2])    # co drugi element
print(owoce7[::-1])   # lista od tyłu
print(owoce7[::-2])   # od tyłu, co drugi
print(owoce7[20:2:-2])

# --- Iterowanie po listach ----------------------------------------------------
for i in owoce7:
    print(i)

for index,i in enumerate(owoce7):
    print(f"{index} - {i}")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 7.1 - 7.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 7.1 - Stwórz listę 5 ulubionych filmów. Wyświetl pierwszy i ostatni element.
filmy = ["Matrix", "Gladiator", "Incepcja", "Interstellar", "Avatar"]
print(filmy[0])
print(filmy[-1])

# 7.2 - Stwórz listę liczb od 1 do 10. Wyświetl elementy od indeksu 3 do 7.
lista_liczby = list(range(1,11))
print(lista_liczby[3:8])  # stop = 8, bo indeks 8 już nie wchodzi
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Sprawdzanie, czy element znajduje się na liście --------------------------
owoce_powt7 = ["jabłko", "banan", "gruszka"]

print('jabłko' in owoce_powt7)  # True
print('banan' in owoce_powt7)   # True
print('wiśnia' in owoce_powt7)  # False

for i in owoce_powt7:
    if i.lower() == 'banan':
        print('Znaleźliśmy banana')

# --- Modyfikowanie zawartości listy -------------------------------------------
# Lista jest mutowalna - elementy podmieniamy przez indeks albo slice
owoce_mod7 = ["gruszka", "banan", "agrest", "jabłko"]
print(owoce_mod7)

owoce_mod7[0] = 'czereśnia'
print(owoce_mod7)

owoce_mod7[1:3] = ['ananas','gruszka']
print(owoce_mod7)

# :: Pułapka --> podmiana slice'a na napis daje nieoczekiwany wynik
owoce_mod7[1:3] = 'czereśnia'  # --> napis to sekwencja znaków: każda litera staje się osobnym elementem
print(owoce_mod7)

# --- Dodawanie elementów: append(), insert(), extend() ------------------------
# Metoda              Działanie
# append(x)           dodaje jeden element na końcu listy
# insert(i, x)        wstawia jeden element przed indeks i
# extend(lista)       dodaje wiele elementów na końcu (lista zostaje płaska)
# lista1 + lista2     tworzy nową, połączoną listę
print('*'*70)
owoce_dod7 = ["jabłko", "banan"]
print(owoce_dod7)

# :: append()
owoce_dod7.append('agrest')  # --> append dodaje wartość na końcu listy
print(owoce_dod7)

"""
# Pułapka przy append
owoce_dod7.append(['agrest','owoce'])  # --> cała lista staje się jednym elementem (zagnieżdżenie listy)
print(owoce_dod7)
print(owoce_dod7[3][0])
"""

# :: insert()
owoce_dod7.insert(0,'gruszka')
print(owoce_dod7)

"""
# Pułapka przy insert - tworzy zagnieżdżenie
owoce_dod7.insert(0,['gruszka'])
print(owoce_dod7)
"""

# :: extend()
"""
# Pułapka przy extend
owoce_dod7.extend('gruszka')  # --> napis rozbity na litery, każda jako osobny element
print(owoce_dod7)
"""

owoce_dod7.extend(['gruszka','ananas','wierzba'])  # --> wiele wartości naraz
print(owoce_dod7)

# :: Operator +
nowa_owoce7 = ["jabłko"] + ["banan"] + ["gruszka"]
print(nowa_owoce7)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 7.9A - 7.11A <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 7.9A - Lista zakupów. Stwórz pustą listę zakupy, a potem:
# a) za pomocą append() dodaj kolejno "chleb", "mleko" i "masło", wyświetl listę,
# b) wstaw "jajka" na sam początek, a "ser" tuż przed ostatni element (użyj indeksu ujemnego)
# i wyświetl listę. Oczekiwany wynik: ['jajka', 'chleb', 'mleko', 'ser', 'masło'].
shopping_list = []
shopping_list.append("chleb")
shopping_list.append("mleko")
shopping_list.append("masło")
print(shopping_list)
shopping_list.insert(0, "jajka")
shopping_list.insert(-1, "ser")  # insert(-1, x) wstawia PRZED ostatni element
print(shopping_list)

# 7.11A - Kolejka do lekarza. Z listy kolejka = ["Adam", "Ola"]:
# a) dodaj "Kasia" i "Tomek" na koniec, a "Zofia" na początek,
# b) dołóż grupę ["Bartek", "Ewa", "Jan"] jedną operacją (lista ma zostać płaska),
# c) wstaw "Marek" na trzecie miejsce i wypisz kolejkę z numerami: 1. Zofia, 2. Adam, ...
queue = ["Adam", "Ola"]
queue.insert(0, "Zofia")
queue.extend(["Kasia", "Tomek"])
queue = queue + ["Bartek", "Ewa", "Jan"]  # albo: queue.extend(["Bartek", "Ewa", "Jan"])
queue.insert(2,"Marek")                   # trzecie miejsce = indeks 2
for index, i in enumerate(queue,1):
    print(f"{index}. {i}")  # format z treści zadania: 1. Zofia, 2. Adam, ...
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Usuwanie elementów: remove(), pop(), del, clear() ------------------------
# Sposób          Co usuwa                                   Zwraca
# remove(x)       pierwsze wystąpienie wartości x            None
# pop(i)          element o indeksie i (bez i --> ostatni)   usunięty element
# del lista[i]    element o indeksie i                       nic (to instrukcja, nie metoda)
# clear()         wszystkie elementy                         None
owoce_del7 = ["jabłko", "banan", "gruszka", "kiwi", "gruszka", "kiwi", "banan"]

owoce_del7.remove('banan')  # --> usuwa pierwsze wystąpienie
print(owoce_del7)

# owoce_del7.remove('mikolaj')  # --> ValueError: list.remove(x): x not in list

owoce_pop_index = owoce_del7.pop(1)
print(owoce_del7)
print(owoce_pop_index)  # usunięty element

owoce_pop_last = owoce_del7.pop()
print(owoce_del7)
print(owoce_pop_last)   # usunięty ostatni element

del owoce_del7[3]
print(owoce_del7)

# del owoce_del7[10]  # --> IndexError: list assignment index out of range

owoce_del7.clear()
print(owoce_del7)  # []

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 7.3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 7.3 - Porządki na liście. Na liście zwierzeta = ["pies", "kot", "chomik", "kot", "papuga", "rybka"]
# wykonaj po kolei i po każdym kroku wyświetl listę:
# a) usuń pierwszego "kot" (remove),
# b) usuń pierwszy element (del),
# c) zdejmij ostatni element i wyświetl, co usunąłeś (pop),
# d) zdejmij element o indeksie 1 i wyświetl, co usunąłeś (pop),
# e) usuń "słoń", ale tylko jeśli jest na liście - inaczej wyświetl Nie ma słonia,
# f) wyczyść listę (clear).
zwierzeta = ["pies", "kot", "chomik", "kot", "papuga", "rybka"]

zwierzeta.remove('kot')
print(zwierzeta)

del zwierzeta[0]
print(zwierzeta)

zwierzeta_last_item = zwierzeta.pop()
print(zwierzeta_last_item)
print(zwierzeta)

zwierzeta_index_item = zwierzeta.pop(1)
print(zwierzeta_index_item)
print(zwierzeta)

if 'słoń' in zwierzeta:  # sprawdzamy przez in, żeby remove nie wywalił ValueError
    zwierzeta.remove('słoń')
    print('Słoń usunięty')
else:
    print('Nie ma słonia')
print(zwierzeta)  # poza if/else --> lista wyświetla się po kroku e) w obu przypadkach

zwierzeta.clear()
print(zwierzeta)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Funkcje wbudowane dla list -----------------------------------------------
print("*"*30)
liczby_fun7 = [4, 2, 8, 1, 5, 3, 7, 6]

print(min(liczby_fun7))  # 1
print(max(liczby_fun7))  # 8
print(sum(liczby_fun7))  # 36
print(len(liczby_fun7))  # 8

zwierzeta_fun7 = ['arnold','zygzak','Zygzak',"pies", "kot", "chomik", "kot", "papuga", "rybka"]

print(min(zwierzeta_fun7))    # Zygzak --> wielkie litery mają mniejsze kody (ord) niż małe
print(max(zwierzeta_fun7))    # zygzak
# print(sum(zwierzeta_fun7))  # --> TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(len(zwierzeta_fun7))    # 9

# :: Metody count() i index()
oceny7 = [5, 4, 3, 5, 5, 4, 3, 5]

print(oceny7.count(5))  # 4 --> ile razy występuje 5
print(oceny7.index(3))  # 2 --> indeks pierwszego wystąpienia 3

# --- Sortowanie i odwracanie list: sort(), sorted() ---------------------------
# Zapis            Zmienia oryginał   Zwraca
# lista.sort()     tak                None
# sorted(lista)    nie                nową, posortowaną listę
liczby_sort7 = [4, 2, 8, 1, 5]

liczby_sort7.sort()  # --> sortuje oryginalną listę, przypisanie wyniku do zmiennej da None
print(liczby_sort7)

liczby_sort7 = [4, 2, 8, 1, 5]

liczby_sort_now = sorted(liczby_sort7)
print(liczby_sort7)     # [4, 2, 8, 1, 5] --> oryginał bez zmian
print(liczby_sort_now)  # [1, 2, 4, 5, 8]

# :: Sortowanie malejąco - reverse=True
liczby_sort7 = [4, 2, 8, 1, 5]

liczby_sort7.sort(reverse=True)
print(liczby_sort7)

liczby_sort7 = [4, 2, 8, 1, 5]

liczby_sort_now = sorted(liczby_sort7,reverse=True)
print(liczby_sort7)
print(liczby_sort_now)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 7.5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 7.5 - Stwórz listę liczb [5, 3, 8, 1, 9, 2, 7]. Posortuj ją rosnąco i wyświetl,
# potem malejąco i wyświetl.
liczby = [5, 3, 8, 1, 9, 2, 7]
liczby.sort()
print(liczby)
liczby.sort(reverse=True)
print(liczby)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Inne ciekawe funkcje i możliwości ----------------------------------------

# :: List comprehension
# Przeiteruj przez 10 liczb i dodaj ich potęgi do nowo utworzonej listy
lista_c = []
for i in range(1,11):
    lista_c.append(i**2)
print(lista_c)

lista_compr = [i**2 for i in range(1,11)]  # --> to samo w jednej linii
print(lista_compr)

# :: zip()
a7 = [1, 2, 3, 4]  # --> zip kończy na najkrótszej liście, 4 zostaje pominięte
b7 = [10, 20, 30]

for i7,k7 in zip(a7,b7):
    print(i7,k7)

print(zip(a7,b7))        # <zip object at 0x...> --> sam zip nie pokazuje zawartości
print(list(zip(a7,b7)))  # [(1, 10), (2, 20), (3, 30)] --> lista krotek

# :: Rozpakowanie
owoce_roz = ["jabłko", "banan", "gruszka"]
raz, dwa, trzy = owoce_roz  # liczba zmiennych musi się zgadzać z liczbą elementów
print(raz,dwa,trzy)

pierwszy, *reszta = owoce_roz  # *reszta zbiera wszystkie pozostałe elementy do listy
print(pierwszy)
print(*reszta)  # * rozpakowuje listę --> print('banan', 'gruszka')

# :: Kopiowanie (pułapka)
pierwsza_lista_a7 = [1,3,5,6]
druga_lista_a7 = pierwsza_lista_a7  # --> tak nie kopiujemy: obie zmienne wskazują na tę samą listę
"""
# Jak to naprawić?
druga_lista_a7 = pierwsza_lista_a7[:]      # 1 sposób
druga_lista_a7 = pierwsza_lista_a7.copy()  # 2 sposób
druga_lista_a7 = list(pierwsza_lista_a7)   # 3 sposób
# Wszystkie 3 sposoby to kopie PŁYTKIE - przy listach zagnieżdżonych wewnętrzne listy dalej są wspólne
# (wtedy: import copy --> copy.deepcopy(lista))
"""

print(pierwsza_lista_a7)
print(druga_lista_a7)

druga_lista_a7.append(9)

print(pierwsza_lista_a7)  # [1, 3, 5, 6, 9] --> zmieniła się też pierwsza lista!
print(druga_lista_a7)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE DODATKOWE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lista_compr = [i**2 for i in range(1,11)]  # przypomnienie
print(lista_compr)

# Utwórz za pomocą list comprehension listę liczb od 1 do 20 pomnożonych przez 5
lista = [i * 5 for i in range(1, 21)]
print(lista)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ==============================================================================
# 8. Krotki
# ==============================================================================

# --- Deklaracja i uzupełnianie krotek danymi ----------------------------------
# Krotka (tuple) jest niemutowalna - po utworzeniu nie zmienimy jej zawartości
krotka_8 = (3, 30)
print(type(krotka_8))

krotka_str8 = ('tekst','imie','gears')
print(type(krotka_str8))

krotka_pusta8A = ()
krotka_pusta8B = tuple()
print(type(krotka_pusta8A),type(krotka_pusta8B))

krotka_miesz8 = ('tekst','imie','gears',3, 30,True, 45.6)
print(type(krotka_miesz8))

# :: Krotka jednoelementowa
# krotka_elem8 = ('imie')  # --> str, nie tuple (same nawiasy nie tworzą krotki)
krotka_elem8 = ('imie',)   # --> krotkę tworzy przecinek
print(type(krotka_elem8))

# :: Krotka bez nawiasów
krotka_bez_nawiasu8 = 'czerwony','niebieski','zielony'
krotka_bez_nawiasu8 = 'czerwony',
print(type(krotka_bez_nawiasu8))

# --- Edytowanie krotki - niemutowalny obiekt ----------------------------------

# :: Nowa krotka przez dodawanie
krotka_str8 = ('tekst','imie','gears')
krotka_str8 = krotka_str8 + ('banan',)  # --> powstaje nowa krotka, stara się nie zmienia
# krotka_str8 = krotka_str8 + 'banan',  # --> TypeError: can only concatenate tuple (not "str") to tuple
#                                       #     przy dodawaniu zawsze opakuj element w ()
print(type(krotka_str8))
print(krotka_str8)

# :: Zmiana przez listę: tuple --> list --> tuple
krotka_na_liste8 = list(krotka_str8)
print(krotka_na_liste8)
krotka_na_liste8.append('gruszka')
print(krotka_na_liste8)
lista_na_krotke8 = tuple(krotka_na_liste8)
print(lista_na_krotke8)

# :: Mnożenie krotki
hahaha = ('ha',) * 3  # --> ('ha', 'ha', 'ha')
# hahaha = 'ha', * 3  # --> TypeError: Value after * must be an iterable, not int
print(hahaha)

# --- Pobieranie wartości z krotek ---------------------------------------------
# Działa tak samo jak w listach
owoce_k8 = ("jabłko", "banan", "gruszka", "kiwi", "mango")

print(owoce_k8[0])     # jabłko
print(owoce_k8[-1])    # mango
# print(owoce_k8[20])  # --> IndexError: tuple index out of range
print(owoce_k8[3])     # kiwi

print(owoce_k8[:])
print(owoce_k8[4:])
print(owoce_k8[:4])
print(owoce_k8[::2])
print(owoce_k8[::-1])
print(owoce_k8[::-2])
print(owoce_k8[:2:-2])

# --- Rozpakowywanie krotek ----------------------------------------------------
# Bardzo częste i przydatne
owoce_k8 = ("jabłko", "banan", "gruszka")
raz, dwa, trzy = owoce_k8
print(f"Pierwsza zmienna \"{raz}\", druga zmienna \"{dwa}\", trzecia zmienna \"{trzy}\"")

owoce_k8 = ("jabłko", "banan", "gruszka")
pierwszy, *reszta = owoce_k8  # --> *reszta to zawsze lista, nawet przy rozpakowaniu krotki
print(f"Pierwsza zmienna \"{pierwszy}\", druga zmienna \"{reszta}\"")

# :: Zamiana wartości zmiennych
apex = 'predator'
alpha = 'wilk'
print(f"Apex {apex}, Alpha {alpha}")
apex, alpha = alpha, apex  # --> po prawej powstaje krotka, którą rozpakowujemy, bez trzeciej zmiennej
print(f"Apex {apex}, Alpha {alpha}")

# --- Funkcje dla krotek -------------------------------------------------------
liczby = (4, 2, 8, 1, 5)
print(len(liczby))      # 5
print(min(liczby))      # 1
print(max(liczby))      # 8
print(sum(liczby))      # 20
print(liczby.count(2))  # 1
print(liczby.index(2))  # 1

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 8.1 - 8.5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 8.1 - Stwórz krotkę z 4 porami roku. Wyświetl pierwszą i ostatnią.
pory_roku = ('zima', 'wiosna', 'lato', 'jesień')
print(pory_roku[0], pory_roku[-1], sep=", ")  # zima, jesień (bez sep wyszłoby "zima ,  jesień")

# 8.2 - Stwórz krotkę punkt = (5, 10). Rozpakuj ją do zmiennych x i y. Wyświetl: x=5, y=10.
punkt = (5, 10)
x, y = punkt
print(f'x = {x}, y = {y}')

# 8.3 - Stwórz krotkę dane = ("Adam", 25, "Warszawa"). Rozpakuj ją do zmiennych imie, wiek, miasto i wyświetl w f-stringu.
dane = ("Adam", 25, "Warszawa")
raz, dwa, trzy = dane
print(f"imie - {raz}, wiek - {dwa}, miasto - {trzy}")

# 8.4 - Mając krotkę liczby = (3, 7, 1, 9, 4, 7, 3, 7), policz ile razy występuje 7 i na jakim indeksie jest pierwszy raz.
liczby = (3, 7, 1, 9, 4, 7, 3, 7)
print(liczby.count(7))  # 3
print(liczby.index(7))  # 1

# 8.5 - Stwórz dwie zmienne a = 100 i b = 200. Zamień ich wartości za pomocą krotki (bez trzeciej zmiennej).
a = 100
b = 200
a, b = b, a
print("Wartość liczby a:", a, "Wartość liczby b:", b)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ==============================================================================
# 9. Słowniki
# ==============================================================================

# --- Tworzenie słowników ------------------------------------------------------
# Słownik przechowuje pary klucz: wartość
slownik_9A = {}
slownik_9B = dict()
print(type(slownik_9A), type(slownik_9B))

slownik_przyklad_9A = {'imie':'Dominik','wiek':28,'prawo_jazdy':True}
slownik_przyklad_9B = dict(imie='Dominik',wiek=28,prawo_jazdy=True)
print(slownik_przyklad_9B)

# :: Słownik z listy / krotki par
# lista_krotek_9 = [('imie','Dominik'),('wiek',28),('prawo_jazdy',False)]  # lista krotek
# lista_krotek_9 = (('imie','Dominik'),('wiek',28),('prawo_jazdy',False))  # krotka krotek
lista_krotek_9 = ('imie','Dominik'),('wiek',28),('prawo_jazdy',False)      # to samo bez nawiasów - wszystkie 3 zapisy działają
print(dict(lista_krotek_9))

# :: Słownik zagnieżdżony
slownik_zagn9 = {
    'imie':'Rafał',
    'wiek':28,
    'wejscia':{'15.09.2026':2,'17.09.2026':4}
}

print(slownik_zagn9)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 9.9 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 9.9 - Tworzenie słowników.
# a) Stwórz słownik ksiazka z kluczami "tytul", "autor" i "rok", a potem go wyświetl.
ksiazka = {'tytul':'Lśnienie','autor':'Stephen King','rok':1977}
print(ksiazka)

# b) Stwórz ten sam słownik jeszcze raz, tym razem za pomocą dict().
ksiazka = dict(tytul='Lśnienie', autor='Stephen King', rok=1977)
print(ksiazka)

# c) Stwórz słownik ceny, w którym kluczami są nazwy trzech owoców, a wartościami ich ceny. Wyświetl cały słownik i cenę jednego owocu.
ceny = dict(banan=2.5, jablko=3.0, gruszka=1.5)
print(ceny)
print(ceny['banan'])

# d) Z listy krotek [("PL", "Polska"), ("DE", "Niemcy"), ("FR", "Francja")] zrób słownik kraje i wyświetl go.
lista = [("PL", "Polska"), ("DE", "Niemcy"), ("FR", "Francja")]
kraje = dict(lista)
print(kraje)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Pobieranie wartości ze słowników -----------------------------------------
# Zapis                    Gdy klucza nie ma
# slownik['klucz']         KeyError
# slownik.get('klucz')     None
# slownik.get('klucz', x)  wartość domyślna x
osoba_slownik_9 = {"imie": "Adam", "wiek": 25, "miasto": "Warszawa"}

# print(osoba_slownik_9['banan'])  # --> KeyError: 'banan'
if 'banan' in osoba_slownik_9:     # in sprawdza klucze słownika
    print(osoba_slownik_9['banan'])
else:
    print('Nie ma takiego klucza')
print(osoba_slownik_9['imie'])

print(osoba_slownik_9.get('imie'))
print(osoba_slownik_9.get('banan'))          # None --> gdy nie ma klucza
print(osoba_slownik_9.get('banan','brak'))   # brak --> wartość domyślna, gdy nie ma klucza

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 9.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 9.2 - Stwórz słownik oceny = {"Adam": 5, "Ola": 4, "Kasia": 3}. Pobierz ocenę Adama przez [] i
# ocenę Bartka przez .get() z domyślną wartością "brak".
oceny = {"Adam": 5, "Ola": 4, "Kasia": 3}
print(oceny['Adam'])
print(oceny.get('Bartek', 'brak'))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Iteracja po słownikach ---------------------------------------------------
osoba_iter9 = {"imie": "Adam", "wiek": 25, "miasto": "Warszawa"}

for i in osoba_iter9:           # --> domyślnie iterujemy po kluczach
    print(i)

for i in osoba_iter9.keys():    # --> klucze
    print(i)

for i in osoba_iter9.values():  # --> wartości
    print(i)

for klucz,wartosc in osoba_iter9.items():  # --> pary (klucz, wartość)
    print(f"Klucz:{klucz} - Wartość:{wartosc}")

# :: Zamiana na listę
print(list(osoba_iter9))           # ['imie', 'wiek', 'miasto']
print(list(osoba_iter9.keys()))    # ['imie', 'wiek', 'miasto']
print(list(osoba_iter9.values()))  # ['Adam', 25, 'Warszawa']
print(list(osoba_iter9.items()))   # [('imie', 'Adam'), ('wiek', 25), ('miasto', 'Warszawa')]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 9.1 - 9.8* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 9.1 - Stwórz słownik samochod z kluczami: marka, model, rok, kolor. Wyświetl każdą parę klucz-wartość.
samochod = {"marka": 'Opel', 'model':"astra", 'rok': 2025, 'kolor': 'czarny'}
for klucz, wartosc in samochod.items():
    print(f"Klucz:{klucz} - wartość: {wartosc}")

samochod = {"marka": "Toyota", "model": "Corolla", "rok": 2020, "kolor": "czarny"}
for klucz, wartosc in samochod.items():
    print(f"{klucz}: {wartosc}")

# 9.8* - Stwórz listę uczniowie, której elementami są słowniki: [{"imie": "Adam", "ocena": 4}, {"imie": "Ola", "ocena": 5}, ...].
# Wyświetl tylko uczniów z oceną 5 lub wyższą.
uczniowie = [
    {"imie": "Adam", "ocena": 4},
    {"imie": "Ola", "ocena": 5},
    {"imie": "Kasia", "ocena": 3},
    {"imie": "Bartek", "ocena": 5},
    {"imie": "Zofia", "ocena": 6}
]
for uczen in uczniowie:
    if uczen['ocena'] >= 5:
        print(uczen)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Modyfikacja zawartości słowników -----------------------------------------
# Słownik jest mutowalny, a jego klucze są zawsze unikalne
osoba_mod9 = {"imie": "Adam", "wiek": 25}

# :: Dodawanie i nadpisywanie przez []
osoba_mod9['email'] = 'naszemail@gmail.com'  # --> nowy klucz = dodanie
print(osoba_mod9)

osoba_mod9['imie'] = 'Mariusz'  # --> istniejący klucz = nadpisanie wartości
print(osoba_mod9)
osoba_mod9['Imie'] = 'Mariusz'  # --> wielkość liter ma znaczenie, to nowy klucz
print(osoba_mod9)

# :: update()
osoba_mod9.update(imie='Sebastian',pelnoletni=True)
print(osoba_mod9)
osoba_mod9.update({'imie':'Damian','email':'nietenemail@gmail.com'})
print(osoba_mod9)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 9.4 - 9.4B <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 9.4 - Poproś użytkownika o 3 imiona i 3 oceny. Zapisz je do słownika (imię jako klucz, ocena jako wartość). Wyświetl cały słownik.
"""
uczniowie = {}
for i in range(3):
    imie = input('Podaj imie: ')
    ocena = int(input('Podaj ocenę: '))  # int(), żeby ocena była liczbą, a nie napisem
    uczniowie[imie] = ocena
print(uczniowie)
"""

# 9.4B - Spróbuj dodać do słownika nową wartość za pomocą setdefault()
osoba_mod9 = {"imie": "Adam", "wiek": 25}
osoba_mod9.setdefault('imie','Damian')  # --> klucz już jest, więc nic się nie zmienia
osoba_mod9.setdefault('bank','PKOBP')   # --> klucza nie ma, więc zostaje dodany
print(osoba_mod9)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Usuwanie ze słowników: del, pop(), popitem(), clear() --------------------
# Sposób                  Co usuwa                                Zwraca
# del slownik['klucz']    parę o podanym kluczu                   nic (instrukcja)
# pop('klucz')            parę o podanym kluczu                   usuniętą wartość
# pop('klucz', x)         jw., ale gdy klucza nie ma - bez błędu  usuniętą wartość albo x
# popitem()               ostatnio dodaną parę                    krotkę (klucz, wartość)
# clear()                 wszystkie pary                          None
osoba = {"imie": "Alicja", "wiek": 35, "miasto": "Kraków", "email": "adam@mail.com"}

del osoba['email']
print(osoba)

# del osoba['email']  # --> KeyError: 'email'

zachowaj = osoba.pop('miasto')
print(osoba)
print(zachowaj)

# zachowaj_dwa = osoba.pop('miasto')  # --> KeyError: 'miasto'
zachowaj_dwa = osoba.pop('miasto','brak')
print(zachowaj_dwa)  # brak

zachowaj_trzy = osoba.popitem()
print(osoba)
print(zachowaj_trzy)  # ('wiek', 35)

osoba.clear()
print(osoba)  # {}

# :: Pułapka przy kopiowaniu (tak samo jak w listach)
a = {"x": 1, "y": 2}
b = a  # --> b to ten sam słownik, a nie kopia

print(a,b)

b['x'] = 20
print(a,b)  # --> zmieniły się oba

b = {"y": 99, "z": 3}
c = b.copy()  # --> kopia płytka: wystarczy, gdy w słowniku nie ma zagnieżdżonych słowników / list

print(b,c)
c['y'] = 20
print(b,c)  # --> zmienił się tylko c

# :: Łączenie słowników (Python 3.9+)
# klucze w słownikach są unikalne
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

# operator | - łączy, drugi nadpisuje
c = a | b
print(c)   # {'x': 1, 'y': 99, 'z': 3}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 9.3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 9.3 - Mając słownik magazyn = {"jabłka": 10, "banany": 5, "gruszki": 8}, dodaj "kiwi": 12, zmień ilość bananów na 15, usuń gruszki.
# Wyświetl po każdej operacji.
magazyn = {"jabłka": 10, "banany": 5, "gruszki": 8}
magazyn.setdefault('kiwi', 12)  # albo: magazyn['kiwi'] = 12
print(magazyn)
magazyn['banany'] = 15
print(magazyn)
del magazyn['gruszki']
print(magazyn)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Dict comprehension -------------------------------------------------------
# Działa jak list comprehension, tylko w {} i z parą klucz: wartość
lista_comprehension = [i for i in range(1,6)]
print(lista_comprehension)  # [1, 2, 3, 4, 5] --> dla porównania list comprehension

kwadraty = {x: x ** 2 for x in range(1, 6)}
print(kwadraty)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

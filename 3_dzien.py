# Python szkolenie - Podstawy (dzień 3)

# ==============================================================================
# Przypomnienie: pułapka z listami (modyfikowanie listy podczas iteracji)
# ==============================================================================

lista = [2,6,8,12,16]
lista_mieszna = [3, 5, 2,6,8, 9, 12,16]

for i in range(1,21):
    if i % 2 == 0:
       print(i)

# --- remove() w pętli - dlaczego tak nie robimy -------------------------------

print(f"Oryginalna lista: {lista}")
for i in lista:
    if i % 2 == 0:
        lista.remove(i)
print(f"Lista po zmianie: {lista}")

# remove() to nie używamy go w pętli do usuwania

# indeksy  0^  1^  2^  3   4
#elementy [6,  12, ]

# ==============================================================================
# 10. Zbiory (set)
# ==============================================================================

# --- Tworzenie zbiorów ---------------------------------------------------------
# Zbiór to nieuporządkowana kolekcja unikalnych elementów
# Każdy element zbioru jest unikalny

zbior10 = {} # Zawsze tworzy słownik
print(type(zbior10))

zbior10A = set()
print(type(zbior10A))

zbior10B = {2,6,3,8,2,6,3,5,2}
print(type(zbior10B))
print(zbior10B)

zbior10C = {'gruszka','jablko','python','wisnia','gruszka','jablko'}
print(zbior10C)

zbior10D = {2.5, 6.2 ,3.8, 6.2, 3.8, 3.8, 3.8, 3.8 ,3.8}
print(zbior10D)

zbior10E = {True,False,True}
print(zbior10E)

# --- Konwersje z innych typów złożonych ----------------------------------------
# Lista, słownik, string, krotka

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 10.1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 10.1 - Utwórz po jednej zmiennej każdego z poniższych typów, a następnie na ich podstawie utwórz odpowiadający im zbiór (set):

# :: string (dowolny tekst, np. z powtarzającymi się literami) → zbiór unikalnych liter
string_zadanie = ("Ala ma koty, koty lubią Ale. Ala ma psy, psy lubią Ale.")
print (type(string_zadanie))
string_zadanie = set(string_zadanie)
print (type(string_zadanie))
print (string_zadanie)

print('*'*20)

tekst = 'python'
zbior_tekst = set(tekst)
print(zbior_tekst)

print('*'*20)

tekst = "programowanie"
zbior_tekst = set(tekst)
print(tekst)
print(zbior_tekst)

print('*'*20)

string1 = 'bananowiec'
string1_to_set = set(string1)
print(f'String: {string1} | String zamiana set: {string1_to_set}')

# :: int → zastanów się, czy set() zadziała bezpośrednio na pojedynczej liczbie (spróbuj i sprawdź, co się stanie)
int_liczba = 7
# zbior_liczba = set(int_liczba) # TypeError: 'int' object is not iterable
# Integer nie możemy utworzyć jako set (tak samo bool pojedyńczy oraz float)

# :: lista (z kilkoma powtarzającymi się elementami) → zbiór bez duplikatów
lista = [1,2,3,4,2,4,1]

zbior_lista = set(lista)
print(zbior_lista)

print('*'*20)

list4 = ['jabłko','gruszka','banan','pomarańcza']
list4_to_set = set(list4)
print(type(list4_to_set))
print(f'Lista: {list4} | Lista zamiana set: {list4_to_set}')

# :: krotka (z kilkoma powtarzającymi się elementami) → zbiór bez duplikatów
print('*'*20)

krotka = (1, 2, 2, 3, 3, 4, 5)
zbior_krotka = set(krotka)
print(krotka)
print(zbior_krotka)

print('*'*20)

krotka5 = ('banan','jabłko','wiśnia')
krotka5_to_set = set(krotka5)
print(type(krotka5_to_set))
print(f'Krotka: {krotka5} | Krotka zamiana set: {krotka5_to_set}')

print('*'*20)

# :: słownik (przynajmniej 3 pary klucz-wartość) → jeden zbiór zrobiony z kluczy, drugi osobny zbiór zrobiony z wartości (.values())
dane = {
"imie": "Miłosz",
"wiek": 88,
"miasto": "Bydgoszcz"
}

dane_to_zbior_klucze = set(dane.keys())
dane_to_zbior_wartosci = set(dane.values())
print(f'Dane - słownik: {dane} | Klucze: {dane_to_zbior_klucze}, Wartości: {dane_to_zbior_wartosci}')

print('*'*20)

slownik_zadanie = {
    'imie': 'Marcin',
    'wiek': 28,
    'miasto': 'Gdańska'
}
print (type(slownik_zadanie))
#Wartości
slownik_zadanie_values = slownik_zadanie.values()
slownik_zadanie_values = set(slownik_zadanie_values)
print (type(slownik_zadanie_values))
print (slownik_zadanie_values)
#Klucze
slownik_zadanie_keys = slownik_zadanie.keys()
slownik_zadanie_keys = set(slownik_zadanie_keys)
print (type(slownik_zadanie_keys))
print (slownik_zadanie_keys)

# Dla każdego przypadku wypisz na konsoli zarówno zmienną oryginalną, jak i wynikowy zbiór, żeby zobaczyć różnicę.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 10.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 10.2 - Poproś użytkownika o zdanie. Policz ile unikalnych słów zawiera (ignorując wielkość liter). split()?
# list() --> dict() --> set()
"""
zdanie = input("Podaj zdanie: ")
slowa = zdanie.lower().split()
unikalne_slowa = set(slowa)
print(unikalne_slowa)
print(len(unikalne_slowa))
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Pułapka set() przy sortowaniu ---------------------------------------------
zbior10_sort = set('astmalubipluca')
print(zbior10_sort)

# Poprawny sort, ale liczymy się z tym, że będziemy mieli liste
print(sorted(zbior10_sort)) #--> zmiana typu danych na listę

# set to zbior nieuporzadkowanych elementów
print(set(sorted(zbior10_sort)))

# małe sety w postaci {1,2,3}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 10.3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 10.3 - Mając string "abrakadabra", znajdź ile unikalnych liter zawiera i wyświetl je posortowane.
string_zadanie2 = "abrakadabra"
string_zadanie2 = set(string_zadanie2)
print (f"Unikalne liter: {string_zadanie2} oraz ich ilość: {len(string_zadanie2)}, a posortowane: {sorted(string_zadanie2)}")

print('*'*20)

tekst = "abrakadabra"
unikalne_litery = set(tekst)
print(unikalne_litery)
print(len(unikalne_litery))
print(sorted(unikalne_litery))

print('*'*20)

string = 'abrakadabra'
string_zbior = set(string)
sorted(string_zbior)
print("unikalne litery: ", len(string_zbior), sorted(string_zbior))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Set comprehension ----------------------------------------------------------
lista_compr = [i for i in range(1,11)]
print(lista_compr)

set_compr = {i for i in range(1,11)}
print(set_compr)

# Unikalność długości nazwy zwierząt
lista_zwierzat = ['pies','lis','zaba','pajak','rosomak']
set_comprB = {len(zwierzecie) for zwierzecie in lista_zwierzat}
print(set_comprB)

# --- Modyfikowanie zawartości zbiorów (dodawanie) -------------------------------
# add() update()

# :: Dodawanie jednego
owoceset10 = {"jabłko", "banan"}
print(owoceset10)

owoceset10.add('gruszka')
print(owoceset10)

owoceset10.add('banan')
print(owoceset10)

# :: Dodawanie wielu elementów naraz (krotek, list, słowników)
owoceset10.update(['wisnia','agrest','banan'])
print(owoceset10)

owoceset10.update(('czerwony','zielony','banan'))
print(owoceset10)

owoceset10.update({'czerwony':23,'zielony':23,'banan':34}.values())
print(owoceset10)

owoceset10.update({'czerwony','zielony','niebieski'})
print(owoceset10)

# :: Pułapka --> zawsze podajemy krotki, listy, słowniki! Nigdy pojedyncze łańcuchy znaków, inty itp.
owoceset10.update('czerwony')
print(owoceset10)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 10.4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 10.4 - Masz pusty zbiór koszyk = set(). Dodaj do niego pojedynczo (przez add())
# trzy produkty: "chleb", "masło", "jajka". Następnie jednym wywołaniem update()
# dodaj naraz listę ["mleko", "ser", "chleb"] (zwróć uwagę, że "chleb" już tam jest
# - sprawdź, czy zbiór faktycznie nie wpuści duplikatu).
# Na koniec wyświetl zawartość koszyka i informację, ile jest w nim produktów.
koszyk = set()
koszyk.add("chleb")
koszyk.add("masło")
koszyk.add("jajka")
print(koszyk)
koszyk.update(["mleko", "ser", "chleb"] )
print(f'Zawartość koszyka: {koszyk} , ilość produktów: {len(koszyk)}')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Usuwanie elementów ze zbiorów ----------------------------------------------
# remove(), discard(), pop()

owocesetre10 = {"jabłko", "banan","agrest","wiśnia","telefon"}
print(owocesetre10)

# :: usuwanie jednego elementu
owocesetre10.remove('telefon')
print(owocesetre10)

# remove wywala błąd jak spróbujemy usunąć coś czego nie ma
# owocesetre10.remove('telefon') # KeyError: 'telefon'
# print(owocesetre10)

# :: discard używamy jako zabezpieczenie, gdy elementu może nie być w zbiorze
owocesetre10.discard('telefon')
print(owocesetre10)
owocesetre10.discard('wiśnia')
print(owocesetre10)

# :: pop() - zachowuje usunięty element
set_element = owocesetre10.pop()
print(owocesetre10)
print(set_element)

# pop Nie pozwala na wybranie dokładnego miejsca ktore chcemy usuwac
# set_element = owocesetre10.pop(2) TypeError: set.pop() takes no arguments (1 given)
# pop bierze losowy element z zbioru i go usuwa

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 10.5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 10.5 - Masz zbiór koszyk = {"chleb", "masło", "jajka", "mleko", "ser"}. Usuń z niego "masło" za pomocą remove().
# Spróbuj usunąć "cukier" (którego tam nie ma) najpierw przez remove() (zobacz błąd), a potem przez discard() (bez błędu).
# Na koniec użyj pop(), żeby usunąć i wyświetlić dowolny element, po czym wyczyść cały zbiór metodą clear() i wyświetl go na końcu.
koszyk = {"chleb", "masło", "jajka", "mleko", "ser"}
koszyk.remove('masło')
print(koszyk)
# koszyk.remove('cukier') KeyError: 'cukier'
print(koszyk)
koszyk.discard('cukier')
print(koszyk)
element_koszyk = koszyk.pop()
print(element_koszyk)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Zbiory - zaleta szybkości ---------------------------------------------------
duzy_zbior = set(range(1_000_000))
print(999_999 in duzy_zbior)
print(2_999_999 in duzy_zbior)

# --- Funkcja difference ----------------------------------------------------------
# difference() lub operator "-"

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.difference(b))
print(a-b)

print(b.difference(a))
print(b-a)

# :: symetryczna funkcja difference
print(a.symmetric_difference(b))
print(b^a)

# :: Przykład
set_ucznie = {'Adam','Maciej','Kuba','Elwira','Alicja','Monika'}
set_ucznie_zdali = {'Adam','Monika','Kuba'}

nie_zdali = set_ucznie - set_ucznie_zdali
print(nie_zdali)

# Utworzyli 3 pary zbiorów:
# - auta auta_naprawione
# - ucznie_lista uczniowie_na_wycieczke
# - lista_osob lista_osob_pelnoletnich
# użyć funkcji difference i wymienić:
# - auta nienaprawione,
# - uczniow, którzy nie jadą na wycieczkę
# - niepełnoletnich
# symetryczny przykład użycia
"""
auta = {'kia','fiat','audi', 'opel','toyota'}
auta_naprawione={'kia','audi'}
uczniowie_lista = {'Andrzej','Marek','Renata','Agata','Leszek','Radosław'}
uczn_wycieczka = {'Marek','Renata','Agata'}
lista_osob = {'Andrzej','Marek','Renata','Agata','Leszek','Radosław'}
osoby_pelnoletnie = {'Marek','Renata','Agata'}
print(auta.difference(auta_naprawione))
print(uczniowie_lista.difference(uczn_wycieczka))
print(uczniowie_lista.symmetric_difference(uczn_wycieczka))
print(lista_osob.difference(osoby_pelnoletnie))
"""
"""
auta = {"Ford", "BMW", "Audi", "Toyota", "Opel"}
auta_naprawione = {"BMW", "Toyota"}
nienaprawione = auta.difference(auta_naprawione)
print(nienaprawione)
uczniowie = {"Adam", "Ola", "Kasia", "Bartek", "Jan"}
uczniowie_wycieczka = {"Adam", "Kasia", "Jan"}
nie_jada = uczniowie - uczniowie_wycieczka
print(nie_jada)
lista_osob = {"Adam", "Ola", "Kasia", "Bartek", "Jan"}
lista_osob_pelnoletnich = {"Adam", "Bartek"}
niepelnoletni = lista_osob - lista_osob_pelnoletnich
print(niepelnoletni)
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.symmetric_difference(b))
print(a ^ b)
"""

auta = {'Audi', 'BMW', 'Mercedes', 'Renault', 'Mazda', 'Alfa Romeo'}
auta_naproawione = {'Audi', 'BMW', 'Renault'}
print (f"Auta nienaprawione: {auta.difference(auta_naproawione)}")
uczniowie_lista = {'Maciek', 'Kuba', 'Eliza', 'Wiola', 'Kamila'}
uczniowie_na_wycieczke = {'Kuba', 'Wiola', 'Kamila'}
print (f"Uczniowie którzy nie jadą na wyczieczkę {uczniowie_lista.symmetric_difference(uczniowie_na_wycieczke)}")
lista_osob = {'Mateusz', 'Kasia', 'Ania', 'Ala', 'Ola', 'Patryk'}
lista_osob_pelnoletnich = {'Mateusz', 'Patryk', 'Ala'}
print (f"Lista osób niepełnoletnich: {lista_osob.difference(lista_osob_pelnoletnich)}")

# --- Funkcja intersection --------------------------------------------------------
# intersection() --> część wspólna

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.intersection(b))
print(a & b)

# :: wiele zbiorów naraz
c = {5, 6, 7}
print(a & b & c)

# :: przykład
adam = {'Python','taniec','gry','bilard','polityka'}
ola = {'ogrodnictwo','mechanika','polityka','taniec'}

wspolne_hobby = adam & ola
print(wspolne_hobby)

# Utwórz dwa zbiory
#  studentów z projektami oraz wyświetl ich wspólne projekty
#  nauczycieli oraz ich wspólne klasy, które uczą
"""
student_adam = {'Programowanie', 'Ekologia', 'Integracja'}
student_milosz = {'Programowanie', 'Turystyka', 'Krajoznactwo', 'Integracja'}
wspolne_projekty = student_adam & student_milosz
print (wspolne_projekty)

nauczycielA = {'4A', '5B', '6C', '7D', '6A'}
nauczycielB = {'7A', '6D', '6C', '4A', '5B'}
wspolne_klasy = nauczycielA & nauczycielB
print (wspolne_klasy)
"""

"""
student1 = {'projekt4', 'projekt2', 'projekt3'}
student2 = {'projekt1', 'projekt3', 'projekt4'}
wspolne_projekty = student1 & student2
print(wspolne_projekty)


naucz1 = {'klasa1', 'klasa2', 'klasa3'}
naucz2 = {'klasa3', 'klasa4', 'klasa5'}
wspolne_klasy = naucz1.intersection(naucz2)
print(wspolne_klasy)
"""

"""
studentA = {'kalkulator', 'stronaWWW', 'aplikacja mobilna'}
studentB = {'aplikacja mobilna', 'dziennik budowy'}
print(studentA.intersection(studentB))
nauczycielA = {'3A', '3B', '2B'}
nauczycielB = {'3A', '1a', '2B'}
print(nauczycielA.intersection(nauczycielB))
"""

"""
ala = {'plan domu','mała architektura','transport atomów mionowych'}
aga = {'aplikacja biblioteczna','mała architektura'}
nauczyciele1 ={'1a','1b','2a','3a'}
nauczyciel2 = {'2a','3b'}
wspolne_projekty = ala & aga
print(wspolne_projekty)
wspolne_klasy = nauczyciele1 & nauczyciel2
print(wspolne_klasy)
"""

# --- Funkcja union -----------------------------------------------------------------
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.union(b))
print(a | b)

# :: wiele zbiorów naraz
c = {5, 6, 7}
print(a | b | c)

# Utwórz dwa zbiory nauczycieli z klasami, oraz 3 zbiory klientów ze sprzętem:
# sprawdź ile razem nauczyciele mają wszystkich klas
# sprawdź ile było łącznie naprawianych unikalnych sprzętów u 3 klientów
"""
nauczycielA = {'3A', '3B', '2B'}
nauczycielB = {'3A', '1a', '2B'}
klasy_razem = nauczycielB|nauczycielA
print("Razem klas: ", len(klasy_razem))
klient1 = {'pralka', 'lodowka', 'tv'}
klient2 = {'tv', 'mikrofala', 'ekspres do kawy'}
klient3 = {'suszarka', 'mikrofala', 'lodowka'}
naprawione_sprzety = klient1|klient2|klient3
print("Naprawione unikalne sprzęty łącznie: ", len(naprawione_sprzety))
"""

"""
nauczycielA = {'4A', '5B', '6C', '7D', '6A'}
nauczycielB = {'7A', '6D', '6C', '4A', '5B'}
wszystkie_klasy = nauczycielA | nauczycielB
print (wszystkie_klasy)

klientA = {'Smartphone', 'Telewizor', 'Komputer'}
klientB = {'Pralka', 'Zmywarka', 'Komputer'}
razem_AB = klientA | klientB
print (razem_AB)
"""

"""
nauczyciel1 = {"Matematyka", "Fizyka", "Informatyka", "Chemia"}
nauczyciel2 = {"Matematyka", "Historia", "Informatyka", "Biologia"}
wszystkie_klasy = nauczyciel1 | nauczyciel2
print(wszystkie_klasy)
klient1 = {"Laptop", "Monitor", "Drukarka"}
klient2 = {"Laptop", "Klawiatura", "Mysz"}
klient3 = {"Monitor", "Skaner", "Mysz"}
wszystkie_sprzety = klient1 | klient2 | klient3
print(wszystkie_sprzety)
"""

naucz1 = {'klasa1', 'klasa2', 'klasa3'}
naucz2 = {'klasa3', 'klasa4', 'klasa5'}
klient1 = {'toster','lodówka','pralka'}
klient2 = {'suszarka','lodówka','ekspres'}
klient3 = {'zmywarka','lodówka','ekspres'}
print(f'Łącznie klas: {len(naucz1 | naucz2)}')
print(f'Łącznie unikalnych sprzętów: {len(klient1 | klient2 | klient3)}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 10.9 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 10.9 - Mając dwa zbiory uczniów: grupa_a = {"Adam", "Ola", "Kasia", "Bartek"} i grupa_b = {"Ola", "Zofia", "Bartek", "Darek"},
# znajdź: kto jest w obu grupach, kto jest tylko w A, kto jest w którejkolwiek.
"""
grupa_a = {"Adam", "Ola", "Kasia", "Bartek"}
grupa_b = {"Ola", "Zofia", "Bartek", "Darek"}
print("tylko a grupie a: ", grupa_a-grupa_b)
print("tylko a grupie b: ", grupa_b-grupa_a)
print("w jakiejkolwiek grupie: ", grupa_a|grupa_b)
print("w obu grupach: ", grupa_a&grupa_b)
"""

grupa_a = {"Adam", "Ola", "Kasia", "Bartek"}
grupa_b = {"Ola", "Zofia", "Bartek", "Darek"}

print (f"W obu grupach są: {grupa_a | grupa_b}. \nTylko w grupie a są: {grupa_a - grupa_b}. \nW którejkolwiek są: {(grupa_a | grupa_b) - (grupa_a & grupa_b)}.")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Inne przydatne metody zbiorów ------------------------------------------------
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {6, 7}

# :: issubset - czy a jest podzbiorem b?
print(a.issubset(b))      # True - wszystkie elementy a są w b
print(a <= b)              # True - to samo

# :: issuperset - czy b jest nadzbiorem a?
print(b.issuperset(a))    # True
print(b >= a)              # True

# :: isdisjoint - czy zbiory nie mają wspólnych elementów?
print(a.isdisjoint(c))    # True - brak wspólnych
print(a.isdisjoint(b))    # False - mają wspólne

# :: frozenset - niezmienny zbiór (jak krotka dla listy)
zamrozony = frozenset(['gruszka','jablko','agrest','wisnia'])
print(zamrozony)
# zamrozony.add(7) # AttributeError: 'frozenset' object has no attribute 'add'

# ==============================================================================
# 11. Zaawansowane elementy przetwarzania list i zbiorów
# ==============================================================================

# --- List comprehension - zaawansowane techniki ---------------------------------
lista_compr = [i**2 for i in range(1,11)]
print(lista_compr)

# :: Transformacja
# Wypisać w liście P jak cyfra jest parzysta, N jak nie jest
wynik = ['P' if i % 2 == 0 else 'N' for i in range(1,11)]
print(list(range(1,11)))
print(wynik)

# :: Filtracja
wynik2 = [i**2 for i in range(1,11) if i % 2 == 0]
print(wynik2)

# :: Lista zagnieżdżona (spłaszczanie)
macierz = [[1,2,3],[3,4,5],[6,7,8]]
plaska = [element for wiersz in macierz for element in wiersz]
print(plaska)

for wiersz in macierz:
    for element in wiersz:
        print(element)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 1 - Mając listę temperatur [-5, 12, 0, 25, -2, 18, 30, -10], użyj list comprehension z if/else, żeby zamienić każdą wartość
# na etykietę: "zimno" (poniżej 15) lub "ciepło" (15 i więcej).
temperatury = [-5, 12, 0, 25, -2, 18, 30, -10]
wynik = ["zimno" if i < 15 else "ciepło" for i in temperatury]
print(wynik)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 2 - Mając listę liczb [4, 7, 2, 9, 15, 3, 22, 11, 8], jednym list comprehension (filtrowanie + transformacja razem)
# stwórz nową listę zawierającą podwojone wartości, ale tylko tych liczb, które są większe od 5.
liczby = [4, 7, 2, 9, 15, 3, 22, 11, 8]
wynik = [i * 2 for i in liczby if i > 5]
print(wynik)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Dict comprehension -----------------------------------------------------------
# można za pomocą comprehension szybko obrócić klucze-wartość
original = {'a':1,'b':2,'c':3}

odwrocony = {wartosc:klucz for klucz,wartosc in original.items()}
print(original,odwrocony )

oceny = {"Adam": 5, "Ola": 3, "Kasia": 4, "Bartek": 5, "Zofia": 2}
najlepsi = {klucz:wartosc for klucz,wartosc in oceny.items() if wartosc >=4}
print(najlepsi)

# --- map() ---------------------------------------------------------------------------
# map() --> do zmieniania szybkiego np. takiej listy jak liczby
liczby = [1, 2, 3, 4, 5]

# podwojone = map(lambda x: x*2 ,liczby) # brakuje czegoś
podwojone = list(map(lambda x: x*2 ,liczby))
print(podwojone)

potegi2 = list(map(lambda cyfra: cyfra**2 ,liczby))
print(potegi2)

# :: map() --> można robić to na wielu listach
a = [1, 2, 3]
b = [10, 20, 30]
sum_lista = list(map(lambda awartosc, bwartosc: awartosc+bwartosc, a, b))
print(sum_lista)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE - map() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Mając dwie listy: ceny = [100, 250, 80] i rabaty = [10, 50, 5],
# użyj map(), żeby policzyć ceny po rabacie (cena - rabat) dla każdej pary naraz.
ceny = [100, 250, 80]
rabaty = [10, 50, 5]
po_rabacie = list(map(lambda cenwart, rabwart : cenwart-rabwart, ceny, rabaty))
print(po_rabacie)

ceny = [100, 250, 80]
rabaty = [10, 50, 5]
cena_po_rabacie = list(map(lambda x_cena, y_rabat : x_cena - y_rabat, ceny,rabaty ))
print(cena_po_rabacie)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- filter() ------------------------------------------------------------------------
# filter() służy do filtrowania

slowa = ["kot", "hipopotam", "pies", "żyrafa", "mysz"]
# dlugie = filter(lambda s: len(s)>4, slowa) # zwraca brzydki obiekt zamiast listy
dlugie = list(filter(lambda s: len(s)>4, slowa))
print(dlugie)

produkty = [
    {"nazwa": "Laptop", "cena": 3500},
    {"nazwa": "Mysz", "cena": 50},
    {"nazwa": "Monitor", "cena": 1200},
    {"nazwa": "Kabel", "cena": 15}
]

drogie = list(filter(lambda drog: drog['cena'] > 100, produkty))
print(drogie)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE - filter() <<<<<<<<<<<<<<<<<<<<<<<<<<
# Mając listę słowników osoby = [{"imie": "Adam", "wiek": 17}, {"imie": "Ola", "wiek": 22}, {"imie": "Kasia", "wiek": 15},
# {"imie": "Bartek", "wiek": 30}], użyj filter(), żeby zostawić tylko osoby pełnoletnie (wiek >= 18).
osoby = [{"imie": "Adam", "wiek": 17}, {"imie": "Ola", "wiek": 22}, {"imie": "Kasia", "wiek": 15}, {"imie": "Bartek", "wiek": 30}]
pelnoletnie = list(filter(lambda lata: lata['wiek'] >=18, osoby))
print(pelnoletnie)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- sorted() / sort() z wartością key ------------------------------------------------
imiona = ["zofia", "Adam", "kasia", "Bartek"]
print(sorted(imiona, key=str.lower))

uczniowie = [
    {"imie": "Adam", "ocena": 4},
    {"imie": "Ola", "ocena": 5},
    {"imie": "Kasia", "ocena": 3}
]

# :: posortować malejąco
print(sorted(uczniowie, key=lambda u: u['ocena'], reverse=True ))

# :: posortować rosnąco
print(sorted(uczniowie, key=lambda u: u['ocena'] ))

dane = [("Adam", 4), ("Ola", 5), ("Kasia", 5), ("Bartek", 4)]
print(sorted(dane, key=lambda x: (-x[1],x[0])))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE - sorted() <<<<<<<<<<<<<<<<<<<<<<<<<<
# Masz listę imion: imiona = ["Bartek", "Zo", "Kasia", "Ala", "Krzysztof"].
# Posortuj ją od najkrótszego do najdłuższego imienia.
imiona = ["Bartek", "Zo", "Kasia", "Ala", "Krzysztof"]
print(sorted(imiona, key=lambda imie: len(imie), reverse=False))

print(sorted(imiona,key=len))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Sortowanie wieloprzebiegowe - kilka sort() po kolei ------------------------------
ludzie = [
    {"imie": "Jan",   "nazwisko": "Rybacki",    "wiek": 30, "pensja": 7000, "miasto": "Gdansk"},
    {"imie": "Anna",  "nazwisko": "Kowalska",  "wiek": 30, "pensja": 5000, "miasto": "Krakow"},
    {"imie": "Adam",  "nazwisko": "Kowalski",  "wiek": 30, "pensja": 6000, "miasto": "Krakow"},
    {"imie": "Adam",  "nazwisko": "Kowalski",  "wiek": 30, "pensja": 5500, "miasto": "Krakow"},
    {"imie": "Ola",   "nazwisko": "Nowak",     "wiek": 25, "pensja": 4000, "miasto": "Krakow"},
    {"imie": "Ala",   "nazwisko": "Abacka",   "wiek": 30, "pensja": 7000, "miasto": "Gdansk"},
]

ludzie_sort = ludzie.copy()
print(ludzie_sort)
ludzie_sort.sort(key=lambda u: u['imie'])
# print(ludzie_sort)
ludzie_sort.sort(key=lambda u: u['nazwisko'])
# print(ludzie_sort)
ludzie_sort.sort(key=lambda u: u['wiek'])
# print(ludzie_sort)
ludzie_sort.sort(key=lambda u: u['pensja'], reverse=True)
print(ludzie_sort)

# --- any() oraz all() -----------------------------------------------------------------
liczby = [1, 2, 3, 4, 5, 6, 7, 8]

# :: any() -> czy chociaż jeden element jest prawdziwy dla warunku
print(any(x % 2 == 0 for x in liczby))

# :: all() -> czy wszystkie są prawdziwe
print(all(x > 0 for x in liczby))
print(all(x > 3 for x in liczby))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE - any() i all() <<<<<<<<<<<<<<<<<<<<<<<
# Masz listę obecności na zajęciach: obecnosc = [True, True, False, True, True] (jedna wartość na osobę). Sprawdź za pomocą all(),
# czy wszyscy byli obecni, oraz za pomocą any(), czy przynajmniej jedna osoba była nieobecna (podpowiedź: not przed elementem).
print('*'*40)
obecnosc = [True, True, False, True, True]
print(all(i == True for i in obecnosc))
print(any(i == False for i in obecnosc))

print('*'*40)
print(all(obecnosc))
# print(any(obecnosc)) # --> True
print(any(not osoba for osoba in obecnosc))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- zip() i enumerate() - zaawansowane techniki --------------------------------------
imiona = ["Adam", "Ola", "Kasia"]
oceny = [5, 4, 3]

slownik = dict(zip(imiona,oceny))
print(slownik)

# :: enumerate
for index,i in enumerate(oceny,start=1):
    print(f'Index:{index} - wartość:{i}')

# ==============================================================================
# 12. Wyjątki i obsługa błędów
# ==============================================================================

# --- try/except - podstawowa obsługa --------------------------------------------------
# Wyjątki obsługujemy za pomocą formuły try / except

print('1 - przed try')
try:
    print('2 - w try')
    print(oceny[7]) # IndexError: list index out of range
    print('3 - po błędzie')
except:
    print('Program naciął się na błąd i nie wykona się dalej')

print('Witaj w Pythonie')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 12.1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 12.1 - Napisz program, który pyta użytkownika o rok urodzenia i oblicza jego wiek (przyjmij bieżący rok jako 2026).
# Jeśli użytkownik wpisze coś, co nie jest liczbą - wyświetl komunikat o błędzie zamiast pozwolić programowi się wysypać.
"""
try:
    rok_urodzenie = int(input('Podaj rok urodzenia:... '))
    wiek = 2026 - rok_urodzenie
    print(f"Masz {wiek} lat")
except:
    print("Podałeś niepoprawne dane!")
"""

# Dodatkowo - napisz program, który dzieli liczbę 100 przez liczbę podaną przez użytkownika. Jeśli użytkownik poda 0,
# wyświetl komunikat o błędzie zamiast pozwolić programowi się wysypać.
"""
cyfra_uzytkownik = input("Podaj cyfrę: ")
try:
    print (f"{100 / int(cyfra_uzytkownik)}")
except:
    print ("Podałeś błędną cyfrę")
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Łapanie konkretnego typu wyjątku - lepsza praktyka niż łapanie wszystkiego -------
"""
lista_index = [0,0,0,67,2,3,4]

cyfra_uzytkownik = input("Podaj cyfrę indexu: ")
try:
    cyfra = int(cyfra_uzytkownik)
    obliczenie = 100 / (lista_index[cyfra])
except ValueError:
    print('Wystąpił błąd podczas zmiany inputa na int: ValueError')
except ZeroDivisionError:
    print('Nie można dzielić przez zero')
except IndexError:
    print('Index poza listą')
"""

# :: Łapanie dwóch wyjątków razem
"""
lista_index = [0,0,0,67,2,3,4]

cyfra_uzytkownik = input("Podaj cyfrę indexu: ")
try:
    cyfra = int(cyfra_uzytkownik)
    obliczenie = 100 / (lista_index[cyfra])
except (ValueError, ZeroDivisionError):
    print('Wpisz poprawną liczbę różną od zera')
except IndexError:
    print('Index poza listą')
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 12.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 12.2 - Masz listę zakupów produkty = ["chleb", "mleko", "jajka"]. Napisz program, który pyta użytkownika o numer
# produktu (licząc od 1) i wyświetla jego nazwę. Obsłuż osobno dwa przypadki:
# użytkownik wpisał coś, co nie jest liczbą (ValueError), oraz podał numer spoza zakresu listy (IndexError).
"""
produkty = ["chleb", "mleko", "jajka"]
produkt = input('Podaj numer produktu: ')
print(produkt)
try:
    numer = int(produkt)
    print(produkty[numer-1])
except ValueError:
    print('Wpisano niepoprawną wartość, która nie jest liczbą')
except IndexError:
    print("Podales numer poza listą produktów")
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- try / except / else / finally ----------------------------------------------------
zmienna_wyj = 0

try:
    obliczenie = 100 / zmienna_wyj
except:
    print('Wystąpił błąd')
else: # else formuła wykonuje kod jak nie złapie żadnego wyjątku
    print('Kod tylko jak się powiedzie')
finally: # finally wykonuje kod na końcu zawsze
    print('kod się powiedzie finally')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 12.3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 12.3 - Napisz program, który pyta użytkownika o dwie liczby i mnoży je przez siebie.
# Użyj else, żeby wyświetlić wynik tylko wtedy, gdy nie było błędu, oraz finally, żeby zawsze
# (niezależnie od błędu) wyświetlić komunikat "Koniec obliczeń".
"""
liczbyinput = input('Podaj dwie liczby oddzielone przecinkiem: ')
liczba1 , liczba2 = liczbyinput.split(',')
try:
    int1 = int(liczba1)
    int2 = int(liczba2)
except ValueError:
    print('Nie podano wartości typu int')
else:
    print(f'Wynik: {int1 * int2}')
finally:
    print('Koniec obliczeń')
"""

"""
number_1 = input("Podaj 1 liczbę: ")
number_2 = input("Podaj 2 liczbę: ")
try:
    obliczenie_zadanie = int(number_1) * int(number_2)
except:
    print ('Wystąpił błąd')
else:
    print (f"Wynik mnożenia {int(number_1)} oraz {int(number_2)} wynosi {obliczenie_zadanie}")
finally:
    print ('Koniec obliczeń')
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Przykłady typowych wyjątków -------------------------------------------------------
# ZeroDivisionError - dzielenie przez zero
# print(10 / 0)

# ValueError - zły typ wartości
# int("abc")

# TypeError - operacja na niezgodnych typach
# "tekst" + 5

# IndexError - indeks poza zakresem listy
# lista = [1, 2, 3]
# print(lista[10])

# KeyError - klucz nie istnieje w słowniku
# slownik = {"a": 1}
# print(slownik["b"])

# FileNotFoundError - plik nie istnieje
# open("nie_istnieje.txt")

# NameError - zmienna nie istnieje
# print(zmienna_ktorej_nie_ma)

# --- Obiekt wyjątku - as e --------------------------------------------------------------
# Opisać lepiej błąd jaki występuje --> as e

try:
    zmienna_str = int('abc')
except ValueError as e:
    print(f'Typ błędu: {type(e).__name__}')
    print(f'Treść błędu: {e}')

# --- raise - rzucanie własnych wyjątków --------------------------------------------------
print('*'*20)

age11 = -5

try:
    if age11 < 0:
        raise ValueError('Wiek nie może być ujemny')
    if age11 > 110:
        raise ValueError('Wiek nie może być większy niż 110 lat')
    print(f'Wiek jest równy: {age11}')
except ValueError as e:
    print(e)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 12.5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 12.5 - Masz zmienną rabat z procentowym rabatem (np. rabat = 150). Jeśli rabat jest mniejszy niż 0 lub większy niż 100,
# rzuć ValueError z odpowiednim komunikatem. Przechwyć wyjątek za pomocą except ValueError as e i wypisz osobno typ błędu
# (type(e).__name__) oraz jego treść (e).
rabat = 150
try:
    if rabat < 0 or rabat > 100:
        raise ValueError("Rabat musi być w przedziale 0-100")
    print(f"Rabat: {rabat}%")
except ValueError as e:
    print("Typ błędu:", type(e).__name__)
    print("Treść błędu:", e)

rabat = 150
print('Rabat wynosi:', rabat)
try:
    if rabat <0:
        raise ValueError('Rabat jest mniejszy niż 0')
    if rabat >100:
        raise ValueError('Rabat jest większy niż 100')
except ValueError as e:
    print(f'Typ błędu: {type(e).__name__}')
    print(f'Treść błędu: {e}')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Pętla z obsługą wyjątków ------------------------------------------------------------
"""
while True:
    try:
        wiek = int(input("Podaj swój wiek: "))
        if wiek < 0 or wiek > 150:
            print("Wiek musi być między 0 a 150!")
            continue
        break
    except ValueError:
        print("To nie jest liczba! Spróbuj ponownie.")

print(f"Twój wiek: {wiek}")
"""

# --- Hierarchia wyjątków ------------------------------------------------------------------
# BaseException
#   └── Exception
#         ├── ValueError
#         ├── TypeError
#         ├── KeyError
#         ├── IndexError
#         ├── FileNotFoundError
#         ├── ZeroDivisionError
#         ├── AttributeError
#         ├── RuntimeError
#         └── ... (i wiele innych)

# UWAGA: nigdy nie łap BaseException - to złapie też Ctrl+C (KeyboardInterrupt)

# ==============================================================================
# 13. Funkcje
# ==============================================================================

# --- Deklarowanie funkcji -------------------------------------------------------------
# nie można wywołać przed deklaracją
# przywitaj() # NameError: name 'przywitaj' is not defined

def przywitaj():
    print('Cześć!')

przywitaj()
przywitaj()
przywitaj()
przywitaj()
przywitaj()

przywitaj = przywitaj()
print(przywitaj) # None --> zwraca None z zmiennej

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 13.1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 13.1 - Napisz funkcję powitanie(), która pyta użytkownika o imię (input()) i wyświetla Cześć [imie]!. Wywołaj ją 3 razy.
def powitanie():
    Hello = input("Podaj swoje imię: ")
    print (f"Cześć {Hello}!\nCześć {Hello}!\nCześć {Hello}!")

"""
powitanie()
powitanie()
powitanie()
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 13.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 13.2 - Napisz funkcję linia_separatora(), która wypisuje linię złożoną z 30 znaków = (wykorzystaj mnożenie stringa: "=" * 30).
def linia_separatora():
    print("*" * 30)
linia_separatora()
linia_separatora()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Zwracanie wyników z funkcji - return ---------------------------------------------
def oblicz_sume():
    wynik = 3+8
    return wynik
    wynik = 4+8 # NIGDY SIĘ NIE WYKONA
    wynik = 3+9 # NIGDY SIĘ NIE WYKONA

oblicz_sume()
print(oblicz_sume())
zmienna_oblicz = oblicz_sume()
print(zmienna_oblicz)

# :: return vs print
def dodaj_print():
    print(3 + 5)       # wyświetla, ale nie zwraca

def dodaj_return():
    return 3 + 5       # zwraca, ale nie wyświetla

x = dodaj_print()    # wyświetli 8, ale x = None
y = dodaj_return()   # nie wyświetli nic, ale y = 8

# :: Zwracanie wielu wartości - Python automatycznie pakuje je w krotkę
# print(lisfun) # zmienna nie istnieje poza funkcją
def policz_min_max():
    lisfun = [2,5,6,4,3]
    return min(lisfun),max(lisfun)
# print(lisfun) # zmienna nie istnieje poza funkcją

wynik = policz_min_max()
print(wynik)

mi,ma = policz_min_max()
print(mi,ma)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 13.4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 13.4 - Napisz funkcję oblicz_iloczyn(), która oblicza iloczyn liczb 4 i 7 i zwraca wynik
# (bez parametrów - liczby na sztywno w środku funkcji).
def oblicz_iloczyn():
    Iloczyn = 4 * 7
    return Iloczyn

print(oblicz_iloczyn())

def oblicz_iloczyn():
    ilo = 4 * 7
    return (ilo)
spr_oblicz_iloczyn = oblicz_iloczyn()
print(spr_oblicz_iloczyn)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 13.6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 13.6 - Napisz funkcję info_o_tekscie(), która dla
# stałego tekstu "Python" zwraca dwie wartości naraz: jego długość oraz wersję pisaną wielkimi literami.
def info_o_tekscie():
    tekzad = 'Python'
    return len(tekzad), tekzad.upper()
print(info_o_tekscie())

def info_o_tekscie():
    txt = 'Python'
    return len(txt), txt.upper()
dlugosc, wielkie_litery = info_o_tekscie()
print(f'Długość tekstu: {dlugosc}')
print(f'Tekst wielkimi: {wielkie_litery}')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Parametry / argumenty funkcji ----------------------------------------------------
""" # druga nazwana tak samo funkcja może nadpisać pierwszą co potem może powodować błędy
def przywitaj_osobe():
    print('Pierwsza funkcja')

def przywitaj_osobe():
    print('Druga funkcja')

przywitaj_osobe()
"""

def przywitaj_osobe(imie): # parametr w funkcji
    print(f'Witaj {imie}')

# przywitaj_osobe() # TypeError: przywitaj_osobe() missing 1 required positional argument: 'imie'
przywitaj_osobe('Krystian') # argument który przekazujemy
# przywitaj_osobe('Krystian','Klaudia') # TypeError: przywitaj_osobe() takes 1 positional argument but 2 were given

# str_example_len = 'abrada'
# print(len(str_example_len,'abrada')) # TypeError: len() takes exactly one argument (2 given)

def przywitaj_osobe_z_wiekiem(imie,wiek): # parametr w funkcji
    print(f'Witaj {imie}, masz {wiek} lat')

przywitaj_osobe_z_wiekiem('Damian',29)
# przywitaj_osobe_z_wiekiem('Damian') TypeError: przywitaj_osobe_z_wiekiem() missing 1 required positional argument: 'wiek'
# przywitaj_osobe_z_wiekiem('Damian',29,34,25,45) TypeError: przywitaj_osobe_z_wiekiem() takes 2 positional arguments but 5 were given

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 13.9 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 13.9 - Napisz funkcję pole_prostokata(a, b), która zwraca (return) pole prostokąta. Wyświetl wynik.
def pole_prostokata(a, b):
    return a * b
print (f"Pole prostokąta 3 na 4 wynosi: {pole_prostokata(3,4)}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 13.12 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 13.12 - Napisz funkcję odwroc(tekst), która zwraca odwrócony string. Np. "Python" → "nohtyP".
def odwroc(tekst):
    print(tekst[::-1])
    return tekst[::-1]
odwroc('Python')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Wartości domyślne parametrów -----------------------------------------------------
def wartosci_domyslne(imie,wiek=59):
    print(f'Witaj {imie}, masz {wiek}')

wartosci_domyslne('Renata')
wartosci_domyslne('Kamil',20)
# wartosci_domyslne('Kamil',20,23)TypeError: wartosci_domyslne() takes from 1 to 2 positional arguments but 3 were given
# wartosci_domyslne() # TypeError: wartosci_domyslne() missing 1 required positional argument: 'imie'

# Wartości domyślne zawsze po wszystkich wymaganych argumentach
# def wartosci_domyslne_blad(imie=23,wiek): # SyntaxError: parameter without a default follows parameter with a default
#     print(f'Witaj {imie}, masz {wiek}')

def wartosci_domyslne_wiele(imie,wiek=23,pelnoletni=True,prawo_jazdy=False):
    print(f'Witaj {imie}, masz {wiek}, jesteś {'pełnoletni/a' if pelnoletni else 'niepelnoletni/a'},{'masz' if pelnoletni else 'nie masz'} prawo jazdy')

wartosci_domyslne_wiele('Patrycja')

# --- *args i **kwargs ------------------------------------------------------------------
def pierwszy_przypadek(*args):
    print(f'Argumenty opakowane w krotkę {args}') # args przekazane z parametru to przekazane argumenty opakowane w krotkę
    print(f'Argumenty opakowane w krotkę  podane rozpakowaniu', end=' ')
    print(*args)

    print(sum(args))

# pierwszy_przypadek(2)
# pierwszy_przypadek(2,5)
pierwszy_przypadek(2,5,7,5,6,3,6,3,7.6,2)

def drugi_przypadek(**kwargs):
    # print(kwargs)
    for klucz,wartosc in kwargs.items():
        print(f'K: {klucz}, W:{wartosc}')

drugi_przypadek(imie='Jan',nazwisko='Kowalski',wiek=29,prawo_jazdy=True)

def trzeci_przypadek(imie,wiek,prawo_jazdy=True,*args,**kwargs): # ustawienie poprawne
    pass

# --- Dokumentowanie funkcji - docstring -------------------------------------------------
def oblicz_iloczyn(a,b):
    """Funkcja jest odpowiedzialna za liczenie iloczonu przy pomocy przesłanych dwóch argumentów"""
    return a + b

def oblicz_iloczyn2(a,b):
    """
    Funkcja jest odpowiedzialna za liczenie iloczonu przy pomocy przesłanych dwóch argumentów
    Funkcja jest odpowiedzialna za liczenie iloczonu przy pomocy przesłanych dwóch argumentów
    Funkcja jest odpowiedzialna za liczenie iloczonu przy pomocy przesłanych dwóch argumentów
    Przekazywane są dwa argumenty nie sprawdzane czy są intem, bez ochrony try/except
    """
    return a + b

help(oblicz_iloczyn)

help(oblicz_iloczyn2)

help(len)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 13.13 - 13.15 <<<<<<<<<<<<<<<<<<<<<<<<<<
# 13.13 - Napisz funkcję srednia(*args), która przyjmuje dowolną liczbę liczb i zwraca ich średnią.
# Dodaj rozbudowany docstring z Args i Returns.

# 13.15 - Napisz funkcję podsumowanie(**kwargs), która wypisuje wszystkie przekazane dane w formacie klucz: wartość (jedna linia na parę),
# a na końcu wypisuje, ile argumentów zostało przekazanych.

# \* prze argumentem
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

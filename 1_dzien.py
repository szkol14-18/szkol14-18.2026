# Python szkolenie - Podstawy

# ==============================================================================
# 1. Środowisko pracy
# ==============================================================================

# --- Przydatne skróty klawiaturowe --------------------------------------------
# Ctrl + /      Wykomentowanie linijki
# Ctrl + \      Podział edytora na dwa okna
# Ctrl + C      Kopiowanie do schowka
# Ctrl + V      Wklejanie ze schowka
# Ctrl + S      Zapisz plik
# Ctrl + Z      Cofanie zmian
# Ctrl + Y      Ponowienie zmian (do przodu)
# Ctrl + +      Powiększenie okien
# Ctrl + -      Pomniejszenie okien
# Ctrl + `      Otwarcie / zamknięcie terminala
# End           Kursor na koniec linii
# Home          Kursor na początek linii
# Tab           Przesuwanie dalej części kodu do przodu
# Shift + Tab   Przesuwanie dalej części kodu do tyłu

# ==============================================================================
# 2. "Hello world" i pisanie na konsoli
# ==============================================================================

# :: Printowanie w konsoli
# print('python')
print('python') # print() --> print('') print("")
print()
print('python')

print(35)

print(466,254,234)

print('Python jest super')

# :: Znaki specjalne
print('Python jest \nsuper')
print('Python jest \tsuper')
print('Python jest \'super\' ')
print('Python jest \"super\" ')
# print('Python jest 'super' ') --> wywala błąd
print('Python jest "super" ')
print("Python jest 'super' ")
print("Python jest \\super\\ ")

# Ściągawka znaki specjalne:
# Znak   Działanie
# \n     Nowa linia
# \t     Tabulator
# \\     Pojedynczy backslash
# \"     Cudzysłów w stringu
# \'     Apostrof w stringu

# :: Parametr end
print('Python jest lepszy niż Java',end='')
print(' haha ')

# :: Parametr sep
print("Adam", "Ewa", "Kasia")
print("Adam", "Ewa", "Kasia",sep='*')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 2.1 - 2.4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
"""
# 2.1 - Wyświetl swoje imię
print("Imię: Mateusz")

print("Dawid")

print("Przemysław")

print('Beata')

# 2.2 - Wyświetl imię ulubionej postaci, a w kolejnych liniach: nazwisko, wiek, ulubioną książkę (w cudzysłowie)
print("Ulubiona postać: Iron Man \nNazwisko: Olejniczak \nWiek: 29 \nUlubiona książka: \"TO\" ")

print('UlubionaPostać \nŻurek \n30lat \n"Lśnienie"')

print("Harry")
print('Potter')
print(17)
print('"Harry Potter i Kamień Filozoficzny"')

print('Kubus \nPuchatek \n10 \n"Ogniem i mieczem"')

# 2.3* - Wyświetl liczbę 5, a następnie wyświetl w konsoli działanie dodawania 5 i 3
# print(5)
# print(5, ' + ', 3) --> nie błąd, ale wypisze tylko "5  +  3", nie policzy wyniku (' + ' to napis)

print(5, "\nWynik działania 5 + 3 to:", 5+3)

print(5)
print(5+3)

# 2.4 - Wyświetl dzisiejszą datę wrzucająć kilka tekstów po przecinku w princie i dodaj separator '-'
print("14","09","2026",sep='-')

print("Dzisiaj", "jest", "14", "09", "2026", sep="-")
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# :: Działania na liczbach
print(5+3) # Dodawanie
print(5-10) # Odejmowanie
print(6*3) # Mnożenie
print(14/5) # Dzielenie
print(14//5) # Dzielenie całkowite (zaokrąglone w dół: 14//5 --> 2, -14//5 --> -3)

# :: Działania na stringach
print('Ala'+'ma'+'kota') # --> sep nie działa
# print('Ala'+5) # pomieszane typy, nie działa
# print('Ala'-5) # pomieszane typy, nie działa

# print('nie'-'n') # Python nie wspiera operacji odejmowania na stringach

print("Ala"*45)
# print("Ala"/4) # Nie ma operacji dzielenia na str

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 2.7 - 2.9 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 2.7 - Wykonaj w konsoli działanie 3 * 15 * 99 / 121 + 3
print(3 * 15 * 99 / 121 + 3)

print(round((3 * 15 * 99 / 121 + 3),2)) # round Zaokrąglanie do najbliższej liczby (tu do 2 miejsc po przecinku)

# Uwaga: przy równej połówce round zaokrąga do liczby parzystej (tzw. zaokrąglanie bankierskie)
print(round(2.5)) # 2 --> a nie 3!
print(round(3.5)) # 4
print(round(0.5)) # 0

# 2.5 - Napraw: print("Teraz mamy przyzwolenie numer" + 593)
print("Teraz mamy przyzwolenie numer" + " 593") # docelowo: str(593) - konwersja typów niżej

# 2.6 - Napraw: print("57" + 35)
print(57 + 35) # docelowo: int("57") + 35 - konwersja typów niżej

# 2.9 - Wyświetl prostokąt z gwiazdek * o szerokości 5 i wysokości 3
print("*"*5)
print("*"*5)
print("*"*5)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ==============================================================================
# 3. Zmienne i typy danych
# ==============================================================================

# --- Zmienne ------------------------------------------------------------------
# print(x) # --> odnosienie się przed deklaracją zmiennej wywali błąd
x_31 = 15
print(x_31)
x_32 = 'Ala'
print(x_32)

# :: f-string print
print(f'Ala ma {x_31}')
print('Ala ma ' + str(x_31) + " i jest super")
print(f'{x_32} ma {x_31}')
print(f'Wiek: {x_31} - bez 10 lat - {x_31-10}')

print("*"*20)

print(x_31)
x_31 = 15-10
print(x_31)

print("*"*20)

# :: Input
# numer_buta_3 = input("Podaj numer twojego buta:")
# print(f"Numer buta użytkownika to: {numer_buta_3}")

# print(input("Podaj numer twojego buta:"))

# Poproś użytkownika o bok kwadratu, a następie daj jego kwadrat
# Input zawsze zwraca string, napis
# bok_kwadratu_3 = input("Podaj bok kwadratu:")
# print(f"Kwadrat boku to: {int(bok_kwadratu_3)**2}")

# bok_kwadratu_3A = int(input("Podaj bok kwadratu:"))
# print(f"Kwadrat boku to: {bok_kwadratu_3A**2}")

# :: Konwersja typów (int, str, bool)
zmienna_str_3 = '35'
zmienna_int_3 = 35
print(int(zmienna_str_3))
print(str(zmienna_int_3))

# bool --> True, False
# zmienna_bool = bool(input("Podaj coś:")) # --> zawsze zwróci True jak użytkownik cokolwiek wpisze

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 3.1 - 3.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 3.1 - Za pomocą input() zapytaj użytkownika (o wybrany aspekt) i go wyświetl
# dane = input("Podaj swoje imię: ")
# print(dane)

# rok = 2026
# ur = int(input("Podaj datę urodzenia:"))
# print(f"Masz {rok - ur} lat")

# miasto = input("Podaj miasto w jakim mieszkasz:")
# print(f"{miasto}")

# kolor_wlosow = input("Podaj swój kolor włosów: ")
# print(kolor_wlosow)
# print(type(kolor_wlosow))
# print("*"*20)

# 3.2* - Za pomocą input() zapytaj o bok a i bok b prostokąta, następnie oblicz pole
# bok_a = int(input("Podaj bok a:"))
# bok_b = int(input("Podaj bok b:"))
# print(f"pole prostokąta wynosi:{bok_a * bok_b}")
# print(f"obwód prostokąta wynosi:{bok_a*2+bok_b*2}")

# bok_a = int(input("Podaj wartość boku prostokąta a: "))
# bok_b = int(input("Podaj wartość boku prostokąta b: "))
# print(f"Pole prostokąta to {bok_a * bok_b}")

# a = int(input("Podaj bok a: "))
# b = int(input("Podaj bok b: "))
# print(f"Pole prostokąta wynosi: {a * b}")
# print("*" * 20)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# :: Cechy zmiennych
# Można przypisać napisy i liczby, ale nie tylko
# Wielkość liter ma znaczenie (name ≠ Name)
# Nazwy najlepiej po angielsku
# Kilka wyrazów łączymy w jeden ciąg (snake_case)
# Wartość zmiennej jest edytowalna

# :: Konwencja nazewnictwa
# Styl         Przykład    Gdzie używany
# snake_case   moje_imie   Zmienne i funkcje w Pythonie
# camelCase    mojeImie    JavaScript
# PascalCase   MojeImie    Nazwy klas w Pythonie

# :: Poprawne nazewnictwo w pythonie zmiennych
# wiek                      # jeden wyraz
# first_name                # dwa wyrazy
# liczba_punktow_koncowych  # trzy wyrazy
# gracz1                    # wyraz + cyfra
# total_score_2             # wiele wyrazów + cyfra
# _prywatna_zmienna         # podkreślnik na początku
# max3_proby                # cyfra w środku

# :: Złe nazewnictwo w pythonie
# Niedozwolone --> SyntaxError
# 2gracz          # zaczyna się od cyfry
# imie studenta   # zawiera spację
# moje-imie       # zawiera myślnik
# suma!punktow    # znak specjalny (!)
# class           # słowo zastrzeżone Pythona

# Dozwolone, ale niezgodne z konwencją --> zadziała, lepiej unikać
# średnia_ocen    # polski znak (ś) - nazwy piszemy bez polskich znaków
# Imie_Studenta   # wielkie litery - zmienne piszemy snake_case (imie_studenta)

# :: Przypisywanie wielu zmiennych
pierwszy, drugi = 23,57

print(pierwszy,drugi)

# :: Słowa zastrzeżone (keyword)
import keyword

print(keyword.kwlist)

# --- Typy danych --------------------------------------------------------------
# Typ       Opis                        Przykład
# str       Tekst                       "Alicja ma kota"
# int       Liczba całkowita            23, -74
# float     Liczba zmiennoprzecinkowa   25.764, 24.4
# complex   Liczba zespolona            3 + 25j, 25j
# bool      Wartość logiczna            True, False

# :: type()
print(type("Ala")) # --> str
print(type(5)) # -->int
print(type(24.5)) # --> float (część dziesiętną oddzielamy kropką, nie przecinkiem!)
print(type(25j)) # --> complex (zespolona)
print(type(True)) # --> bool

# Dla bool tylko --> True False

# --- Typy liczbowe ------------------------------------------------------------
# Zaokrąglanie
float_example_3A = 19.5
print(f"{float_example_3A:.0f}")  # 20 --> .0f formatowanie tekstowe, wynik to napis (str)
print(f"{float_example_3A:.10f}") # 19.5000000000
float_example_3AA = f'{float_example_3A:.10f}'
print(type(float_example_3AA))    # <class 'str'> --> na tym już nie policzymy
print(float_example_3A * 2)       # 39.0 --> oryginalna zmienna dalej jest floatem, formatowanie jej nie zmienia

print(f"{18.5:.0f}")              # 18 --> formatowanie też zaokrąga połówkę do parzystej

print("*float-round*"*10)
float_example_3B = 19.5
print(f'{float_example_3B}')      # 19.5
float_example_3B = round(19.5)
print(f'{float_example_3B}')      # 20 --> round bez miejsc po przecinku zwraca int, nie float
print(round(18.5))                # 18 --> połówka do parzystej
print(round(19.5, 1))             # 19.5 --> z miejscami po przecinku zostaje float
print("*float-round*"*10)

# :: Bool
print(bool(''))
print(bool('False'))

# input("podaj cos:")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 3.4 - 3.9A <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 3.4 - Stwórz zmienne: a34 = 10, b34 = 3.14, c34 = "Python", d34 = True. Wyświetl typ każdej z nich za pomocą type().
a34 = 10
b34 = 3.14
c34 = "Python"
d34 = True
print(f'zmienna a34: {type(a34)}, zmienna b34: {type(b34)}, zmienna c34: {type(c34)}, zmienna d34: {type(d34)}')

a34 = 10
b34 = 3.14
c34 = "Python"
d34 = True
print(type(a34))
print(type(b34))
print(type(c34))
print(type(d34))

# 3.6 - Poproś użytkownika o dwie liczby (input). Oblicz i wyświetl: sumę, różnicę, iloczyn oraz iloraz (z dokładnością do 2 miejsc po przecinku).
"""
liczba_1 = float(input("podaj pierwszą liczbę:"))
liczba_2 = float(input("podaj drugą liczbę:"))
print(f"Suma wynosi:{liczba_1+liczba_2:.2f}")
print(f"Różnica wynosi:{liczba_1-liczba_2:.2f}")
print(f"Iloczyn wynosi:{liczba_1*liczba_2:.2f}")
print(f"Iloraz wynosi:{liczba_1/liczba_2:.2f}")

print("Podaj dwie liczby")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
print(f'Obliczona suma: {a + b}')
print(f'Obliczona różnica: {a - b}')
print(f'Obliczony iloczyn: {a * b}')
print(f'Obliczony iloraz: {a / b:.2f}')

number1 = int(input("Podaj pierwszą liczbę: "))
number2 = int(input("Podaj drugą liczbę: "))
print(f'Suma liczb: {number1 + number2:.2f} \nRóżnica liczb: {number1 - number2:.2f} \nIloczyn liczb: {number1 * number2:.2f} \nIloraz liczb: {number1 / number2:.2f}')
"""

# 3.8A - BMI = masa / (wzrost * wzrost). Napisz program, który odbierze od użytkownika jego masę w kilogramach i wzrost w metrach, wyliczy i
# wypisze BMI.
"""
masa = float(input("Podaj wagę w kg: "))
wzrost = float(input("Podaj wzrost w metrach: "))
bmi = masa / (wzrost * wzrost)
print(f'Twoje BMI wynosi: {bmi:.2f}')
"""

# 3.9A - Poproś użytkownika o temperaturę w stopniach Celsjusza. Przelicz ją na stopnie Fahrenheita według wzoru F = C * 9/5 + 32
# i wyświetl wynik z dokładnością do 1 miejsca po przecinku.
"""
c = float(input("Podaj temperaturę w stopniach Celsjusza: "))
f = c * 9 / 5 + 32
print(f"Temperatura w Fahrenheitach: {f:.1f}")

temp = float(input("Podaj temperaturę w stopniach Celsjusza: "))
temp_F = temp*9/5 + 32
print(f"Temperatura w stopniach Fahrenheita wynosi: {temp_F:.1f}")

temperature = float(input("Podaj temperaturę w stopniach Celsjusza: "))
fahrenheit = temperature * 9/5 + 32
print(f'{temperature} stopni Celsjusza to {fahrenheit:.1f} stopni Fahrenheita')
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ==============================================================================
# 4. Instrukcje warunkowe
# ==============================================================================

# :: Operatory porównania
# Operator   Znaczenie            Przykład   Wynik
# ==         Równe                5 == 5     True
# !=         Różne (nierówne)     5 != 3     True
# >          Większe              5 > 3      True
# <          Mniejsze             5 < 3      False
# >=         Większe lub równe    5 >= 5     True
# <=         Mniejsze lub równe   3 <= 5     True

print("***Instrukcje***"*10)
x_int4 = 10
print(x_int4 == 10) # True
print(x_int4 != 5)  # True
print(x_int4 > 20)  # False
print(x_int4 < 20)  # True
print(x_int4 >= 10) # True
print(x_int4 <= 2)  # False

print("***str***"*5)
x_str4 = 'ala'
print(x_str4 == 'ala') # True
print(x_str4 == 'Ala') # False
print(x_str4 > 'Ala') # True (późniejszy materiał)

# --- Jeden warunek ------------------------------------------------------------
age_4 = 20

if age_4 == 20: # --> pass pozwala na przygotowanie if bez błędu
    pass

if age_4 == 20:
    print(f"Wiek to {age_4} lat")

if age_4 != 20:
    print("Wiek osoby nie jest równy 20 lat")

# --- Else ---------------------------------------------------------------------
print("***else***"*5)
age_4A = 9

if age_4A >= 18:
    print("Osoba jest pełnoletnia")
else:
    print("Osoba jest niepełnoletnia")

# --- Wiele warunków -----------------------------------------------------------
# instrukcja warunkowa elif
print("***elif***"*5)
grade_4 = 5

if grade_4 == 6:
    print("Celujący")
elif grade_4 == 5:
    print("Bardzo Dobry")
elif grade_4 == 4:
    print("Dobry")
else:
    print('Niedostateczny')

# --- Operatory logiczne w warunkach -------------------------------------------
# Operatory logiczne and, or, not + operatory is (tożsamość) i in (przynależność)
# Operator   Rodzaj            Znaczenie
# and        logiczny          oba warunki muszą być True
# or         logiczny          co najmniej jeden warunek musi być True
# not        logiczny          negacja (True <-> False)
# is         tożsamości        czy to ten sam obiekt (używamy głównie z None)
# in         przynależności    czy element znajduje się w napisie / liście

# :: Operator and --> oba warunki muszą zwracać True
grade_4B = 18
prawo_jazdy = True

if grade_4B >= 18 and prawo_jazdy:
    print("Osoba jest pełnoletnia i posiada prawo jazdy")

grade_4C = 18
prawo_jazdyB = False

if grade_4C >= 18 and prawo_jazdyB:
    print("Nie ma nie ma nie ma nie ma ")

# :: Operator or --> co najmniej jeden warunek musi zwracać True
grade_4D = 18
prawo_jazdy_motocykl = False

if grade_4D >= 18 or prawo_jazdy_motocykl:
    print("Przeszedł warunek or")
else:
    print("Warunek or nie przeszedł")

# :: Operator not --> negacja
if not prawo_jazdy_motocykl:  # not False --> True, więc blok się wykona
    print('Brak prawa jazdy na motocykl, sprawdzenie not')

# :: Operator is
# operator is sprawdza czy to ten sam obiekt, używamy go do None (is None / is not None)
zmienna4_none = 'sdfsa'
print(zmienna4_none)

if zmienna4_none is None:
    print("Nie ma danych")

if zmienna4_none is not None:
    print("Wykonaj jakiś kod na tej przekazanej zmiennej")

x_is_example1 = int("278")
x_is_example2 = int("278")

print(x_is_example1 == x_is_example2)  # True --> te same wartości
print(x_is_example1 is x_is_example2)  # False --> dwa różne obiekty w pamięci

# Zalecane == do porównywania wartości, is tylko do None

# :: Operator in --> sprawdza czy jakaś wartość jest w środku
str_example_4 = 'Python jest super'

if 'super' in str_example_4:
    print('super jest w podannej zmiennej')

lista_example_4 = ['banan','owoc','czerwony']

if 'owoc' in lista_example_4:
    print('Element znajduje się na liście')

if 'owoc' == lista_example_4:  # nigdy True: porównuje napis z całą listą, element sprawdzamy przez in
    print('jest')

# zamiast tego:
kolor = "czerwony"
if kolor == "czerwony" or kolor == "zielony" or kolor == "niebieski":
    print("To kolor podstawowy")

# lepiej napisać tak:
if kolor in ["czerwony", "zielony", "niebieski"]:
    print("To kolor podstawowy")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 4.2 - 4.10A <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 4.2 - Poproś użytkownika o liczbę. Sprawdź czy jest dodatnia, ujemna czy równa zero. Wyświetl odpowiedni komunikat.
"""
liczba = float(input("Podaj liczbę: "))
if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba == 0:
    print("Liczba jest równa 0")
else:
    print("Liczba jest ujemna")

number = int(input("Podaj liczbę całkowitą: "))
if number > 0:
    print(f"Liczba {number} jest dodania")
elif number <0:
    print(f"Liczba {number} jest ujemna")
else:
    print(f"Liczba {number} jest równa zero")
"""

# 4.4 - Poproś użytkownika o temperaturę. Jeśli jest powyżej 30 - wyświetl Gorąco, jeśli między 15 a 30 - Przyjemnie, jeśli poniżej 15 - Zimno.
"""
temp = float(input("Podaj temperaturę: "))
if temp > 30:
    print("Gorąco!")
elif temp >= 15:
    print("Przyjemnie")
else:
    print("Zimno!")
"""

# 4.6 - Poproś użytkownika o wiek i czy ma bilet (tak/nie). Jeśli ma 18+ i ma bilet - wyświetl Wejście dozwolone. W przeciwnym razie Brak wejścia. Użyj and.
"""
wiek = int(input("Podaj swój wiek: "))
bilet = input("Masz bilet?  ")
if bilet == 'tak' and wiek >= 18:
    print("Wejście dozwolone")
else:
    print("Brak wejścia!")
"""

# 4.7 - Poproś użytkownika o owoc. Sprawdź czy wpisany owoc znajduje się na liście ["jabłko", "banan", "gruszka", "pomarańcza"]. Jeśli tak - wyświetl
# Mamy ten owoc, jeśli nie - Nie mamy tego owocu. Użyj operatora in.
"""
lista = ["jabłko", "banan", "gruszka", "pomarańcza"]
owoc = input("Podaj owoc: ")
if owoc in lista:
    print("Mamy ten owoc")
else:
    print("Nie mamy tego owocu")
"""

# 4.10A - Rozbuduj swój program do BMI w taki sposób, by poza wyświetleniem obliczonego BMI wyświetlił nam również odpowiedni opis wg skali z Wikipedii.
"""
masa = float(input("Podaj swoją wagę: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
komunikat = "Twoje BMI = masa / (wzrost*wzrost) wynosi: "
BMI = masa/(wzrost*wzrost)
print(f"{komunikat} {BMI:.2f}")

if BMI < 16:
    print("Wygłodzenie")
elif 16 <= BMI < 17:
    print("Wychudzenie")
elif 17 <= BMI < 18.5:
    print("Niedowaga")
elif 18.5 <= BMI < 25:
    print("Pożądana masa")
elif 25 <= BMI < 30:
    print("Nadwaga")
elif 30 <= BMI < 35:
    print("Otyłość 1 stopnia")
elif 35 <= BMI < 40:
    print("Otyłość 2 stopnia")
else:
    print("Otyłość 3 stopnia")

# elif BMI >= 40:
#     print("Otyłość 3 stopnia")
# else:
#     pass

weight = float(input("Podaj swoją wagę w kilogramach: "))
height = float(input("Podaj swój wzrost w metrach: "))
BMI = weight / (height * height)
print(f'Twoje BMI wynosi: {BMI:.1f}')
if BMI < 18.5:
    print("Niedowaga")
elif BMI >= 18.5 and BMI < 25:
    print("Waga prawidłowa")
elif BMI >= 25 and BMI < 30:
    print("Nadwaga")
elif BMI >= 30 and BMI < 35:
    print("Otyłość I stopnia")
elif BMI >= 35 and BMI < 40:
    print("Otyłość II stopnia")
else:
    print("Otyłość III stopnia")
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ==============================================================================
# 5. Pętle
# ==============================================================================

# --- Pętla while --------------------------------------------------------------
# Pętla while potrzebuje warunku oraz jego przerwania
# while True:
#     print('Tutaj mamy dodatkowy kod')

# while nie skończona
# zmienna5_while = True
# while zmienna5_while:
#     i5_while = 0
#     print(f'Pętla cały czas trwa {i5_while}')
#     i5_while = 10
#     if i5_while == 5:
#         zmienna5_while = False

"""
i5_while = 0
zmienna5_while = True
while zmienna5_while:
    print(f'Pętla cały czas trwa {i5_while}')
    # i5_while = i5_while + 1
    i5_while += 1 # inkrementacja
    if i5_while == 5:
        zmienna5_while = False

odpowiedz5 = None
while odpowiedz5 is None:
    while_petla_input = input("Jak chcesz przejść dalej to napisz 'tak'")
    if while_petla_input == 'tak':
        print("Kończymy działanie pętli")
        odpowiedz5 = while_petla_input
"""

# --- Pętla for ----------------------------------------------------------------
string_example5_for = 'Fantastycznie'
lista_example5_for = ["jabłko", "banan", "gruszka", "pomarańcza"]

# 0 1 2 3 4 5 6 7 8 9 10 11 12
# F a n t a s t y c z n  i  e

for i in string_example5_for:
    print(i)

# 0      1     2       3
# jabłko banan gruszka pomarańcza

for owoc in lista_example5_for:
    print(owoc)

# :: range()
# Python ma wbudowane coś takiego jak range()
# range(start,stop,step):
# start - od jakiego numeru zaczynamy (domyślnie 0)
# stop  - do jakiego numeru iterujemy, ale BEZ tej liczby (range(1,11) --> 1..10)
# step  - co jaki krok (domyślnie 1, może być ujemny: range(10,0,-1) --> 10..1)

# for numer in range(0,10):
#     print(numer)

# for i in range(0,n+1)

# for numer in range(1,11):
#     print(numer)

for numer in range(1,11,3):
    print(numer)

# :: enumerate --> pozwala na dodanie kolumny LP
for index,owoc in enumerate(lista_example5_for): # zaczynając od zero numeracja 0,1,2 ....
    print(f"{index} - {owoc}")

for index,owoc in enumerate(lista_example5_for,start=1):
    print(f"{index} - {owoc}")

for numer in range(10,0,-3):
    print(numer)

# --- Zagnieżdżanie pętli ------------------------------------------------------
# czyli pętla w pętli
for cyfra in range(1,11):
    for k in range(1,11):
        print(f'{cyfra} * {k}= {cyfra * k}')

# --- Instrukcja BREAK ---------------------------------------------------------
i5_while = 0
while True:
    print(f'Pętla cały czas trwa {i5_while}')
    # i5_while = i5_while + 1
    i5_while += 1 # inkrementacja
    if i5_while == 5:
        break

for i in range(1,11):
    print(i)
    if i == 5:
        break

# --- Instrukcja CONTINUE ------------------------------------------------------
# continue pomija resztę bieżącego obrotu pętli i przechodzi do następnego
print("***Continue***"*5)
for i in range(1,11):
    if i == 6 or i == 8 or i == 10 or i == 4 or i == 2:
        continue
    print(i)

print("***Continue***"*5)

i5_while = 0
zmienna5_while = True
while zmienna5_while:
    print(f'Pętla cały czas trwa {i5_while}')
    if i5_while == 3:
        i5_while += 1  # bez tego pętla nigdy się nie skończy (continue przeskakuje to, co jest niżej)
        continue
    print('Komunikat dla 0,1,2,4, ale nie dla 3')
    i5_while += 1
    if i5_while == 5:
        zmienna5_while = False

# :: Operacje modulo
print(10 % 2)

for i in range(1,11):
    if i % 2 == 0:
        print(i)

print(10 % 3)   # 1  - bo 10 / 3 = 3 reszta 1
print(10 % 2)   # 0  - bo 10 / 2 = 5 reszta 0 (dzieli się równo)
print(7 % 2)    # 1  - bo 7 / 2 = 3 reszta 1
print(9 % 3)    # 0  - bo 9 / 3 = 3 reszta 0
print(5 % 5)    # 0  - bo 5 / 5 = 1 reszta 0

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIA 5.1 - 5.9A <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 5.1 - Wyświetl liczby od 1 do 10 za pomocą pętli for.
"""
print("*" * 20)
for i in range(1,11):
    print(i)
print("*" * 20)
for liczba in range(1, 11):
    print(liczba)
print("*" * 20)
for numer in range(1,11):
    print(numer)
print("*" * 20)
"""

# 5.2 - Wyświetl liczby od 10 do 1 (odliczanie w dół) za pomocą pętli while.
"""
print("*" * 20)

number = 10
while number <= 10 and number > 0:
    print(number)
    number -= 1

print("*" * 20)
liczba = 10
while liczba >= 1:
    print(liczba)
    liczba -= 1

print("*" * 20)

i = 10
while i >= 1:
    print(i)
    i -= 1
    #i = i - 1
print("*" * 20)  # bez wcięcia --> wykona się raz, po zakończeniu pętli

l5=10
while True:
    print(l5)
    l5 -=1
    if l5==0:
        break
"""

# 5.5 - Poproś użytkownika o hasło. Daj mu maksymalnie 3 próby. Jeśli wpisze poprawne ("admin123") -
# wyświetl Zalogowano i przerwij pętlę (break). Jeśli nie trafi - Brak prób.
# for proba in range(3):
#     haslo = input("Podaj hasło: ")
#     if haslo == "admin123":
#         print("Zalogowano")
#         break
#     if proba == 2:
#         print("Brak prób")

# for i in range(3):
#     paski = input("Podaj hasło: ")
#     if paski == "admin123":
#         print("Zalogowano")
#         break
#     if i == 2:
#         print("Brak pozostałych prób")
#     print("*" * 20)

# for test in range(0,3):
#     haslo = input("Podaj hasło:")
#     if haslo =='admin123':
#         print("Zalogowano")
#         break
#     if test == 2:
#         print("Brak prób")

# 5.9A - Wyświetl 20 kolejnych potęg liczby 2. (**)
print("*" * 20)
for i in range(1,21):
    print(2**i)
print("*" * 20)

for i in range(20):
    print(2 ** i)
print("*" * 20)

liczba = 2
for i in range(20):
    print(f"2 do {i} = {liczba ** i}")
print("*" * 20)

# 5.7 - Wyświetl tabliczkę mnożenia od 1 do 5 (zagnieżdżone pętle). Format: 1 x 1 = 1.
for cyfra in range(1, 6):  # stop = 6, bo range nie bierze ostatniej liczby
    for k in range(1, 6):
        print(f"{cyfra} x {k} = {cyfra * k}")
    print()  # pusta linia po każdej liczbie (wcięcie na poziomie pierwszej pętli)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ==============================================================================
# 6. Łańcuchy znaków
# ==============================================================================

# --- Funkcje wbudowane: upper, lower, title -----------------------------------
# Metody stringów (wywołujemy przez kropkę: tekst.metoda())
str6_example = 'aLa MuSi iśĆ DO DoMu'

# --> metody  .metoda()
# --> funkcje funkcja()

print(str6_example)
print(str6_example.upper())      # ALA MUSI IŚĆ DO DOMU --> wszystkie litery duże
print(str6_example.lower())      # ala musi iść do domu --> wszystkie litery małe
print(str6_example.title())      # Ala Musi Iść Do Domu --> każdy wyraz z dużej
print(str6_example.capitalize()) # Ala musi iść do domu --> pierwsza litera duża, reszta małe (jak w zdaniu)
print(str6_example.swapcase())   # AlA mUsI IŚć do dOmU --> małe na duże i odwrotnie

# pytanie6 = input('Czy chcesz kontynuować zakupy, odpowiedź Tak/Nie')
# if pytanie6.lower() == 'tak':
#     print('Chce dalej korzystać ze sklepu')

# --- Funkcje wbudowane: replace -----------------------------------------------
# tekst6 = "Lubię koty i koty koty lubią mnie"

# print(tekst6.replace('koty','psy'))
# print(tekst6.replace('koty','psy',1))
# print(tekst6.replace('koty','psy',2))

# tekst6_email = "   admin @ gmail . com"

# print(tekst6_email.replace(' ',''))

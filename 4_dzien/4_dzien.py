# ==============================================================================
# 14. Moduły
# ==============================================================================
# wbudowany moduł to ten moduł jest od razu możliwy do importu wraz z instalacją pythona
# Dajemy je zwyczajowo na samym początku pliku

# --- Style importu (import, as, from import) -----------------------------------
# print(keyword.kwlist) Nie zadziała przed importem

import keyword

print(keyword.kwlist)

import keyword as kw

print(kw.kwlist)
print(keyword.kwlist)

kw = 'abra'

import keyword as key

print(key.kwlist)
# print(kw.kwlist) # AttributeError: 'str' object has no attribute 'kwlist'

from keyword import kwlist
print(kwlist)

# print(klist) NameError: name 'klist' is not defined. Did you mean: 'kwlist'?

from keyword import kwlist as klist

print(klist)

# --- Moduł math ------------------------------------------------------------------
import math

#zakr round() :.0f

print(math.ceil(3.2))    # 4 (zaokrąglenie w górę)
print(math.floor(3.8))   # 3 (zaokrąglenie w dół)

# --- help() i dir() - sprawdzanie zawartości modułu -------------------------------
# help(math) # --> ctrl + c na kosnoli stopuje przewijanie help dla modulu
# dir(math) os.system --> wywala błą

# print(dir(math))

# lista dir zwracająca wszystkie zawarte w module math funkcje
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign',
#  'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose',
# 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder',
# 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# help(math.ceil)

# Dokumentacja modułów:
# math: https://docs.python.org/3/library/math.html

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 14.1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 14.1 -- Zaimportuj moduł math. Oblicz i wypisz: pierwiastek z 144,
# wartość liczby pi zaokrągloną do 2 miejsc po przecinku, oraz math.pow(2, 10).
print(math.sqrt(144))
root = math.isqrt(144) # Round a square root number downwards to the nearest integer:
print (root)
pi = math.pi
print (round(pi, 2))
print (math.pow(2, 10))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 14.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 14.2 -- Zaimportuj moduł random.
# Wylosuj 5 liczb z zakresu 1-100 i wypisz je na ekranie (użyj pętli).
# random: https://docs.python.org/3/library/random.html
import random

for i in range(5):
    print(random.randint(1, 100))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 14.3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 14.3 -- Zaimportuj date z modułu datetime. Wypisz dzisiejszą datę oraz dzień tygodnia
# (0 = poniedziałek, 6 = niedziela).
# https://docs.python.org/3/library/datetime.html
from datetime import date
dzis = date.today()
print(dzis)
print(dzis.weekday())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Moduł math - dodatkowe funkcje (from import) ---------------------------------
from math import sqrt, pi, pow, factorial, gcd

print(f'Pierwiastkowanie modułem math: {sqrt(144)}')
print(f'Wypisanie liczby pi z modułu math:{pi}')
print(f'Potęgowanie liczb {pow(2,10)}')
print(f'! silnia {factorial(5)}')
print(f'GCD, czyli największy wspólny dzielnik {gcd(12,18)}')

# --- Moduł random - dodatkowe funkcje ---------------------------------------------
import random

print(f'Losowa liczba 1-10: {random.randint(1,10)}')
print(f'Losowy element z listy: {random.choice(['gruszka','jablko','agrest','wisnia','czeresnia'])}')
print(f'Losowa liczbę od 0.0 - 1.0: {random.random()}')

# Randomowo dawało nam czas oczekiwania --> raz 1 sekunde, raz 4 sekundy

# --- Moduł datetime - dodatkowe funkcje -------------------------------------------
from datetime import datetime, date, timedelta

dzis = date.today()
print(dzis)

teraz = datetime.now()
print(teraz)
print(teraz.strftime("%d.%m.%Y %H:%M"))

print(dzis.weekday())

# :: dodawanie/odejmowanie dni od daty
za_tydzien = dzis + timedelta(days=7)
tydzien_temu = dzis - timedelta(days=7)
print(f'Za tydzień mamy datę: {za_tydzien}')
print(f'Tydzień temu był: {tydzien_temu}')

# :: różnica między dwiema datami
urodziny = date(2026, 12, 25)
ile_dni = urodziny - dzis
print(f"Dni do świąt: {ile_dni.days}")

# :: pobranie samych składowych daty
print(dzis.year,dzis.month,dzis.day)

# --- Moduły zewnętrzne - środowisko wirtualne -------------------------------------
# Globalne środowisko
# Wirtualne środowisko

# Scenariusz:
# Instalujecie pythona 3.14
# Piszecie swój kod 1000 linijek
# Używacie różnych modułów(też zewnętrznych)
# Zostawiacie ten skrypt np na 5 miesięcy
# Reinstall systemu
# Instalujecie pythona 3.16
# Próbujecie odpalić sobie skrypt
# Sypie błędami, których wcześnbiej w ogóle nie było

# zewnetrzynch modułów niektóre zapisy, wywoływania zostają całkowicie zmienione

# python --> print(f'') --> później
# 2.2
# python print("  '    '   ")

# import matplotlib # ModuleNotFoundError: No module named 'matplotlib'

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

# Środowisko wirtualne (venv) - po co to w ogóle jest?
#
# Wracając do scenariusza opisanego wyżej: piszesz skrypt, instalujesz do niego kilka
# zewnętrznych bibliotek w konkretnych wersjach, zostawiasz go na kilka miesięcy, w
# międzyczasie robisz reinstalację systemu / aktualizujesz Pythona / instalujesz coś
# innego, co po cichu zaktualizowało którąś z bibliotek "globalnie". Gdy wracasz do
# starego skryptu, dostajesz błędy, których wcześniej w ogóle nie było, mimo że w kodzie
# nic nie zmieniłeś.
#
# Środowisko wirtualne rozwiązuje ten problem - to osobny, odizolowany "mini-Python"
# stworzony tylko na potrzeby jednego projektu. Biblioteki instalowane wewnątrz takiego
# środowiska nie mają wpływu na inne projekty (i odwrotnie), więc każdy projekt może
# mieć swoje własne, niezależne wersje bibliotek, dokładnie takie, jakich potrzebuje -
# niezależnie od tego, co dzieje się globalnie na komputerze.

# :: Tworzenie i aktywacja środowiska wirtualnego
# python -m venv venv                    # tworzy nowe środowisko wirtualne w folderze "venv"
# .\venv\Scripts\Activate                # aktywuje środowisko (Windows) --> aby wyjść: 'deactivate'
# source venv/bin/activate               # aktywuje środowisko (Linux/Mac)

# :: Instalowanie i zarządzanie pakietami (pip)
# pip install requests                   # instalacja pakietu w najnowszej wersji
# pip install requests==2.67.4           # instalacja konkretnej, wybranej wersji
# pip list                               # lista wszystkich zainstalowanych pakietów w środowisku
# pip show requests                      # szczegóły o pakiecie (wersja, lokalizacja, zależności)
# pip install --upgrade pip              # aktualizacja samego pip do najnowszej wersji

# :: Zapisywanie i odtwarzanie zestawu zależności projektu
# pip freeze > requirements.txt          # zapisuje wszystkie zainstalowane pakiety do pliku
# pip install -r requirements.txt        # instaluje pakiety z takiego pliku (np. na nowym komputerze)

# pandas
# pamdas
# pendas # --> wirus, dziwny skrypt

# --- Import modułu własnego -------------------------------------------------------
import kalkulator

# import kalkulator_urzadzen # ModuleNotFoundError: No module named 'kalkulator_urzadzen'

print(f'Moduł własny dodaj(2,5): {kalkulator.dodaj(2,5)}')

import kalkulator as kalk
print(f'Moduł własny dodaj(2,5): {kalk.dodaj(2,5)}')

from kalkulator import odejmij

print(f'Moduł własny odejmij: {odejmij(2,6)}')

print(kalkulator.__doc__)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE - własny moduł <<<<<<<<<<<<<<<<<<<<<<<<<
# Utwórz swój własny moduł (inny niż kalkulator -- np. coś związanego z Twoimi zainteresowaniami: konwerter jednostek,
# generator haseł, cokolwiek z 3 funkcjami) w osobnym pliku .py, a następnie zaimportuj go i wywołaj jego funkcje w drugim pliku.
#
# Wymagania:
# moduł musi mieć docstring na górze pliku (dokumentację modułu) oraz docstring dla każdej funkcji,
# moduł musi zawierać dokładnie 3 funkcje, o takiej strukturze (niezależnie od tematu modułu):
# funkcja z parametrem domyślnym (np. generuj_haslo(dlugosc=12)),
# funkcja przyjmująca co najmniej 2 parametry i zwracająca wynik obliczony na ich podstawie,
# funkcja, która rzuca wyjątek (raise ValueError(...)), jeśli dostanie niepoprawne dane wejściowe (np. ujemną długość, pusty string),
# moduł musi mieć blok if __name__ == "__main__": z testem wszystkich trzech funkcji,

# prefixem --> PS --> 'bs_modul.py'

import pw_modul
print(pw_modul.__doc__)
print(pw_modul.sprawdz_km(34))

import dz_modul
print(dz_modul.__doc__)
print(dz_modul.iloczyn(2,6))

import ms_os_check
print(ms_os_check.__doc__)
print(ms_os_check.zmien_rozmiar(1024))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Bonus: os, shutil, glob ------------------------------------------------------
"""
Moduł os -- praca z systemem plików:

import os

print(os.getcwd())              # bieżący katalog roboczy
print(os.listdir("."))          # lista plików w katalogu
print(os.path.exists("plik.txt"))  # czy plik istnieje? True/False
os.makedirs("nowy_folder", exist_ok=True)  # tworzy folder

# zmiana katalogu roboczego
os.chdir("nowy_folder")
os.chdir("..")   # powrót o poziom wyżej

# rozróżnianie plików od folderów
print(os.path.isfile("plik.txt"))   # True/False -- czy to plik?
print(os.path.isdir("nowy_folder")) # True/False -- czy to folder?

# łączenie ścieżek w sposób bezpieczny dla każdego systemu (Windows/Linux/Mac)
sciezka = os.path.join("dane", "raporty", "styczen.csv")
print(sciezka)   # dane/raporty/styczen.csv (albo dane\raporty\styczen.csv na Windows)

# rozbijanie ścieżki na części
print(os.path.basename(sciezka))   # styczen.csv -- sama nazwa pliku
print(os.path.dirname(sciezka))    # dane/raporty -- sam folder
print(os.path.splitext(sciezka))   # ('dane/raporty/styczen', '.csv') -- nazwa + rozszerzenie

# rozmiar pliku (w bajtach)
print(os.path.getsize("plik.txt"))

# zmiana nazwy i usuwanie plików
os.rename("stary.txt", "nowy.txt")
os.remove("nowy.txt")            # usuwa plik (bezpowrotnie -- uważaj!)
os.rmdir("pusty_folder")         # usuwa PUSTY folder

# przechodzenie po całym drzewie folderów -- bardzo przydatne do automatyzacji
for folder, podfoldery, pliki in os.walk("."):
    for plik in pliki:
        print(os.path.join(folder, plik))

Moduł shutil -- kopiowanie i przenoszenie plików/folderów (czego os nie robi wprost):

import shutil

shutil.copy("dane.txt", "kopia_dane.txt")        # kopiuje plik
shutil.move("kopia_dane.txt", "archiwum/")       # przenosi plik do folderu
shutil.rmtree("stary_folder")                    # usuwa folder RAZEM z zawartością (uważaj!)

Moduł glob -- wyszukiwanie plików po wzorcu (np. "wszystkie pliki .csv w folderze"):
import glob

pliki_csv = glob.glob("dane/*.csv")          # wszystkie .csv w folderze dane/
wszystkie_csv = glob.glob("dane/**/*.csv", recursive=True)  # też w podfolderach
print(pliki_csv)
"""

# --- Moduł sys ---------------------------------------------------------------------
import sys

print(sys.version)       # wersja Pythona
print(sys.platform)      # system operacyjny ('win32', 'linux', 'darwin')

# --- Moduł time --------------------------------------------------------------------
import time

start = time.time()
time.sleep(1)            # pauza 1 sekunda
koniec = time.time()
print(f"Minęło: {koniec - start:.2f} sekund")

# --- Biblioteki do automatyzacji procesów biznesowych -------------------------------
# Do pracy z dokumentami biurowymi
    # openpyxl -- czytanie/pisanie plików Excel (.xlsx), formatowanie komórek, formuły. Bardzo praktyczne, bo mnóstwo firm żyje na Excelu.
    # python-docx -- generowanie/edycja dokumentów Word.
    # python-pptx -- generowanie prezentacji PowerPoint.

# Do PDF-ów
    # PyPDF2 / pypdf -- łączenie, dzielenie, wyciąganie tekstu z PDF-ów.
    # reportlab lub fpdf2 -- generowanie PDF-ów od zera (np. automatyczne faktury).

# Do e-maili
    # smtplib (wbudowana) -- wysyłanie maili.

# --- Popularne zewnętrzne biblioteki ------------------------------------------------
# numpy -- Obliczenia numeryczne, tablice. Instalacja: pip install numpy. Przykład: np.array([1, 2, 3])
# pandas -- Analiza danych, tabele (DataFrame). Instalacja: pip install pandas. Przykład: pd.read_csv("dane.csv")
# matplotlib -- Wykresy i wizualizacje. Instalacja: pip install matplotlib. Przykład: plt.plot([1,2,3])
# requests -- Zapytania HTTP / API. Instalacja: pip install requests. Przykład: requests.get(url)
# flask -- Aplikacje webowe. Instalacja: pip install flask. Przykład: app = Flask(__name__)
# psycopg2 -- Łączenie z PostgreSQL. Instalacja: pip install psycopg2-binary. Przykład: psycopg2.connect(...)

# ==============================================================================
# 15. Korzystanie z plików tekstowych
# ==============================================================================

# --- Ścieżka względna i bezwzględna -----------------------------------------------
# Ścieżka bezwględna --> 'C:\Users\labuser\Desktop\szkolenie_python_podstawy_10.03.2026\4_dzien\dane.txt'

# :: Ścieżka względna
import os

print(os.getcwd())
print('*'*20)
katalog_skryptu = os.path.dirname(os.path.abspath(__file__))
print(katalog_skryptu)
sciezka_danetxt = os.path.join(katalog_skryptu, "dane.txt")
print(sciezka_danetxt)
print('*'*20)

# --- Odczytywanie plików tekstowych - read() --------------------------------------
# with open("dane.txt", "r", encoding="utf-8") as plik: # wywala błą, bo w głownym folderze nie ma dane.txt
#     zawartosc = plik.read()
#     print(zawartosc)

# with open(plik_tekstowy, tryb_odpalania, encoding)
# encoding -> pl litery

# metoda with open otwiera plik, robi na nim konkretne działania, a następnie automatycznie go zamyka
with open(sciezka_danetxt, "r", encoding="utf-8") as plik:
    zawartosc = plik.read() #  read() wyświetla całość str w środku pliku tekstowego
    print(zawartosc)
    koniec = plik.read()
    print(f'tutaj mamy koniec -> {koniec}') # nie ma dalszego tekstu, więc kończy czytanie

# plik.read()# ValueError: I/O operation on closed file.

# --- readlines() ---------------------------------------------------------------------
# zwraca nam listę zdań znajdujących się w pliku
with open(sciezka_danetxt, "r", encoding="utf-8") as plik:
    zawartosc = plik.readlines()
    print(zawartosc)
    print(zawartosc) # odniesienie do tego samego readlines
    koniec = plik.readlines() # jesteśmy już po przeczytaniu pliku i zwraca nam pustą listę
    print(koniec)

# --- readline() ------------------------------------------------------------------------
# zwraca od początku zaczynając linijkę jedną max
with open(sciezka_danetxt, "r", encoding="utf-8") as plik:
    zawartosc = plik.readline()
    print(zawartosc) # Ala ma kota
    print(zawartosc) # Ala ma kota odniesienie do tego samego readline
    koniec = plik.readline() # Ola ma psa zwraca nam kolejną linijkę w tekśćie
    print(koniec)
    print(plik.readline()) # Kasia lubi programować w Pythonie
    print(plik.readline()) # Bartek je śniadanie o ósmej
    print(plik.readline()) # Zofia czyta książkę wieczorem
    print(plik.readline()) # puste, bo koniec pliku
    print(plik.readline()) # puste bo koniec pliku

# --- Iterowanie po liniach pliku (for) --------------------------------------------------
print('*'*30)
with open(sciezka_danetxt, "r", encoding="utf-8") as plik:
    for linia in plik:
        print(linia.strip())

# --- Funkcja seek() ---------------------------------------------------------------------
# Funkcja seek ustawia nam kursos czytania plików tekstowych na konkretne miejsce
with open(sciezka_danetxt, "r", encoding="utf-8") as plik:
    plik.read()
    print('pustemiejsce-'*7)
    print(plik.read())
    print('pustemiejsce-'*7)
    plik.seek(0)
    print(plik.read())

# --- Sprawdzanie ilości linii w pliku ----------------------------------------------------
with open(sciezka_danetxt, "r", encoding="utf-8") as plik:
    ile_linii = len(plik.readlines())
    print(f'Plik podany ma {ile_linii} linii')

with open(sciezka_danetxt, "r", encoding="utf-8") as plik:
    zawartosc = plik.readline()
    print(zawartosc) # Ala ma kota
    print(f'{len(zawartosc)}')
    koniec = plik.readline() # Ola ma psa zwraca nam kolejną linijkę w tekśćie
    print(koniec)
    print(f'{len(koniec)} długość zdanie drugiego')
    plik.seek(12)
    print(plik.readline())

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE - poćwicz czytanie pliku <<<<<<<<<<<<<<<
# osoby.txt
# Mając ten plik, napisz program, który po kolei (jedno pod drugim, żeby zobaczyć różnicę między metodami):
print('='*50)
sciezka_osoby = os.path.join(katalog_skryptu,'osoby.txt')

# :: wczyta cały plik jako jeden string (read()) i go wypisze
with open(sciezka_osoby, "r", encoding="utf-8") as plik:
    caly_plik = plik.read()
    print(caly_plik)
print('='*50)

# :: wczyta plik jako listę linii (readlines()) i wypisze tę listę (zwróć uwagę na \n na końcu każdej linii)
with open (sciezka_osoby, "r", encoding="utf-8") as plik:
    osoby_read = plik.readlines()
    print (osoby_read)
print('='*50)

# :: przeiteruje po pliku pętlą for i wypisze każdą osobę bez \n (użyj .strip())
with open(sciezka_osoby, 'r', encoding='utf-8') as plik:
    for linia in plik:
        print(linia.strip())

# :: wczyta tylko pierwsze dwie linie przez dwukrotne wywołanie readline(),
# użyje seek(0), żeby wrócić na początek pliku, a następnie policzy i wypisze, ile linii ma plik (przez len(readlines())).
with open(sciezka_osoby, 'r', encoding='utf-8') as plik:
        print(plik.readline())
        print(plik.readline())
        plik.seek(0)
        print(f'Liczba linii: {len(plik.readlines())}')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Obsługa błędu - plik nie istnieje ---------------------------------------------------
try:
    sciezka_grecka = os.path.join(katalog_skryptu,'tragedia_grecka.txt') # FileNotFoundError
    with open(sciezka_grecka, 'r', encoding='utf-8') as plik:
        plik.read()
except FileNotFoundError:
    print('Pod ścieżką nie ma danego pliku')

# --- Otwieranie pliku bez with (druga metoda) --------------------------------------------
# UWAGA: poniższe "Linijka kodu z błędem" to tylko ILUSTRACJA - w tym konkretnym demo nic
# takiego się nie dzieje (te linijki są zakomentowane), a plik.close() faktycznie się wykona.
# Chodzi o to, że gdyby MIĘDZY open() a close() faktycznie wystąpił błąd (wyjątek), program
# wywaliłby się w tym miejscu i nigdy by nie dotarł do linijki z close() - plik zostałby
# otwarty "na zawsze". Właśnie dlatego wolimy with open(...) - on zamknie plik nawet wtedy,
# gdy coś pójdzie nie tak w środku.
plik = open(sciezka_osoby, 'r', encoding='utf-8')
zawartosc = plik.read()
# Linijka kodu
# Linijka kodu
# Linijka kodu
# Linijka kodu z błędem # plik nigdy się nie zamknie, bo nie dojdzie do linijki z polecenime close()
# Linijka kodu
# Linijka kodu
## Po działaniu z plikiem on sam się automatycznie w tej metodzie nie zamyka
plik.close() # zamykamy zawsze plik po działaniach

# --- Zapis w plikach tekstowych - tryb "w" (write) ----------------------------------------
sciezka_wynik = os.path.join(katalog_skryptu,'wyniki.txt')
# Write nadpisuje całkowicie plik tekstowy, oraz usuwa zawartość oryginału
with open(sciezka_wynik, 'w', encoding='utf-8') as plik:
    plik.write("Pierwsza linijka\n")
    plik.write("Druga linijka linijka\n")

# Jeśli pod daną ścieżką nie ma danego pliku tekstowego to tworzy go na nowo
sciezka_nieis = os.path.join(katalog_skryptu,'tragedia_rzymska.txt')
with open(sciezka_nieis, 'w', encoding='utf-8') as plik:
    plik.write("Pierwsza linijka\n")
    plik.write("Druga linijka linijka\n")

# --- Zapis w plikach tekstowych - tryb "a" (append) ---------------------------------------
# append dodaje na samym końcu pliku nie kasując oryginału
with open(sciezka_wynik, 'a', encoding='utf-8') as plik:
    plik.write("Trzecia linijka\n")
    plik.write("Czwarta linijka\n")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 15.1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print('='*60)
sciezka_notatka = os.path.join(katalog_skryptu,'notatka.txt')
# 15.1 -- Utwórz plik notatka.txt i zapisz do niego 3 dowolne zdania (każde w osobnej linii).
with open(sciezka_notatka, "w", encoding="utf-8") as plik:
    plik.write("Python jest super\n")
    plik.write("Lubię automatyzację\n")
    plik.write("Uczę się Pythona\n")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 15.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 15.2 -- Odczytaj plik notatka.txt i wypisz każdą linię z numerem (np. 1: Python jest super.).
with open(sciezka_notatka, "r", encoding="utf-8") as plik:
    for nr, linia in enumerate(plik, start=1):
        print(f"{nr}: {linia.strip()}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 15.3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 15.3 -- Dopisz do pliku notatka.txt jeszcze jedno zdanie (tryb "a"). Następnie odczytaj cały plik i wypisz go.
with open(sciezka_notatka, "a", encoding="utf-8") as plik:
    plik.write("Python przydaje się w pracy\n")
with open(sciezka_notatka, "r", encoding="utf-8") as plik:
    print(plik.read())
print('='*60)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Bonus: praca z plikami CSV -----------------------------------------------------------
# Adam,28,kraków
import csv

sciezka_danecsv = os.path.join(katalog_skryptu,'dane.csv')
with open(sciezka_danecsv , "r", encoding="utf-8") as plik:
    czytnik = csv.reader(plik,delimiter=";")
    # print(czytnik) # brzydki obiekt
    for wiersz in czytnik:
        print(wiersz)

# :: Zapis CSV
sciezka_writecsv = os.path.join(katalog_skryptu,'wyniki.csv')

with open(sciezka_writecsv , "w", encoding="utf-8") as plik: # io.UnsupportedOperation: not writable przer 'r'
    pisarz = csv.writer(plik, delimiter=';')
    pisarz.writerow(['Imie','Wiek','Miasto'])
    pisarz.writerow(['Damian',25,'Poznań'])
    pisarz.writerow(['Ala',20,'Kraków'])

# --- Bonus: praca z JSON ------------------------------------------------------------------
import json
dane = {"imie": "Adam", "wiek": 25, "hobby": ["Python", "gry"]}

sciezka_json = os.path.join(katalog_skryptu,'dane.json')

with open(sciezka_json , "w", encoding="utf-8") as plik:
    json.dump(dane, plik, ensure_ascii=False, indent=4)

with open(sciezka_json , "r", encoding="utf-8") as plik:
    wczytane = json.load(plik)
    print(wczytane)
    print(wczytane['imie'])

# ==============================================================================
# 16. Dane zdalne - wykorzystanie usług sieciowych
# ==============================================================================

# --- Czym są API i kody statusu -----------------------------------------------------------
# API (Application Programming Interface) - sposób komunikacji miedzy programami. Najczęściej za pomocą pobierania danych w formacie json

produkty = [
    {"nazwa": "Laptop", "cena": 3500},
    {"nazwa": "Mysz", "cena": 50},
    {"nazwa": "Monitor", "cena": 1200},
    {"nazwa": "Kabel", "cena": 15}
]

# Get metoda -> pobieranie danych bez żadnych filtracji jak i z jakąś konkertną filtracją
# Ponad 3000 -> pobieramy dane, ale dodatkow dajemy parametr do filtracji

# POST --> wysyłamy jakieś dane

# Status code
# 2xx --> daje nam informacje, że wszystko przebiegło pomyślnie
# 4xx --> że to my najpewniej wpisaliśmy coś źle, taki url nie istnieje
# 5xx --> że aplikacja padła, nie działa

# --- GET request + JSON -------------------------------------------------------------------
print('='*70)
print('=requests='*8)
import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

odpowiedz = requests.get(url)

#sprawdzenie poprawności połączenia
print(odpowiedz.status_code) # 200 --> wszystko poszło po naszej myśli

dane = odpowiedz.json()
print(dane)
print(dane['title'])
print('='*70)

# --- Pobieranie listy danych ---------------------------------------------------------------
odpowiedz = requests.get('https://jsonplaceholder.typicode.com/users/')
print(odpowiedz.status_code)
uzytkownicy = odpowiedz.json()

for u in uzytkownicy[:3]: # pierwsze trzy
    print(f'{u['username']} -- {u['email']}')

# --- Parametry w GET -------------------------------------------------------------------------
"""  100 postów
odpowiedz = requests.get('https://jsonplaceholder.typicode.com/posts/')
print(odpowiedz.status_code)
posts = odpowiedz.json()
print(len(posts))
"""
params = {'userId':1}
odpowiedz = requests.get('https://jsonplaceholder.typicode.com/posts',params=params)
print(odpowiedz.status_code)
posts = odpowiedz.json()
print(len(posts))

# --- Obsługa błędów --------------------------------------------------------------------------
"""
import requests

url = "https://jsonplaceholder.typicode.com/posts/999"

try:
    odpowiedz = requests.get(url, timeout=5)
    if odpowiedz.status_code == 200:
        dane = odpowiedz.json()
        print(dane)
    elif odpowiedz.status_code == 404:
        print("Nie znaleziono zasobu!")
    else:
        print(f"Błąd: {odpowiedz.status_code}")
except requests.exceptions.ConnectionError:
    print("Brak połączenia z internetem!")
except requests.exceptions.Timeout:
    print("Przekroczono czas oczekiwania!")
"""

# --- POST -- wysyłanie danych ------------------------------------------------------------------
nowy_post = {
    "title": "Mój post",
    "body": "Treść posta",
    "userId": 1
}

odpowiedz = requests.post("https://jsonplaceholder.typicode.com/posts",json=nowy_post)
print(odpowiedz.status_code) # operacja zakończona sukcesem 201
print(odpowiedz.json())

# --- Bonus: nagłówki / autoryzacja --------------------------------------------------------------
"""
# headers = {
#     "Authorization": "Bearer TWOJ_TOKEN",
#     "Content-Type": "application/json"
# }

# odpowiedz = requests.get("https://api.example.com/dane", headers=headers)
"""

# --- Bonus: zapis danych z API do pliku ----------------------------------------------------------
"""
import requests
import json

odpowiedz = requests.get("https://jsonplaceholder.typicode.com/users")
uzytkownicy = odpowiedz.json()

with open("uzytkownicy.json", "w", encoding="utf-8") as plik:
    json.dump(uzytkownicy, plik, ensure_ascii=False, indent=4)
print("Zapisano do pliku!")
"""

# ==============================================================================
# 18. Wstęp do obiektowości
# ==============================================================================

# --- Klasa + __init__ + self --------------------------------------------------------------------
# Klasa to szablon (przepis) opisuje dane i zachowania obiektu.

#Deklaruje obiekt
class Osoba:
    pass

class Osoba:
    # konkstruktor co automatycznie uruchamia się przy tworzeniu obiektu
    def __init__(self,imie,wiek):
        self.imie = imie # atrybuty obiektu
        self.wiek = wiek # atrybuty obiektu

# Tworzenie obiektu (instancji)
anna = Osoba('Anna',30)
# anna = Osoba('Anna') #TypeError: Osoba.__init__() missing 1 required positional argument: 'wiek'
# anna = Osoba('Anna',30,34,25,56) #TypeError: Osoba.__init__() takes 3 positional arguments but 6 were given
jan = Osoba('Jan',19)

# Brakuje czegoś w klasie, więc brzydko nazywa print
print(anna) #<__main__.Osoba object at 0x0000018395E7F770>
print(jan)  #<__main__.Osoba object at 0x0000018395FB9BD0>

print(anna.imie,anna.wiek)
print(jan.imie,jan.wiek)

class Pies:
    def __init__(self,imie,rasa):
        self.imie = imie
        self.rasa = rasa

burek = Pies('Burek','owczarek')
luna = Pies('Luna','labrador')

print(burek.imie,burek.rasa)
print(luna.imie,burek.imie)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 18.1b <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print("="*30)
# 18.1b -- Stwórz klasę Ksiazka z atrybutami tytul, autor i rok_wydania. Utwórz 3 obiekty (dowolne książki)
# i wyświetl dla każdej zdanie w stylu "Zbrodnia i kara" (Dostojewski, 1866).
class Ksiazka:
    def __init__(self,tytul,autor,rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

ksiazka_1 = Ksiazka('Harry Potter','Rowling',2001)
ksiazka_2 = Ksiazka('Zbrodnia i kara', 'Dostojewski', 1866)
ksiazka_3 = Ksiazka('Hobbit', 'Tolkien', 1937)

print(
f'"{ksiazka_1.tytul}" ({ksiazka_1.autor}, {ksiazka_1.rok})\n'
f'"{ksiazka_2.tytul}" ({ksiazka_2.autor}, {ksiazka_2.rok})\n'
f'"{ksiazka_3.tytul}" ({ksiazka_3.autor}, {ksiazka_3.rok})'
)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 18.b <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print("="*30)
# 18.b -- Stwórz klasę szczyty z atrybutami wysokosc, nazwa, kategoria. Utwórz 3 obiekty oraz je wyświetlili
class Szczyt:
    def __init__(self, wysokosc, nazwa, kategoria):
        self.wysokosc = wysokosc
        self.nazwa = nazwa
        self.kategoria = kategoria
szczyt1 = Szczyt(2499, "Rysy", "Tatry")
szczyt2 = Szczyt(1603, "Śnieżka", "Karkonosze")
szczyt3 = Szczyt(1725, "Babia Góra", "Beskidy")
print(szczyt1.nazwa, szczyt1.wysokosc, szczyt1.kategoria)
print(szczyt2.nazwa, szczyt2.wysokosc, szczyt2.kategoria)
print(szczyt3.nazwa, szczyt3.wysokosc, szczyt3.kategoria)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

print("="*30)

# --- Metody - funkcja wewnątrz klasy (zawsze self jako pierwszy parametr) -------------------
class KontoBankowe:
    def __init__(self,wlasciciel,saldo=0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplata(self,kwota):
        self.saldo += kwota
        print(f'Wpłacono {kwota} zł. Saldo: {self.saldo} zł')

    def wyplata(self,kwota):
        if kwota > self.saldo:
            print('Brak wystarczających środków')
        else:
            self.saldo -= kwota
            print(f'Wypłacono {kwota} zł. Saldo: {self.saldo} zł')

    def stan(self):
        print(f'Konto {self.wlasciciel}:{self.saldo} zł')

# obiekt
konto = KontoBankowe('Romek')
konto.wplata(500)
konto.stan()
konto.wplata(800)
konto.stan()
konto.wyplata(2000)
konto.stan()
konto.wyplata(200)

# :: Klasa Samochodu
class Auto:
    def __init__(self,marka,predkosc=0):
        self.marka = marka
        self.predkosc = predkosc

    def przyspiesz(self,ile):
        self.predkosc += ile
        print(f'Prędkość {self.marka}: {self.predkosc} km/h ')

    def hamuj(self,ile):
        self.predkosc -= ile
        print(f'Prędkość {self.marka}: {self.predkosc} km/h ')

auto = Auto('Toyota')
auto.przyspiesz(30)
auto.przyspiesz(30)
auto.hamuj(60)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 18.2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 18.2 -- Dodaj do klasy Osoba metodę przedstaw_sie(), która wypisuje np. Cześć, jestem Anna i mam 30 lat.
class Osoba:
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Cześć, jestem {self.imie} i mam {self.wiek} lat.')

milosz = Osoba('Miłosz',33)
milosz.przedstaw_sie()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE 18.2d <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 18.2d -- Rozszerz klasę Samochod o atrybut paliwo (domyślnie 0) oraz metody tankuj(litry)
# (dolewa paliwo do zbiornika) i stan_paliwa() (wypisuje aktualny poziom paliwa).

# ???
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADAŃ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Metody magiczne: __str__ ---------------------------------------------------------------
class Osoba:
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek
    def __str__(self):
        return f'Osoba: {self.imie} - {self.wiek}'

anna = Osoba('Anna',30)
jan = Osoba('Jan',19)

# Brakuje czegoś w klasie, więc brzydko nazywa print
print(anna) # Osoba: Anna - 30
print(jan)  # Osoba: Jan - 19

# --- Metody magiczne: pełny przykład (Druzyna) --------------------------------------------------
class Druzyna:
    def __init__(self, nazwa, zawodnicy):
        self.nazwa = nazwa
        self.zawodnicy = zawodnicy

    def __str__(self):
        return f"Drużyna {self.nazwa} ({len(self.zawodnicy)} os.)"

    def __len__(self):
        return len(self.zawodnicy)

    def __contains__(self, osoba):
        return osoba in self.zawodnicy

    def __eq__(self, other):
        return self.nazwa == other.nazwa

    def __lt__(self, other):
        return len(self.zawodnicy) < len(other.zawodnicy)

    def __gt__(self, other):
        return len(self.zawodnicy) > len(other.zawodnicy)

    def __add__(self, other):
        return Druzyna(f"{self.nazwa} + {other.nazwa}", self.zawodnicy + other.zawodnicy)

d = Druzyna("Orły", ["Adam", "Ola", "Kasia"])
lwy = Druzyna("Lwy", ["Jan", "Ewa"])

print(d)                          # Drużyna Orły (3 os.)
print(len(d))                     # 3
print("Ola" in d)                 # True

# :: __eq__ w akcji -- porównuje tylko nazwę drużyny
print(d == Druzyna("Orły", []))   # True  -- ta sama nazwa, inni zawodnicy
print(d == lwy)                   # False -- inna nazwa

# :: __lt__ / __gt__ w akcji -- porównuje liczbę zawodników
print(d > lwy)                    # True  -- Orły (3) mają więcej niż Lwy (2)
print(d < lwy)                    # False

# :: __add__ w akcji -- "łączy" dwie drużyny w nową
polaczona = d + lwy
print(polaczona)                  # Drużyna Orły + Lwy (5 os.)

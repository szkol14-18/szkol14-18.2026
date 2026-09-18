""" Moduł własny, posiada funkcje do generowania liczb losowych, iloczyn podanych liczb, iloraz podanych liczb"""
import random

def losowanie(a,b):
     return random.randint(a,b)

def iloczyn(a,b=2):
     return a* b

def iloraz(a,b):
    if b == 0:
         raise ZeroDivisionError('Liczba = 0, nie można dzielić przez 0')
    return a/b

if __name__ == "__main__":
    print(losowanie(2,10))
    print(iloczyn(2))
    print(iloraz(10,2))
    print(iloraz(9,0))

# Utwórz swój własny moduł (inny niż kalkulator -- np. coś związanego z Twoimi zainteresowaniami: konwerter jednostek, 
# generator haseł, cokolwiek z 3 funkcjami) w osobnym pliku .py, a następnie zaimportuj go i wywołaj jego funkcje w drugim pliku.
# Wymagania:
# moduł musi mieć docstring na górze pliku (dokumentację modułu) oraz docstring dla każdej funkcji,
# moduł musi zawierać dokładnie 3 funkcje, o takiej strukturze (niezależnie od tematu modułu):
# funkcja z parametrem domyślnym (np. generuj_haslo(dlugosc=12)),
# funkcja przyjmująca co najmniej 2 parametry i zwracająca wynik obliczony na ich podstawie,
# funkcja, która rzuca wyjątek (raise ValueError(...)), jeśli dostanie niepoprawne dane wejściowe (np. ujemną długość, pusty string),
# moduł musi mieć blok if __name__ == "__main__": z testem wszystkich trzech funkcji,
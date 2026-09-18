"""Moduł do przeliczania kilometrów i sprawdzania danych."""

def powitanie(imie="Przemysław"):
    """Funkcja z parametrem domyślnym."""
    return f"Cześć {imie}"

def km_na_mile(km, przelicznik):
    """Funkcja przyjmująca 2 parametry i zwracająca wynik."""
    return km * przelicznik

def sprawdz_km(km):
    """Funkcja rzucająca wyjątek dla błędnych danych."""
    if km < 0:
        raise ValueError("Liczba kilometrów nie może być ujemna")
    return km

if __name__ == "__main__":
    print(powitanie())
    print(km_na_mile(10, 0.621371))
    print(sprawdz_km(5))
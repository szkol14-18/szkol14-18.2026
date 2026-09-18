""" Moduł kalkulator, zawiera funkcje dodaj oraz odejmij dla dwóch argumentów"""


def dodaj(a,b):
    return a+b

def odejmij(a,b):
    return a - b


# za pomocą tej instrukcji if robimy kod tylko jeśli zostanie on w tym mijescu odpalony 
if __name__ == "__main__":
    print(f'SPrawdzanie, czy działaja funkcje dodaj, odejmij')
    print(dodaj(2,7))
    print(odejmij(10,5))
    print(f'SPrawdzanie, czy działaja funkcje dodaj, odejmij')

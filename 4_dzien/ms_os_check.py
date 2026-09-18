"""
Moduł zawierający 3 narzędzia związane z systemem operacyjnym
- zmien_rozmiar    : Przelicza rozmiar podany w bajtach na wybraną jednostkę
- uzycie_dysku     : Oblicza procent zajętego miejsca na dysku
- spr_usera       : Sprawdza nazwę użytkownika. Jeżli nazwa jest pusta ValueError
"""


# import ms_os_check
# print(ms_os_check.zmien_rozmiar(1073741824,'GB'))
# print(ms_os_check.zmien_rozmiar(1073741824,'MB'))
# print(ms_os_check.uzycie_dysku(75, 100))
# print(ms_os_check.spr_usera("Adam"))


def zmien_rozmiar(rozmiar, jednostka='MB'):
# :.2f - 2 miejsca po kropce
    if jednostka == 'KB':
        return f'{rozmiar / 1024:.2f} KB'
    elif jednostka == 'MB':
        return f'{rozmiar / (1024 ** 2):.2f} MB'
    elif jednostka == 'GB':
        return f'{rozmiar / (1024 ** 3):.2f} GB'

def uzycie_dysku(uzycie, calosc):
    return f'{(uzycie / calosc) * 100}%'

def spr_usera(nazwa):
    if not nazwa:
        raise ValueError('Nazwa użytkownika pusta')

    return f'Użytkownik: {nazwa}'


if __name__ == '__main__':
    print(zmien_rozmiar(1024))
    print(uzycie_dysku(50, 100))
    print(spr_usera('Miłosz'))
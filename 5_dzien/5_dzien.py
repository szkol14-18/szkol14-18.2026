# ==============================================================================
# 17. Wykorzystanie baz danych
# ==============================================================================
# - Tworzenie tabel
# - Dodawanie wartości do tabeli
# - Edytowanie
# - Usuwanie
# - Operacje DDL

import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres",
                         user="postgres", password="Password!")

# --- Tworzenie tabeli ------------------------------------------------------------

# odkomentować hasztagi i wyciągnąć z polecenia
"""
# Średnik wywala błąd 
cur = conn.cursor()
cur.execute("""
# CREATE TABLE IF NOT EXISTS klienciii (
#          id SERIAL PRIMARY KEY,
#          imie VARCHAR(50) NOT NULL,
#          miasto VARCHAR(50),
#          saldo DECIMAL(10, 2) DEFAULT 0,
#          aktywny BOOLEAN DEFAULT TRUE
#      )
"""
)
conn.commit()
cur.close()
conn.close()
"""

# -- id --> jest automatycznie nadawany id, klucz główny 
# -- miast, imie --> varchar(str) do 50 znaków,powyżej wywala błąd 
# -- saldo --> zmiennoprzecinkowa 10 znaków max do 2 po przecinku zaokrą
# -- aktywny bool --> True, albo False 

# -- default to domyślna wartość zapisywana jak się nie poda jej przy dodawaniu wiersza
# -- NOT NULL nie można dodać wiersza bez wpisania cokolwiek do tjk kolumny 
# -- Primary key to jest klucz głowny, czyli głowne id tabeli 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Utworzyli tabelę taką podobną jak klienci.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADANIA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Dodawanie do tabeli za pomocą INSERT -----------------------------------------

# :: Dodawanie pojedynczej osoby
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
            f"INSERT INTO klienci (imie,miasto,saldo) VALUES (%s,%s,%s)",
        ("Angelina",'Rzeszów',80)
        )
"""

# :: SQL INJECTION -- Tak nie robimy!!!!!
"""
zmienna = 'abradabra'
with conn:
    with conn.cursor() as cur:
        cur.execute(
            f"INSERT INTO klienci (imie,miasto,saldo) VALUES ({zmienna},{zmienna},24)"
        )
"""

# :: Dodawanie pojedynczej osoby (ten sam wzorzec raz jeszcze, bez f-stringa)
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO klienci (imie,miasto,saldo) VALUES (%s,%s,%s)",
        ("Angelina",'Rzeszów',80)
        )
"""

# :: Dodawanie wielu insertów naraz -- executemany()
"""
klienci = [
    ('Jan','Wałbrzych',840),
    ('Ola','Zakopane',240),
    ('Marek','Warszawa',1000),
]

# dla wielu wyników executemany() w pythonie 
with conn:
    with conn.cursor() as cur:
        cur.executemany(
            f"INSERT INTO klienci (imie,miasto,saldo) VALUES (%s, %s, %s)",
            klienci
        )
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Zrobić inserty do tabeli -- swojej własnej za pomocą pgadmin lub skryptem
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADANIA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Wyciąganie danych za pomocą SELECT --------------------------------------------

# Dwie metody wyciągania:
# 1. fetchone() ->> wyciągnięcie tylko jednej wartości
# 2. fetchall() ->> wyciągnięcie wszystkiego

"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT miasto,imie FROM klienci"
        )
        pierwszy = cur.fetchone()
        print(pierwszy)
        drugi = cur.fetchall()
        print(drugi)
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Sprawdzili metody select na swojej własnej tabeli i wprowadzonych tam wierszach
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADANIA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Edytowanie za pomocą UPDATE ----------------------------------------------------
"""
id = 11
saldo = 1000

with conn:
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE klienci SET saldo = %s WHERE id = %s",
            (saldo,id)
        )
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Edytowali jakąś część swojej tabeli na wartości jakie chcecie
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADANIA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- Usuwanie za pomocą DELETE -------------------------------------------------------
"""
# id = 11 # TypeError: 'int' object does not support indexing
id = 10

with conn:
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM klienci WHERE id = %s",
            (id,)
        )
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ZADANIE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Spróbujcie usunąć coś ze swojej tabeli po wybranych przez siebie warunkach.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> KONIEC ZADANIA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# --- DDL -- zmiana struktury tabeli / kasowanie ---------------------------------------

# :: Tworzenie tabeli (przypomnienie)
"""
# Średnik wywala błąd 
cur = conn.cursor()
cur.execute("""
# CREATE TABLE IF NOT EXISTS klienciii (
#          id SERIAL PRIMARY KEY,
#          imie VARCHAR(50) NOT NULL,
#          miasto VARCHAR(50),
#          saldo DECIMAL(10, 2) DEFAULT 0,
#          aktywny BOOLEAN DEFAULT TRUE
#      )
"""
)
conn.commit()
cur.close()
conn.close()
"""

# :: Dodawanie kolumny -- na sztywno
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
            "ALTER TABLE klienci ADD COLUMN aba VARCHAR(100)"
        )
"""

# :: Dodawanie kolumny -- próba ze zmienną przez %s (BŁĄD!)
"""
# BŁĄD nazwa_kol ma '' przez co łamię budowę zapytania
nazwa_kol = 'abrakadabra'
with conn:
    with conn.cursor() as cur:
        cur.execute(
            "ALTER TABLE klienci ADD COLUMN %s VARCHAR(100)",
            (nazwa_kol,)
        )
"""

# :: Dodawanie kolumny -- poprawnie, przez psycopg2.sql.Identifier()
"""
def funkcja():
    import psycopg2.sql
    nazwa_kolumny = 'abrakadabra'
    with conn:
        with conn.cursor() as cur:
            cur.execute(psycopg2.sql.SQL("ALTER TABLE klienci ADD COLUMN {} VARCHAR(100)").format(psycopg2.sql.Identifier(nazwa_kolumny))
            )
funkcja()
"""

# :: Usuwanie kolumny z tabeli -- na sztywno
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
            "ALTER TABLE klienci DROP COLUMN rasa"
        )
"""

# :: Usuwanie kolumny z tabeli -- ze zmienną
"""
def funkcja():
    import psycopg2.sql
    nazwa_kolumny = 'opis'
    with conn:                       
        with conn.cursor() as cur:  
            cur.execute(
psycopg2.sql.SQL("ALTER TABLE klienci DROP COLUMN {}").format(psycopg2.sql.Identifier(nazwa_kolumny))
            )
funkcja()
"""

# :: Zmiana nazwy kolumny -- na sztywno
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
            "ALTER TABLE klienci RENAME COLUMN aba To email"
        )
"""

# :: Zmiana nazwy kolumny -- ze zmienną
"""
def funkcja():
    import psycopg2.sql
    nks = 'email'
    nkn = 'plec'

    with conn:                       
        with conn.cursor() as cur:  
            cur.execute(
psycopg2.sql.SQL("ALTER TABLE klienci RENAME COLUMN {} TO {}").format(psycopg2.sql.Identifier(nks),psycopg2.sql.Identifier(nkn))
            )
funkcja()
"""

# :: TRUNCATE -- na sztywno
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
            "TRUNCATE TABLE klienci"
        )
"""

# :: TRUNCATE -- ze zmienną
"""
def funkcja():
    import psycopg2.sql
    tabela = 'klienci'

    with conn:                       
        with conn.cursor() as cur:  
            cur.execute(
psycopg2.sql.SQL("TRUNCATE TABLE {}").format(psycopg2.sql.Identifier(tabela))
            )
funkcja()
"""

# :: Kasowanie całej tabeli (DROP TABLE) -- na sztywno
"""
with conn:
    with conn.cursor() as cur:
        cur.execute(
           "DROP TABLE IF EXISTS klienci"
        )
"""

# :: Kasowanie całej tabeli (DROP TABLE) -- ze zmienną
"""
def funkcja():
    import psycopg2.sql
    tabela = 'klienci'

    with conn:                       
        with conn.cursor() as cur:  
            cur.execute( 
psycopg2.sql.SQL("DROP TABLE IF EXISTS {}").format(psycopg2.sql.Identifier(tabela))
            )
funkcja()
"""


-- Tworzenie tabeli za pomocą zapytania sql

-- ctrl + /
-- CREATE TABLE --> tworzenie tabeli
-- IF NOT EXISTS --> jeśli taka nazwa nie istnieje to przypisuje do niej
-- klienci --> nazwa tabeli (z małych liter)

-- CREATE TABLE IF NOT EXISTS klienci (
--             id SERIAL PRIMARY KEY,
-- 			   imie VARCHAR(50) NOT NULL,
-- 			   miasto VARCHAR(50),
--             saldo DECIMAL(10, 2) DEFAULT 0,
--             aktywny BOOLEAN DEFAULT TRUE
--      );

	 
--  średnik na końcu oddziela polecenie sql

-- id --> jest automatycznie nadawany id, klucz główny 
-- miast, imie --> varchar(str) do 50 znaków,powyżej wywala błąd 
-- saldo --> zmiennoprzecinkowa 10 znaków max do 2 po przecinku zaokrą
-- aktywny bool --> True, albo False 

-- default to domyślna wartość zapisywana jak się nie poda jej przy dodawaniu wiersza
-- NOT NULL nie można dodać wiersza bez wpisania cokolwiek do tjk kolumny 
-- Primary key to jest klucz głowny, czyli głowne id tabeli 


-- Dodawanie nowych wierszy do tabeli
-- Pojedyńcze dodanie

-- INSERT INTO klienci (imie,miast,saldo) BŁĄD:  column "miast" of relation "klienci" does not exist
-- VALUES ('Anna','Kraków',1600)

INSERT INTO klienci (imie,miasto,saldo) 
VALUES ('Anna','Kraków',1600);

-- INSERT INTO
--  nazwa_tabeli
-- (nazwa_kolumny1,nazwa_kolumny2)
-- VALUES
-- (przekazana_wartosc1,przekazana_wartosc2)

-- Aby sprawdzić, czy się pojawiło użyjemy selecta
SELECT * FROM klienci;


-- Dodawanie kilku wartosci w insert

-- SPosób1
INSERT INTO klienci (imie,miasto,saldo) VALUES ('Dominik','Warszawa',800);
INSERT INTO klienci (imie,miasto,saldo) VALUES ('Kamila','Poznań',250);
INSERT INTO klienci (imie,miasto,saldo) VALUES ('Robert','Szczecin',573);

SELECT * FROM klienci;


-- Sposób2
INSERT INTO klienci (imie,miasto,saldo)
VALUES 
		('Alicja','Białowieża',5400),
		('Piotr','Będzin',1800),
		('Adam','Gdynia',10800);

-- Wyciąganie danych z tabeli

-- Wyświetlenie całej tabeli

-- SELECT
-- * (wszystkie kolumny) / wypisanie kolumn z nazwa po przecinku
-- FROM
-- nazwa_tabeli
SELECT * FROM klienci;


-- Wyświetlenie kolumny miasto, saldo

-- SELECT rasa FROM klienci; # ERROR:  column "rasa" does not exist
-- SELECT miasto,saldo, FROM klienci; # ERROR:  syntax error at or near "FROM"

SELECT miasto,saldo FROM klienci;


-- Wyświetlenie z warunkiem WHERE

-- Typowa składnia select
-- WHERE
-- nazwa_kolumny = 'wartosc' (warunek)

SELECT * FROM klienci WHERE miasto = 'Warszawa';


-- operatory > < >= <=
SELECT * FROM klienci WHERE saldo > 1000;
SELECT * FROM klienci WHERE saldo >= 5400;

-- Kilka warunków

SELECT * FROM klienci WHERE saldo > 80 AND miasto = 'Kraków';
-- SELECT * FROM klienci WHERE saldo > 80 AND miasto = "Kraków"; SQL wyala błąd przy cudzysłowiu
SELECT * FROM klienci WHERE saldo > 80 AND saldo < 1000;
-- SELECT * FROM klienci WHERE 1000 > saldo > 80; # ERROR:  syntax error at or near ">"

--  OR to albo to 
SELECT * FROM klienci WHERE miasto = 'Kraków' OR miasto = 'Warszawa';

-- IN
SELECT * FROM klienci WHERE miasto IN ('Kraków','Gdańsk','Poznań');

-- BETWEEN
SELECT * FROM klienci WHERE saldo BETWEEN 240 AND 8000;

-- LIKE
SELECT * FROM klienci WHERE imie LIKE 'A%';

SELECT * FROM klienci WHERE imie LIKE 'An%';

SELECT * FROM klienci WHERE imie LIKE '%mi%';

-- ilość wyplutych wierszy 
SELECT * FROM klienci LIMIT 4;

-- KOlejnosc wyswietlania

SELECT * FROM klienci order by saldo;
SELECT * FROM klienci order by saldo ASC;

SELECT * FROM klienci order by saldo DESC;

SELECT * FROM klienci order by saldo DESC, imie;

SELECT * FROM klienci order by saldo DESC, imie, miasto, aktywny, id;

SELECT * FROM klienci order by id DESC;



-- Edytowanie

SELECT * FROM klienci;

-- UPDATE
-- nazwa_tabeli
-- SET
-- kolumna_z_wartoscia
-- =
-- wartoss_na_jaka_chcemy_zmienic
-- WHERE (warunek)

UPDATE klienci SET aktywny = false;


UPDATE klienci SET aktywny = true WHERE id = 3;

UPDATE klienci SET saldo = 0 WHERE saldo < 2000;


-- Dobra praktyka --> zaczęcie od selecta
SELECT * FROM klienci WHERE saldo = 0;

UPDATE klienci SET saldo = 200 WHERE saldo = 0;

SELECT * FROM klienci;


-- Usuwanie 

-- DELETE FROM
-- nazwa_tabeli
-- warunek


-- DELETE FROM klienci # --> kasuje nam całą tabelę, wszystkie wiersze 

SELECT * FROM klienci WHERE miasto = 'Warszawa';

DELETE FROM klienci WHERE miasto = 'Warszawa';


SELECT * FROM klienci;



--  DDL 
-- dodawanie kolumny



ALTER TABLE klienci ADD COLUMN rasa VARCHAR(100);
-- ALTER TABLE klienci ADD COLUMN rasa VARCHAR(100); BŁĄD:  column "rasa" of relation "klienci" already exists

-- ALTER TABLE
-- nazwa_tabeli
-- ADD COLUMN
-- nazwa_kolumny
-- typ danych 

SELECT * FROM klienci;


ALTER TABLE klienci ADD COLUMN opis VARCHAR(100) DEFAULT 'CZLOWIEK';

SELECT * FROM klienci;

-- Usuwanie kolumny

ALTER TABLE klienci ADD COLUMN dział VARCHAR(100);
SELECT * FROM klienci;

ALTER TABLE klienci DROP COLUMN dział;
SELECT * FROM klienci;

-- ALTER TABLE
-- nazwa_tabeli
--  DROP COLUMN
-- nazwa_kolumny


-- Zmiana nazwy kolumny

ALTER TABLE klienci ADD COLUMN abrakadabra VARCHAR(100);
ALTER TABLE klienci DROP COLUMN rasa;
SELECT * FROM klienci;

ALTER TABLE klienci RENAME COLUMN abrakadabra TO rasa;

-- ALTER TABLE
-- nazwa_tabeli
-- RENAME COLUMN
-- stara_nazwa_kolumny
-- nowa_nazwa_kolumny

SELECT * FROM klienci;


--  Truncate kasowanie danych z tabeli

-- DELETE usuwa jeden wiersz po drugim
-- TRUNCATE kasuje (wielkie tabele to sobie szybciej radzi)

TRUNCATE TABLE klienci;

-- TRUNCATE TABLE
-- nazwa_tabeli

SELECT * FROM klienci;

--  Kasowania 

-- DROP TABLE
-- IF EXISTS (zabezpieczenie)
-- nazwa_tabeli

DROP TABLE IF EXISTS klienciii;


-- TABELA: szkolenie_users (logowanie do aplikacji)
CREATE TABLE IF NOT EXISTS szkolenie_users (
    id SERIAL PRIMARY KEY,
    imie VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    haslo VARCHAR(255) NOT NULL,
    data_rejestracji TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- TABELA: szkolenie_todos (zadania przypisane do uzytkownika)
CREATE TABLE IF NOT EXISTS szkolenie_todos (
    id SERIAL PRIMARY KEY,
    tytul VARCHAR(200) NOT NULL,
    opis TEXT,
    wykonane BOOLEAN DEFAULT FALSE,
    data_dodania TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uzytkownik_id INTEGER REFERENCES szkolenie_users(id) ON DELETE CASCADE
);


SELECT * FROM szkolenie_users;
SELECT * FROM szkolenie_todos;

-- Uzytkownik testowy
INSERT INTO szkolenie_users (imie, email, haslo) VALUES
    ('Anna', 'anna@test.pl', 'haslo123');

-- -- Zadania testowe dla Anny (uzytkownik_id = 1)
INSERT INTO szkolenie_todos (tytul, opis, uzytkownik_id) VALUES
    ('Kupic mleko', 'Z Biedronki, 2 kartony', 1),
    ('Nauczyc sie Flask', 'Routing, szablony, formularze, baza danych', 1),
    ('Zadzwonic do lekarza', 'Umowic wizyte na piatek', 1),
    ('Zrobic pranie', NULL, 1),
    ('Oddac ksiazke do biblioteki', 'Na Dlugiej 15', 1);


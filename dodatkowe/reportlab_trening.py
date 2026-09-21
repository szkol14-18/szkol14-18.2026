"""
Generowanie PDF w Pythonie paczką ReportLab
====================================================
Instalacja:  pip install reportlab

Wersje (stan na wrzesień 2026):
  - Uruchomione i sprawdzone: Python 3.12.7 + reportlab 4.0.4 (działa).
  - Najnowsza reportlab na PyPI to 5.0.1, deklaruje Python od 3.9 do 3.14.
    Na niej ten skrypt NIE był uruchamiany, więc przy problemach użyj 4.0.4:
    pip install reportlab==4.0.4
  - Swoją wersję sprawdzisz poleceniem: pip show reportlab

Plan:
1. Canvas          - "płótno" strony PDF, na którym rysujemy
2. Napisy          - drawString, setFont, setFillColor
3. Linie           - line, setLineWidth, setStrokeColor, rect
4. Tabela          - Table + TableStyle (rysowana na canvasie)
5. BytesIO         - budowanie PDF w pamięci (bez pliku na dysku)
6. Zapis do pliku  - buffer.getvalue() -> open(..., "wb")

Uwaga na układ współrzędnych: punkt (0, 0) to LEWY DOLNY róg strony,
oś Y rośnie W GÓRĘ (odwrotnie niż w ekranowych GUI!).
A4 = 595 x 842 punktów (1 punkt = 1/72 cala).
"""

# Importuje BytesIO, czyli "plik w pamięci" na dane binarne.
from io import BytesIO

# Importuje gotowe kolory (colors.black, colors.grey itd.).
from reportlab.lib import colors
# Importuje rozmiar strony A4 jako parę (szerokość, wysokość) w punktach.
from reportlab.lib.pagesizes import A4
# Importuje jednostkę cm, żeby wymiary podawać w centymetrach.
from reportlab.lib.units import cm
# Importuje moduł do rejestrowania czcionek w ReportLab.
from reportlab.pdfbase import pdfmetrics
# Importuje klasę wczytującą czcionki TrueType z plików .ttf.
from reportlab.pdfbase.ttfonts import TTFont
# Importuje moduł canvas, czyli "płótno" do rysowania na stronie PDF.
from reportlab.pdfgen import canvas
# Importuje klasę tabeli i klasę jej stylu.
from reportlab.platypus import Table, TableStyle

# 0. CZCIONKA - domyślny Helvetica NIE ma polskich znaków (ą, ę, ł...).
#    Trzeba zarejestrować czcionkę TTF. Na Windowsie jest Arial.
#    (Na Linuxie np. DejaVuSans.ttf: /usr/share/fonts/truetype/dejavu/)
# Rejestruje zwykły Arial pod nazwą "Arial", żeby można go używać w setFont.
pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
# Rejestruje pogrubiony Arial pod nazwą "Arial-Bold".
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))


# Definiuje funkcję, która zwraca gotowy PDF jako bajty.
def zbuduj_pdf() -> bytes:
    # Docstring: krótki opis, co robi funkcja.
    """Rysuje PDF w pamięci i zwraca jego bajty."""

    # 5. BUFFER - zamiast nazwy pliku dajemy Canvasowi obiekt BytesIO.
    #    To "plik w pamięci": przydatne w Django/Flask (zwracamy PDF w HTTP
    #    response), przy wysyłce mailem, zapisie do bazy itd.
    # Tworzy pusty bufor w pamięci, do którego trafi PDF.
    buffer = BytesIO()
    # Tworzy płótno zapisujące do bufora, ze stroną w rozmiarze A4.
    c = canvas.Canvas(buffer, pagesize=A4)
    # Rozpakowuje rozmiar A4 na dwie zmienne: szerokość i wysokość strony.
    szerokosc, wysokosc = A4

    # 2. NAPISY
    # Ustawia czcionkę pogrubioną, rozmiar 20 punktów.
    c.setFont("Arial-Bold", 20)
    # Pisze tytuł 2 cm od lewej i 2 cm od góry (y liczymy od dołu strony).
    c.drawString(2 * cm, wysokosc - 2 * cm, "Raport sprzedaży")

    # Przełącza czcionkę na zwykłą, rozmiar 11 punktów.
    c.setFont("Arial", 11)
    # Ustawia szary kolor wypełnienia, czyli kolor tekstu.
    c.setFillColor(colors.grey)
    # Pisze szary podtytuł tuż pod tytułem.
    c.drawString(2 * cm, wysokosc - 2.7 * cm, "Wygenerowano w Pythonie (ReportLab)")
    # Wraca do czarnego, żeby kolejne teksty nie były szare.
    c.setFillColor(colors.black)

    # Pisze "Strona 1" wyrównane do prawej krawędzi (x to prawy koniec napisu).
    c.drawRightString(szerokosc - 2 * cm, wysokosc - 2 * cm, "Strona 1")
    # Pisze stopkę wyśrodkowaną poziomo (x to środek napisu), 1,5 cm od dołu.
    c.drawCentredString(szerokosc / 2, 1.5 * cm, "- stopka -")

    # 3. LINIE i KSZTAŁTY
    # Ustawia granatowy kolor linii i obrysów.
    c.setStrokeColor(colors.darkblue)
    # Ustawia grubość linii na 2 punkty.
    c.setLineWidth(2)
    # Rysuje poziomą linię od lewego do prawego marginesu, pod nagłówkiem.
    c.line(2 * cm, wysokosc - 3.2 * cm, szerokosc - 2 * cm, wysokosc - 3.2 * cm)

    # Zmienia grubość linii na cienką, 0,5 punktu.
    c.setLineWidth(0.5)
    # Rysuje prostokąt: lewy dolny róg (x, y), potem szerokość i wysokość.
    c.rect(2 * cm, wysokosc - 5 * cm, 6 * cm, 1 * cm)

    # 4. TABELA - lista list + styl. Style to krotki:
    #    (NAZWA, (kol_start, wiersz_start), (kol_koniec, wiersz_koniec), wartość)
    #    Indeksy ujemne działają jak w listach: (-1, -1) = ostatnia komórka.
    # Tworzy dane tabeli jako listę wierszy (każdy wiersz to lista komórek).
    dane = [
        # Pierwszy wiersz to nagłówki kolumn.
        ["Produkt", "Ilość", "Cena", "Suma"],
        # Wiersz z laptopami: nazwa, ilość, cena, suma.
        ["Laptop", 2, 3500.00, 7000.00],
        # Wiersz z myszkami.
        ["Myszka", 10, 49.90, 499.00],
        # Wiersz z monitorami.
        ["Monitor", 3, 899.00, 2697.00],
        # Wiersz podsumowania, puste teksty w środkowych komórkach.
        ["RAZEM", "", "", 10196.00],
    ]

    # Tworzy tabelę z danych i ustawia szerokości czterech kolumn.
    tabela = Table(dane, colWidths=[6 * cm, 3 * cm, 3.5 * cm, 3.5 * cm])
    # Nakłada na tabelę styl, czyli listę reguł wyglądu.
    tabela.setStyle(TableStyle([
        # Cała tabela (od komórki 0,0 do ostatniej) zwykłym Arialem.
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),
        # Pierwszy wiersz (nagłówek) pogrubiony, nadpisuje regułę wyżej.
        ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
        # Tło nagłówka na granatowo.
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        # Kolor tekstu w nagłówku na biały, żeby było widać na granacie.
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        # Kolumny od drugiej w prawo wyrównane do prawej (liczby).
        ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
        # Siatka wokół wszystkich komórek: grubość 0,5, kolor szary.
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        # Naprzemienne tło wierszy danych (od 2. do przedostatniego).
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, colors.whitesmoke]),
        # Ostatni wiersz (RAZEM) pogrubiony.
        ("FONTNAME", (0, -1), (-1, -1), "Arial-Bold"),
        # Gruba czarna linia nad ostatnim wierszem, oddziela sumę od danych.
        ("LINEABOVE", (0, -1), (-1, -1), 1.5, colors.black),
    ]))

    # Tabela to obiekt platypus, nie canvas - musimy jej powiedzieć, ile ma
    # miejsca (wrapOn), a dopiero potem narysować w wybranym punkcie (drawOn).
    # Oblicza rozmiar tabeli; bierzemy tylko wysokość, szerokość pomijamy (_).
    _, tab_wysokosc = tabela.wrapOn(c, szerokosc, wysokosc)
    # Rysuje tabelę na płótnie; jej lewy dolny róg ustawiamy tak, by górna krawędź była 6 cm od góry.
    tabela.drawOn(c, 2 * cm, wysokosc - 6 * cm - tab_wysokosc)

    # showPage() kończy bieżącą stronę (kolejne rysowanie = nowa strona).
    # save() domyka PDF i zapisuje go do buffera. BEZ save() PDF będzie pusty!
    # Kończy bieżącą stronę.
    c.showPage()
    # Domyka dokument i zapisuje całą zawartość PDF do bufora.
    c.save()

    # Zwraca całą zawartość bufora jako obiekt bytes, czyli gotowy PDF.
    return buffer.getvalue()


# 6. ZAPIS DO PLIKU - PDF to dane binarne, więc tryb "wb" (write binary),
#    a NIE "w". Bajty z buffera trafiają wprost do pliku.
# Uruchamia poniższy kod tylko przy odpalaniu pliku wprost, nie przy imporcie.
if __name__ == "__main__":
    # Buduje PDF w pamięci i zapisuje jego bajty do zmiennej.
    pdf_bajty = zbuduj_pdf()

    # Otwiera plik raport.pdf do zapisu binarnego; "with" sam go zamknie.
    with open("raport.pdf", "wb") as f:
        # Zapisuje bajty PDF do pliku na dysku.
        f.write(pdf_bajty)

    # Wypisuje komunikat z nazwą pliku i jego rozmiarem w bajtach.
    print(f"Zapisano raport.pdf ({len(pdf_bajty)} bajtów)")

    # W Django zamiast pliku zwrócilibyśmy odpowiedź HTTP:
    #   response = HttpResponse(pdf_bajty, content_type="application/pdf")
    #   response["Content-Disposition"] = 'attachment; filename="raport.pdf"'
    #   return response

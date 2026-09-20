# układ aplikacji typowej flask 

# moj_projekt/
#     app.py
#     templates/
#         base.html
#         index.html
#         lista.html

import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "tajny_klucz_12345" #

def get_db():
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="Password!"
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

# @app.route("/")
# def strona_glowna():
#     return "<h1>Witaj w Flask!</h1>"

@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn, cur = get_db()
    cur.execute(
        "SELECT * FROM szkolenie_todos WHERE uzytkownik_id = %s ORDER BY data_dodania DESC",
        (session["user_id"],)
    )
    zadania = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html",zadania=zadania)

# Logowanie sesji 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        haslo = request.form.get("haslo", "")

        conn, cur = get_db()
        cur.execute(
            "SELECT id, imie FROM szkolenie_users WHERE email = %s AND haslo = %s",
            (email, haslo)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["user_imie"] = user["imie"]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", blad="Bledny email lub haslo!")

    return render_template("login.html")


@app.route("/wyloguj")
def wyloguj():
    session.clear()
    return redirect(url_for("login"))


@app.route('/dodaj', methods=["GET", "POST"])
def dodaj():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        tytul = request.form.get("tytul", "").strip()
        opis = request.form.get("opis", "").strip()

        if tytul:
            conn, cur = get_db()
            cur.execute(
                "INSERT INTO szkolenie_todos (tytul, opis, uzytkownik_id) VALUES (%s, %s, %s)",
                (tytul, opis if opis else None, session["user_id"])
            )
            conn.commit()
            cur.close()
            conn.close()

        return redirect(url_for("home"))
    return render_template("dodaj.html")

@app.route('/edytuj/<int:id>',methods=["GET", "POST"])
def edytuj(id):
    if "user_id" not in session:
            return redirect(url_for("login"))
    
    conn, cur = get_db()

    if request.method == "POST":
        tytul = request.form.get("tytul", "").strip()
        opis = request.form.get("opis", "").strip()

        cur.execute(
            "UPDATE szkolenie_todos SET tytul = %s, opis = %s WHERE id = %s AND uzytkownik_id = %s",
            (tytul, opis if opis else None, id, session["user_id"])
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("home"))

    cur.execute(
        "SELECT * FROM szkolenie_todos WHERE id = %s AND uzytkownik_id = %s",
        (id, session["user_id"])
    )
    zadanie = cur.fetchone()
    cur.close()
    conn.close()

    if not zadanie:
        return redirect(url_for("home"))

    return render_template("edytuj.html", zadanie=zadanie)

    

@app.route('/usun/<int:id>',methods=["GET", "POST"])
def usun(id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        conn, cur = get_db()
        cur.execute(
            "DELETE FROM szkolenie_todos WHERE id = %s AND uzytkownik_id = %s",
            (id, session["user_id"])
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("home"))

    return render_template("usun.html")


@app.route('/wykonane/<int:id>',methods=["GET", "POST"])
def wykonane(id):
    if "user_id" not in session:
            return redirect(url_for("login"))

    conn, cur = get_db()
    cur.execute(
        "UPDATE szkolenie_todos SET wykonane = true WHERE id = %s AND uzytkownik_id = %s",
        (id, session["user_id"])
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("home"))




















@app.route("/lista")
def lista():
    if "user_id" not in session:
            return redirect(url_for("login"))
    produkty = ['laptop','Mysz','Monitor','Klawiatura']
    return render_template("lista.html", produkty=produkty, tytul="Produkt")

# Odczyt parametrów z paska url
# http://127.0.0.1:5000/szukaj?fraza=python&strona=3
@app.route('/szukaj')
def szukaj():
    fraza = request.args.get("fraza","") # szuaknie w linku fraza
    strona = request.args.get('strona',1,type=int)
    return f'<h1>SZukasz: {fraza}, strona {strona}</h1>' 


# Routing Mapowanie ścieżek 

# @app.route('/test_o_nas') # Nie nazywamy w ten sam sposób 
# def strona_glowna():
#     return "<h1>Witaj w Flask!</h1>"

@app.route('/test_o_nas')
def strona_testowa_o_nas():
    return 'Tutaj mamy opis naszej organizacji'

@app.route('/test_kontakt')
def kontakt():
    return '<h1>Kontakt: email: admin@gmail.com Telefon: 112 998 997</h1>'

# @app.route('/test_kontakt') View function mapping is overwriting an existing endpoint function: kontakt
# def kontakt_raz_dwa_trzy():
#     return 'coś innego'

# Dynamiczne parametry
@app.route('/test_profil/<imie>')
def profil(imie):
    return f'<h1>Witaj {imie} </h1>'

@app.route('/test_posts/<int:post_id>') # Przy -1 wywala błąd 
def posts(post_id):
    return f'<h1>Post numer: {post_id} </h1>'
# ! + tab --> skoroszyt html
# /test


if __name__ == "__main__":
    # DEBUG = TRUE to jest tryb developera 
    app.run(debug=True)